# AM Plumbing & Heating

A complete static website for **GitHub Pages**, with the existing `amplumbing.uk` custom domain. Plain HTML, CSS and JavaScript. No Node packages, server, database, API keys or client-side routing are required.

## Publish on GitHub Pages

1. Commit and push these files to the repository's publishing branch.
2. In **Settings → Pages**, choose **Deploy from a branch**, select that branch and **/(root)**, then save.
3. Keep `CNAME` containing `amplumbing.uk`. Keep the existing domain DNS configuration and enable HTTPS when GitHub makes it available.

The checked-in HTML is ready to serve. `.nojekyll` bypasses Jekyll. All normal pages use relative links and work both at the domain root and under a GitHub project path. The custom `404.html` uses a root base URL for the existing custom domain; change that base if moving to a repository subpath without the custom domain.

## Preview

From the repository root:

```sh
python -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Python is only a local preview tool; it is not required by GitHub Pages.

## Edit the site

- Shared presentation: `site.css`
- Mobile navigation, gallery and enquiry behavior: `site.js`
- Content and shared HTML templates: `scripts/build_site.py`
- Terms & Conditions and Privacy Policy wording: `scripts/legal_content.py`
- Project photos: `images/projects/*.webp`, with original JPEGs for enlarged views

After editing the content/templates, run `python scripts/build_site.py` and commit the generated HTML too. This optional build script uses only the Python standard library. There is no deployment build step. The company-specific Gas Safe link is stored in `scripts/business.json`.

The old page URLs remain available. The inherited sample blog pages now provide service information based on the existing services. `Home.html` redirects to the homepage. `sitemap.xml`, `robots.txt`, page descriptions, canonical URLs and sharing metadata are included.

## Contact enquiries

GitHub Pages cannot process form submissions. The contact page validates the enquiry, then opens a prefilled message in the visitor's email app addressed to `info@amplumbing.uk`. **The visitor must send the message.** The site never claims a draft was sent. Direct email and telephone links are also available. Automatic delivery without an email application would require a separately configured form service and an updated privacy notice.

## Business and policy details

Preserved: +44 7838 628381; the separately displayed original additional number 0795685621; info@amplumbing.uk; hr@amplumbing.uk; 662 High Road, N12 0NL; company 10809396; VAT 378119079; London services; Gas Safe registration link; the ten-flat Hendon project; safety and recruitment information.

The original additional number has ten digits and is preserved as supplied. Confirm it before relying on it as a working number.

Terms & Conditions (version 2) and the Privacy Policy are included and linked throughout the site. The Terms cover both website use and the supply of plumbing, heating and gas work: scope, existing and concealed pipework, pressure changes, testing records, aftercare, evidence retention, liability, insurers' claims and cancellation. They only bind a customer if they are given to the customer with the quotation before the job is agreed, so quotes and invoices must link to or attach them.

Operational commitments written into the policies that the business must actually follow (change the wording in `scripts/legal_content.py` if not): quotes valid 30 days; payment due 14 days from invoice if the quote is silent; pressure and test results recorded and given on request; removed fittings may be kept and photographed; retention periods (6 years for job records, up to 15 for core safety/test records, 12 months for lapsed enquiries, 6 months for unsuccessful applicants); insurer and territory statement (Zurich, United Kingdom). No fixed fee or warranty length has been invented.

Policy reference material:
- https://ico.org.uk/for-organisations/advice-for-small-organisations/privacy-notices-and-cookies/how-to-write-a-privacy-notice-and-what-goes-in-it/
- https://www.legislation.gov.uk/uksi/2013/3134/contents

No analytics, advertising, external fonts, embedded maps, reCAPTCHA or form-processing scripts are loaded. There is no cookie banner because this implementation does not set non-essential cookies.

## Validation

```sh
python scripts/check_site.py
node --check site.js
```

The checker validates local links and fragment IDs, image references, page structure, legal links, company details and the custom domain. Browser QA covers desktop/mobile layouts, menu behavior, gallery filtering, enlargement and service selection.

## Logo

The header uses `images/am-plumbing-logo-v2.png`, a transparent PNG generated with the built-in image tool. The original logo is preserved as `images/AMPLUMBING-LOGO-2.png`. The generation prompt is recorded in `images/logo-prompt.txt`.

## Updated logo and profile icons

The header now uses `images/brand/am-plumbing-logo-wide.png`, with the lower line spanning the full wordmark width. The website uses `images/brand/favicon.png` for its favicon. Transparent icon and blue-and-white social PNG masters are in `images/brand/`, with separately named Instagram and WhatsApp copies. `am-plumbing-logo-pack.zip` contains the complete PNG set and usage notes. Earlier versions are preserved.

## Invoice and social artwork

Ready-to-use files are in `images/brand/invoice/` (A4 letterhead header and footer at 300 dpi, logo on white and transparent, email-signature logo) and `images/brand/social/` (Facebook, LinkedIn, X and Google Business banners, a 1200x630 link-share image, square profile pictures, and a white logo for dark backgrounds). They are generated from the masters in `images/brand/` by `python scripts/make_brand_assets.py` (needs Pillow; not part of the website build). The invoice footer links to the Terms & Conditions so that they are incorporated into each job.
