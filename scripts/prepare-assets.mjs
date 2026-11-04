const { default: sharp } = await import(process.env.SHARP_MODULE || 'sharp');
import { readdir, mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
const root = process.cwd();
const source = path.resolve(root, '..');
async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  return (await Promise.all(entries.map(e => e.isDirectory() ? walk(path.join(dir,e.name)) : path.join(dir,e.name)))).flat();
}
await mkdir('assets', { recursive: true });
const manifest = [];
for (const folder of ['Card Assets', 'Game Logos']) {
  for (const file of (await walk(path.join(source, folder))).filter(p => p.endsWith('.png'))) {
    const name = path.basename(file, '.png');
    const output = `assets/${name}.webp`;
    const meta = await sharp(file).metadata();
    await sharp(file).resize({ width: folder === 'Game Logos' ? 640 : 420, withoutEnlargement: true }).webp({ quality: 88, effort: 5 }).toFile(output);
    manifest.push({ source: path.relative(source,file), output, width: meta.width, height: meta.height });
  }
}
await writeFile('assets/manifest.json', JSON.stringify(manifest,null,2)+'\n');
console.log(`Prepared ${manifest.length} faithful WebP derivatives; original PNGs untouched.`);
