"""Generate real static entry points and an isolated deployment directory."""
from pathlib import Path
import json, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/build-content.py')],check=True)
data=json.loads((ROOT/'content.json').read_text())
template='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#101010"><meta name="description" content="{description}"><title>{title} — UNO: The Rulez</title><link rel="icon" href="uno-rules-icon.png"><link rel="stylesheet" href="styles.css"><script type="module" src="app.mjs"></script></head><body><div id="app"><div class="error"><h1>Shuffling the rules…</h1><p>Your game-night companion is loading.</p></div></div><noscript><p>This interactive reference needs JavaScript. <a href="sources/README.md">Browse the original rules instead.</a></p></noscript></body></html>
'''
for game in [dict(route='index.html',title='Your game-night companion',description='Visual rules for five UNO editions. Cards, add-on packs, and your table’s house rules.'),*data['games']]:
    (ROOT/game['route']).write_text(template.format(title=game['title'],description=game['description']))
aliases={'liars_uno.html':'liars-uno.html','uno-dare.html':'uno-dare-adults-only.html','UNO Show Em No Mercy.html':'uno-show-em-no-mercy.html','UNO Show Em No Mercy Full Rules.html':'uno-show-em-no-mercy.html'}
for old,new in aliases.items():
    (ROOT/old).write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UNO: The Rulez — moved reference</title><script>location.replace({json.dumps(new)}+location.search+location.hash)</script><p>This rulebook has moved. <a href="{new}">Open the current reference</a>.</p></html>')
# GitHub Pages must serve source transcriptions unchanged in either publish layout.
(ROOT/'.nojekyll').touch()
dist=ROOT/'dist'
if dist.exists():shutil.rmtree(dist)
dist.mkdir()
for file in ['index.html','uno.html','uno-show-em-no-mercy.html','uno-flip.html','liars-uno.html','uno-dare-adults-only.html','uno-rules-icon.png','app.mjs','state.mjs','styles.css','content.json']:
    shutil.copy2(ROOT/file,dist/file)
for folder in ['assets','sources']:shutil.copytree(ROOT/folder,dist/folder)
for old in aliases:shutil.copy2(ROOT/old,dist/old)
(dist/'.nojekyll').touch()
print('Static site built in dist/; no bundler, server runtime, or history fallback needed.')
