"""Check source provenance, routes, assets and page deployment references."""
import hashlib,json,re
from pathlib import Path
from urllib.parse import unquote
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'content.json').read_text())
assert len(d['games'])==5 and len(d['sources'])==10
ids=set()
for c in d['cards']:
    assert c['id'] not in ids,c['id'];ids.add(c['id'])
    assert (R/c['image']).is_file(),c['image']
    s=d['sources'][c['source']]
    if c['status']=='official':assert any(sec['id']==c['section'] for sec in s['sections']),c['id']
    if c['game']=='dare':assert c['status']=='substitute'
for s in d['sources'].values():
    assert (R/s['pdf']).read_bytes().startswith(b'%PDF-')
    transcript=(R/s['transcript']).read_text()
    sha=re.search(r'^source_sha256: (\w+)',transcript,re.M).group(1)
    assert hashlib.sha256((R/s['pdf']).read_bytes()).hexdigest()==sha,s['id']
    assert s['url'].startswith('https://service.mattel.com/')
for g in d['games']:
    assert (R/'assets'/f"{g['logo']}.webp").is_file()
    for n in g['hero']:assert (R/'assets'/f'{n}.webp').is_file()
    for p in g['packs']:assert d['packs'][p]['requires']==g['id']
for route in json.loads((R/'docs/legacy-routes.json').read_text()):
    assert (R/route).is_file() and (R/'dist'/route).is_file(),route
for p in (R/'dist').glob('*.html'):
    for asset in re.findall(r'(?:href|src)="([^"]+)"',p.read_text()):
        if not asset.startswith(('https:', '#')):assert (p.parent/unquote(asset)).exists(),(p,asset)
assert len(json.loads((R/'assets/manifest.json').read_text()))==75
assert 'prefers-reduced-motion:reduce' in (R/'styles.css').read_text()
print(f"Validated {len(d['cards'])} card mappings, 75 images, 10 PDF hashes, expansion requirements, and all six legacy entry pages.")
