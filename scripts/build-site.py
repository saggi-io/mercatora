"""Build only the public website, excluding repository history, reports and secrets.

Run from any directory: python scripts/build-site.py
Publish _site only after the owner's release approval. No deployment is performed.
"""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
target = root / '_site'
pages = ['index.html', 'impressum.html', 'sdk.html', '404.html']
files = pages + ['CNAME', '.nojekyll', 'robots.txt', 'sitemap.xml',
                 'mercatora_logo.png', 'mercatora_logo_favicon.png']
files += [str(f.relative_to(root)) for f in (root / 'assets').rglob('*')
          if f.is_file() and f.suffix in {'.css', '.woff2', '.txt'}]

# Refuse an unsafe or unexpected destination before replacing a previous build.
if target.is_symlink() or target.resolve().parent != root.resolve():
    raise SystemExit('Unsafe build destination')
for name in files:
    source = root / name
    if source.is_symlink() or not source.is_file() or not source.resolve().is_relative_to(root):
        raise SystemExit(f'Invalid source: {name}')
for name in pages:
    html = (root / name).read_text(encoding='utf-8').lower()
    forbidden = ['<script', '<iframe', '<form', 'javascript:', 'data:text/html']
    if any(value in html for value in forbidden):
        raise SystemExit(f'Unexpected active content: {name}')
if target.exists():
    shutil.rmtree(target)
for name in files:
    dest = target / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / name, dest)
print(f'Public site built: {target} ({len(files)} files). Not deployed.')
