import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { normalizeConfig, readConfig, shareURL, visibleCards, victoryText } from '../state.mjs';
const data=JSON.parse(readFileSync(new URL('../content.json',import.meta.url)));
const uno=data.games.find(g=>g.id==='uno');
const mercy=data.games.find(g=>g.id==='mercy');
test('invalid and cross-game packs cannot leak into a deck',()=>{
 assert.deepEqual(normalizeConfig(uno,{packs:['stack','stack','expansion','bogus']}),{packs:['stack'],house:false,continue:false});
 assert.deepEqual(normalizeConfig(mercy,{packs:['stack','expansion'],house:true,continue:true}),{packs:['expansion'],house:true,continue:false});
});
test('classic stacking and No Mercy expansion appear only in the right active deck',()=>{
 assert(!visibleCards(data.cards,uno,{}).some(c=>c.pack));
 const stacked=visibleCards(data.cards,uno,{packs:['stack']});
 assert.equal(stacked.filter(c=>c.pack==='stack').length,4);
 assert(!stacked.some(c=>c.game!=='uno'||c.pack==='speed'));
 assert.equal(visibleCards(data.cards,mercy,{packs:['expansion']}).filter(c=>c.pack==='expansion').length,8);
});
test('both FLIP sides can be searched independently',()=>{
 const flip=data.games.find(g=>g.id==='flip');
 for(const side of ['light','dark']){
  const cards=visibleCards(data.cards,flip,{},side);assert.equal(cards.length,6);assert(cards.every(c=>c.side===side));
 }
});
test('share snapshots round-trip below a GitHub Pages repository prefix',()=>{
 const config={packs:['stack','speed'],house:true,continue:true};
 const link=new URL(shareURL('https://aricbz.github.io/UNO/index.html',uno,config,'#card/uno-stack-pack-stack-1-red'));
 assert.equal(link.pathname,'/UNO/uno.html');assert.equal(link.hash,'#card/uno-stack-pack-stack-1-red');
 assert.deepEqual(readConfig(uno,link.search),config);
});
test('explicit shared official setup overrides saved house settings for the visit',()=>{
 const saved={packs:['swap'],house:true,continue:true};
 assert.deepEqual(readConfig(uno,'?v=1&house=0&continue=1&packs=',saved),{packs:[],house:false,continue:false});
 assert.deepEqual(readConfig(uno,'',saved),saved);
});
test('continue is dependent on house victory, and No Mercy never adopts first-out victory',()=>{
 assert.equal(normalizeConfig(uno,{continue:true}).continue,false);
 assert.match(victoryText(mercy,{house:true}),/last person standing/);
 assert.match(victoryText(mercy,{house:true}),/not specified/);
 assert.match(victoryText(mercy,{}),/OR/);
 assert.match(victoryText(uno,{house:true,continue:true}),/last player holding cards/);
});
test('malformed saved settings normalize safely',()=>{
 assert.deepEqual(normalizeConfig(uno,null),{packs:[],house:false,continue:false});
 assert.deepEqual(normalizeConfig(uno,{packs:'stack',house:'true',continue:1}),{packs:[],house:false,continue:false});
});

test('Liar’s house victory retains challenge and joint-winner conditions',()=>{
 const liars=data.games.find(g=>g.id==='liars');
 assert.match(victoryText(liars,{house:true}),/must survive a challenge/);
 assert.match(victoryText(liars,{house:true}),/joint winners/);
});
