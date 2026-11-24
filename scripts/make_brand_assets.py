"""Build invoice and social-media artwork from the logo masters in images/brand/.

Run: python scripts/make_brand_assets.py   (needs Pillow; not used by the website build)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / 'images' / 'brand'
INV = BRAND / 'invoice'
SOC = BRAND / 'social'
for d in (INV, SOC):
    d.mkdir(exist_ok=True)

NAVY = (12, 37, 59)        # site navy #0c253b
NAVY2 = (18, 58, 94)
INK = (17, 44, 68)         # wordmark navy #112c44
BLUE = (7, 89, 221)        # royal blue #0759dd
GREY = (92, 107, 122)
FONTS = Path('C:/Windows/Fonts')


def font(size, bold=False):
    return ImageFont.truetype(str(FONTS / ('segoeuib.ttf' if bold else 'segoeui.ttf')), size)


def clean(img):
    """Remove faint alpha haze left by the image generator and crop tight."""
    img = img.convert('RGBA')
    a = img.getchannel('A').point(lambda v: 0 if v < 24 else v)
    img.putalpha(a)
    return img.crop(a.point(lambda v: 255 if v > 24 else 0).getbbox())


def white(img):
    out = Image.new('RGBA', img.size, (255, 255, 255, 0))
    out.putalpha(img.getchannel('A'))
    return out


def fit_width(img, w):
    return img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)


def fit_height(img, h):
    return img.resize((round(img.width * h / img.height), h), Image.LANCZOS)


def paste(base, img, xy):
    base.alpha_composite(img, xy)


def text_width(draw, s, f):
    return draw.textlength(s, font=f)


logo = clean(Image.open(BRAND / 'am-plumbing-logo-wide.png'))
mono = clean(Image.open(BRAND / 'am-monogram-transparent.png'))
logo_white = white(logo)
mono_white = white(mono)

# ---------- Logo variants ----------
pad = round(logo.width * 0.04)
tight = Image.new('RGBA', (logo.width + 2 * pad, logo.height + 2 * pad), (0, 0, 0, 0))
paste(tight, logo, (pad, pad))
tight.save(INV / 'logo-transparent.png')
on_white = Image.new('RGBA', tight.size, (255, 255, 255, 255))
paste(on_white, tight, (0, 0))
on_white.convert('RGB').save(INV / 'logo-on-white.png')
wpad = Image.new('RGBA', tight.size, (0, 0, 0, 0))
paste(wpad, logo_white, (pad, pad))
wpad.save(SOC / 'logo-white-transparent.png')

# ---------- Invoice header (A4 width at 300 dpi) ----------
W = 2480
H = 470
hdr = Image.new('RGBA', (W, H), (255, 255, 255, 255))
d = ImageDraw.Draw(hdr)
lg = fit_height(logo, 210)
paste(hdr, lg, (150, 100))
lines = [('AM PLUMBING & HEATING LTD', True), ('662 High Road, London N12 0NL', False),
         ('+44 7838 628381', False), ('info@amplumbing.uk  |  amplumbing.uk', False),
         ('Company no. 10809396  |  VAT no. 378119079', False)]
y = 92
for s, b in lines:
    f = font(40 if b else 36, b)
    d.text((W - 150 - text_width(d, s, f), y), s, font=f, fill=INK if b else GREY)
    y += 56
d.rectangle([150, H - 40, W - 150, H - 32], fill=BLUE)
hdr.convert('RGB').save(INV / 'invoice-header-a4.png', dpi=(300, 300))

# ---------- Invoice footer (A4 width at 300 dpi) ----------
FH = 230
ftr = Image.new('RGBA', (W, FH), (255, 255, 255, 255))
d = ImageDraw.Draw(ftr)
d.rectangle([150, 28, W - 150, 34], fill=BLUE)
rows = [
    ('AM PLUMBING & HEATING LTD  |  Registered in England & Wales  |  Company no. 10809396  |  VAT no. 378119079', font(34, True), INK),
    ('Gas Safe registered business  |  Public liability insured', font(32), GREY),
    ('Our Terms & Conditions apply to all work: amplumbing.uk/Terms-and-Conditions.html   |   Privacy: amplumbing.uk/Privacy-Policy.html', font(32), GREY),
]
y = 62
for s, f, c in rows:
    d.text(((W - text_width(d, s, f)) / 2, y), s, font=f, fill=c)
    y += 52
ftr.convert('RGB').save(INV / 'invoice-footer-a4.png', dpi=(300, 300))

# ---------- Email signature ----------
sig = Image.new('RGBA', (720, 240), (255, 255, 255, 255))
lg = fit_width(logo, 640)
paste(sig, lg, ((720 - lg.width) // 2, (240 - lg.height) // 2))
sig.convert('RGB').save(INV / 'email-signature-logo.png')


# ---------- Social banners ----------
def banner(w, h, name, logo_w, tag_size, sub_size, centre_y=0.5):
    img = Image.new('RGBA', (w, h), NAVY)
    # soft diagonal depth + blue pipe-style accent bars along the bottom
    ov = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.polygon([(w * 0.55, 0), (w, 0), (w, h), (w * 0.35, h)], fill=NAVY2 + (150,))
    img.alpha_composite(ov)
    d = ImageDraw.Draw(img)
    bar = max(8, h // 40)
    d.rectangle([0, h - bar, w, h], fill=BLUE)
    lg = fit_width(logo_white, logo_w)
    tag = 'Better plumbing. Better heating. Better living.'
    sub = 'Plumbing  |  Heating  |  Gas  |  Air conditioning  |  Across London'
    ft, fs = font(tag_size, True), font(sub_size)
    block = lg.height + round(tag_size * 0.9) + tag_size + round(sub_size * 0.8) + sub_size
    top = round((h - bar) * centre_y - block / 2)
    paste(img, lg, ((w - lg.width) // 2, top))
    y = top + lg.height + round(tag_size * 0.9)
    d.text(((w - text_width(d, tag, ft)) / 2, y), tag, font=ft, fill=(255, 255, 255))
    y += tag_size + round(sub_size * 0.8)
    d.text(((w - text_width(d, sub, fs)) / 2, y), sub, font=fs, fill=(170, 200, 235))
    img.convert('RGB').save(SOC / name, quality=95)


banner(1640, 624, 'facebook-cover-1640x624.png', 640, 40, 26, 0.50)
banner(1584, 396, 'linkedin-banner-1584x396.png', 420, 30, 20, 0.50)
banner(1500, 500, 'x-header-1500x500.png', 520, 34, 22, 0.50)
banner(1200, 630, 'link-share-1200x630.png', 560, 36, 24, 0.50)
banner(1080, 608, 'google-business-cover-1080x608.png', 460, 30, 20, 0.50)

# ---------- Profile pictures (square masters + circle preview) ----------
for src, dst in [('am-social-profile.png', 'profile-square-1254.png')]:
    im = Image.open(BRAND / src).convert('RGB')
    im.save(SOC / dst)
    for size in (1080, 400):
        im.resize((size, size), Image.LANCZOS).save(SOC / f'profile-square-{size}.png')
# navy variant: white symbol on navy
prof = Image.new('RGBA', (1080, 1080), NAVY)
m = fit_width(mono_white, 640)
paste(prof, m, ((1080 - m.width) // 2, (1080 - m.height) // 2))
prof.convert('RGB').save(SOC / 'profile-navy-1080.png')
print('Brand assets written to', BRAND)
