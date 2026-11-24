"""Check local links, fragments, shared metadata and key content in generated pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0;self.main=0;self.lang=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
  if tag=='html':self.lang=a.get('lang')=='en-GB'
  for key in ('href','src'):
   if a.get(key):self.refs.append(a[key])
pages={}
for file in ROOT.rglob('*.html'):
 if '.git' in file.parts:continue
 page=Page();page.feed(file.read_text(encoding='utf-8-sig'));pages[file.resolve()]=page
errors=[]
for file,page in pages.items():
 if file.name!='Home.html':
  if page.h1!=1 or page.main!=1 or not page.lang:errors.append(f'{file.name}: invalid landmarks or heading')
  if len(page.ids)!=len(set(page.ids)):errors.append(f'{file.name}: duplicate IDs')
  for legal in ['Terms-and-Conditions.html','Privacy-Policy.html']:
   if not any(ref.endswith(legal) for ref in page.refs):errors.append(f'{file.name}: missing {legal}')
  text=file.read_text(encoding='utf-8')
  for expected in ['10809396','378119079','info@amplumbing.uk','+447838628381']:
   if expected not in text:errors.append(f'{file.name}: missing business detail {expected}')
 for ref in page.refs:
  url=urlsplit(ref)
  if url.scheme or url.netloc:continue
  target=((ROOT/unquote(url.path).lstrip('/')) if url.path.startswith('/') else (file.parent/unquote(url.path))).resolve() if url.path else file
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{file.relative_to(ROOT)}: broken path {ref}')
  elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:errors.append(f'{file.name}: broken fragment {ref}')
for name,ids in {'Terms-and-Conditions.html':['scope','existing','pressure','testing','aftercare','defects','liability','insurers','cancellation'],'Privacy-Policy.html':['sharing','retention','rights']}.items():
 found=pages[(ROOT/name).resolve()].ids
 for i in ids:
  if i not in found:errors.append(f'{name}: missing section {i}')
assert (ROOT/'CNAME').read_text().strip()=='amplumbing.uk'
assert (ROOT/'.nojekyll').exists()
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; local paths, fragments, landmarks, legal links and company details.')
