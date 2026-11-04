"""Build the single source-backed content catalog. No network or dependencies."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
sources = {}
for file in sorted((ROOT/'sources/Extracted Text').glob('*-en.md')):
    text = file.read_text()
    key = file.stem.removesuffix('-rules-en')
    title = re.search(r'^title: "(.*)"', text, re.M).group(1)
    url = re.search(r'^source_url: "(.*)"', text, re.M).group(1)
    sections, page, side, current = [], 1, '', None
    for line in text.splitlines():
        if line.startswith('## Source PDF page'):
            page = int(re.search(r'page (\d+)',line).group(1)); current = None
        elif line.startswith('## Visual context'):
            break
        elif re.match(r'^#{3,} ', line):
            heading = line.lstrip('# ').strip()
            if heading in ['Publisher notice','Publisher identification']: current = None; continue
            if heading in ['LIGHT SIDE','DARK SIDE']: side = heading; current = None; continue
            current = {'id': slug(side+' '+heading), 'title': heading, 'page': page, 'side': side, 'text': ''}
            sections.append(current)
        elif current is not None:
            current['text'] += line+'\n'
    sources[key] = {'id':key, 'title':title, 'url':url, 'pdf':f'sources/{file.stem}.pdf', 'transcript':f'sources/Extracted Text/{file.name}', 'sections':[s | {'text':s['text'].strip()} for s in sections if s['text'].strip()]}

games = [
 dict(id='uno', title='UNO Classic', short='The original rivalry.', description='The one that started it all. Match, skip, reverse. Make it your own with four add-on packs.', logo='uno-logo', color='#ffda47', meta='2–10 players · Ages 7+', source='uno-base-game', packs=['swap','speed','stack','reverse'], route='uno.html', tag='THE ORIGINAL', hero=['uno-skip-red','uno-reverse-green','uno-draw-2-blue']),
 dict(id='mercy', title='Show ’Em No Mercy', short='Friendships, tested.', description='Bigger penalties. Relentless stacking. Get to 25 cards and you’re out.', logo='uno-show-em-no-mercy-logo', color='#ff7185', meta='2–6 players · Ages 7+', source='uno-show-em-no-mercy', packs=['expansion'], route='uno-show-em-no-mercy.html', tag='NO HOLDING BACK', hero=['uno-no-mercy-wild-draw-10','uno-no-mercy-discard-all-yellow','uno-no-mercy-wild-draw-6']),
 dict(id='flip', title='UNO FLIP!', short='There’s a darker side.', description='One deck. Two personalities. Flip the entire game from light to dark and back again.', logo='uno-flip-logo', color='#c6a0ff', meta='2–10 players · Ages 7+', source='uno-flip', packs=[], route='uno-flip.html', tag='DOUBLE THE TROUBLE', hero=['uno-flip-light-flip-blue','uno-flip-dark-flip-teal','uno-flip-dark-draw-5-teal']),
 dict(id='liars', title='Liar’s UNO', short='Keep a straight face.', description='Play it face down. Say what it is. The truth is entirely up to you.', logo='liars-uno-logo', color='#8da6ff', meta='2–6 players · Ages 7+', source='liars-uno', packs=[], route='liars-uno.html', tag='TRUST NO ONE', hero=['liars-uno-liar-7-red','liars-uno-liar-wild-draw-4','liars-uno-wild-liars-challenge']),
 dict(id='dare', title='UNO Dare Adults Only', short='How far will you go?', description='Draw or take the dare. Adults Only artwork, with clearly marked standard Dare reference rules.', logo='uno-dare-adults-only-logo', color='#f5f5f5', meta='Adults Only · Source limitation', source='uno-dare', packs=[], route='uno-dare-adults-only.html', tag='AFTER HOURS', hero=['uno-dare-adults-only-skip-blue','uno-dare-adults-only-wild-draw-2-or-dare-1','uno-dare-adults-only-draw-2-or-dare-2-red'])
]
packs = {p:{'id':p,'name':p.title()+' Pack','source':'uno-'+p+'-pack','requires':'uno'} for p in ['swap','speed','stack','reverse']}
packs['expansion']={'id':'expansion','name':'No Mercy Expansion','source':'uno-show-em-no-mercy-expansion-pack','requires':'mercy'}

# Each summary is authored from the supplied sheet; the complete section remains available.
effects = {
'uno-draw-2-blue':('Draw Two','Next player draws 2 and misses their turn.','Draw Two Card'),
'uno-reverse-green':('Reverse','Reverse the direction of play.','Reverse Card'),
'uno-skip-red':('Skip','The next player loses their turn.','Skip Card'),
'uno-wild':('Wild','Choose the color. Play it even if you have another playable card.','Wild Card'),
'uno-wild-draw-4':('Wild Draw Four','Choose a color; next player draws 4 and loses their turn. Only legal if you have no card matching the current color.','Wild Draw 4 Card'),
'uno-wild-shuffle-hands':('Wild Shuffle Hands','Artwork available, but this card is absent from the supplied 108-card rule sheet. Effect not verified.',''),
'uno-wild-customizable':('Customizable Wild','Artwork available. No predefined effect is documented by this source; agree on a rule before use.',''),
'uno-swap-pack-swap-1-yellow':('Swap 1','Take a random card from another player and give them a card you choose.','SWAP 1'),
'uno-swap-pack-refresh-hand-blue':('Refresh Hand','Put your hand under the discard pile and draw the same number of fresh cards.','REFRESH HAND'),
'uno-swap-pack-wild-force-trade':('Wild Force Trade','Choose two players to exchange hands, then choose a color. You may include yourself.','WILD FORCE TRADE'),
'uno-swap-pack-wild-pass-hands':('Wild Pass Hands','Everyone passes their hand in the current direction. Then you choose a color.','WILD PASS HANDS'),
'uno-speed-pack-speed-up-1-yellow':('Speed Up 1','Play as a number card. Its speed icon raises the speed by one for the next player.','SPEED PACK ICONS'),
'uno-speed-pack-speed-up-5-red':('Speed Up 5','The 5 is the card’s number. Its single speed icon raises speed by one, not five.','SPEED PACK ICONS'),
'uno-speed-pack-wild-double-speed-up':('Wild Double Speed Up','Choose a color and increase the speed by two levels for the next player.','SPEED PACK ICONS'),
'uno-stack-pack-stack-1-red':('Stack 1','Add 1 to a Stack penalty; responding to a Draw card requires matching its color or chosen color.','STACK 1'),
'uno-stack-pack-stack-2-blue':('Stack 2','Works like Stack 1, but adds 2 to the penalty.','STACK 2'),
'uno-stack-pack-wild-stack-3':('Wild Stack 3','Play on any card or respond to any Draw or Stack card. Choose a color; add 3 to the penalty.','WILD STACK 3'),
'uno-stack-pack-wild-stack-number':('Wild Stack Number','Reveal until a number card appears. Its number determines the added draw penalty. Put revealed cards under the discard pile.','WILD STACK NUMBER'),
'uno-reverse-pack-reverse-draw-2-green':('Reverse Draw 2','Reverse direction; next player in that direction draws 2 and loses their turn. Matches any Reverse or Draw 2.','REVERSE DRAW 2'),
'uno-reverse-pack-reverse-skip-yellow':('Reverse Skip','Reverse direction, then skip the next player in that direction. Matches any Reverse or Skip.','REVERSE SKIP'),
'uno-reverse-pack-wild-power-reverse':('Wild Power Reverse','Reverse direction, choose a color, and take another turn.','WILD POWER REVERSE'),
'uno-reverse-pack-wild-no-u':('Wild No U','Respond to a draw action by reversing it onto its player and choosing a color. Or play as a Wild that reverses.','WILD NO U'),
'uno-no-mercy-draw-4-blue':('Draw Four','Next player draws 4 and loses their turn, unless they stack a qualifying Draw card.','Draw Four Card'),
'uno-no-mercy-skip-everyone-green':('Skip Everyone','Skip every other player and take another turn.','Skip Everyone Card'),
'uno-no-mercy-discard-all-yellow':('Discard All','Discard all cards of this card’s color. Put the extra cards underneath it.','Discard All Card'),
'uno-no-mercy-wild-reverse-draw-4':('Wild Reverse Draw 4','Reverse; next player in the new direction draws 4 and loses their turn. With two players, YOU draw 4 unless you stack.','Wild Reverse Draw 4 Card'),
'uno-no-mercy-wild-draw-6':('Wild Draw 6','Next player draws 6 and loses their turn, unless they stack a qualifying Draw card.','Wild Draw 6 Card'),
'uno-no-mercy-wild-draw-10':('Wild Draw 10','Next player draws 10 and loses their turn, unless they stack a qualifying Draw card.','Wild Draw 10 Card'),
'uno-no-mercy-wild-color-roulette':('Wild Color Roulette','Next player chooses a color, reveals until that color appears, takes every revealed card, and loses their turn. Wilds do not count.','Wild Color Roulette Card'),
'uno-no-mercy-7-swap-marker':('7’s Swap','Playing any 7 means you must exchange hands with another player of your choice.','7’s Swap'),
'uno-no-mercy-0-pass-marker':('0’s Pass','Playing any 0 makes everyone pass their hand in the current direction.','0’s Pass'),
'uno-no-mercy-expansion-10-yellow':('10’s Play Again','Play a 10 and immediately take another turn.','10’s PLAY AGAIN'),
'uno-no-mercy-expansion-10-play-again-marker':('10’s Play Again marker','This reminder marker identifies the 10’s extra-turn effect.','10’s PLAY AGAIN'),
'uno-no-mercy-expansion-wild-discard-all':('Wild Discard All','Choose a color to discard from your hand. Put this Wild on top, then choose the color that continues play.','WILD DISCARD ALL'),
'uno-no-mercy-expansion-wild-reverse-draw-8':('Wild Reverse Draw 8','Reverse direction; the next player in that direction draws 8 and loses their turn. Choose the color.','WILD REVERSE DRAW 8'),
'uno-no-mercy-expansion-wild-final-attack':('Wild Final Attack','Reveal your hand. Next player draws 1 per Action or Wild card and loses their turn. At 7+, they draw 25 and everyone else draws 5. Choose a color.','WILD FINAL ATTACK'),
'uno-no-mercy-expansion-wild-sudden-death':('Wild Sudden Death','Everyone, including you, draws until holding 24 cards. Choose a color.','WILD SUDDEN DEATH'),
'uno-no-mercy-mercy-coin':('Mercy coin','Once per game on your turn: discard your entire hand to the bottom, then draw 7. Check the source discrepancy below.','MERCY'),
'uno-no-mercy-no-mercy-coin':('No Mercy coin','Once per game on your turn: double a Draw card’s penalty. Its new value also applies when stacking.','NO MERCY'),
'liars-uno-wild-liars-challenge':('Wild Liar’s Challenge','Choose a color; others offer a face-down card. Challenge until everyone is challenged or you find a truthful player. Multiple players may win together.','Wild Liar\'s Challenge card'),
'liars-uno-liar-wild-draw-4':('Liar’s Wild Draw 4','Play face down. Announce it; next player draws 4 and loses their turn. Choose a color.','Wild Draw 4 card'),
'liars-uno-liar-draw-2-red':('Liar’s Draw Two','Play face down. If the declared action stands, next player draws 2 and loses their turn.','Draw Two card'),
'liars-uno-liar-reverse-red':('Liar’s Reverse','Play face down. If the declared action stands, reverse direction.','Reverse card'),
'liars-uno-liar-skip-red':('Liar’s Skip','Play face down. If the declared action stands, skip the next player.','Skip card'),
'uno-dare-adults-only-skip-blue':('Skip','Standard Dare reference: the next player loses their turn. Adults Only mechanics are not verified.','Skip Card'),
'uno-dare-adults-only-reverse-green':('Reverse','Standard Dare reference: reverse direction. Adults Only mechanics are not verified.','Reverse Card'),
'uno-dare-adults-only-draw-2-or-dare-2-red':('Draw 2 or Dare','Standard Dare reference: choose draw 2 or complete the numbered dare. This does not verify the Adults Only die or dare levels.','Dare Card'),
'uno-dare-adults-only-wild-draw-2-or-dare-1':('Wild Draw 2 or Dare','Standard Dare reference: draw 2 or take the numbered dare; the player of the Wild chooses the color. Adults Only details unverified.','Wild Dare Card'),
}
for side in ['light','dark']:
    names={'reverse':('Reverse','Reverse the direction of play.','Reverse Card'),'wild':('Wild','Choose a color, even if you have another playable card.','Wild Card'),'flip':('Flip','Flip the discard pile, draw pile, and everyone’s hands to the other side.','Flip Card')}
    if side=='light':names|={'draw-1':('Draw One','Next player draws 1 and misses their turn.','Draw One Card'),'skip':('Skip','Next player loses their turn.','Skip Card'),'wild-draw-2':('Wild Draw Two','Choose a color. Next player draws 2 and loses their turn. Only legal with no card matching the current color.','Wild Draw 2 Card')}
    else:names|={'draw-5':('Draw Five','Next player draws 5 and misses their turn.','Draw Five Card'),'skip-everyone':('Skip Everyone','Skip everyone else and take another turn.','Skip Everyone Card'),'wild-draw-color':('Wild Draw Color','Choose a color; next player draws until finding it and loses their turn. Only legal with no card matching the current color.','Wild Draw Color Card')}
    for asset in (ROOT/'assets').glob(f'uno-flip-{side}-*.webp'):
        stem=asset.stem.removeprefix(f'uno-flip-{side}-');stem=re.sub(r'-(blue|red|green|teal|orange|purple)$','',stem)
        effects[asset.stem]=names[stem]
for n in ['0','1','7']:
    for liar in [False,True]:
        key=f'liars-uno-{"liar-" if liar else ""}{n}-red'
        effect={'0':'Everyone passes their hand in the current direction.','1':'Match by color or number.','7':'Swap hands with another player of your choice.'}[n]
        effects[key]=(f'{"Liar’s" if liar else "Regular"} {n}', ('Play face down and declare your card. ' if liar else 'Play face up. ')+effect, {'0':"0's Pass",'7':"7's Swap",'1':'Playing a Liar\'s Card' if liar else 'Playing a Regular Card'}[n])

manifest=json.loads((ROOT/'assets/manifest.json').read_text()); cards=[]
for item in manifest:
    name=Path(item['output']).stem
    if 'Game Logos/' in item['source'] or '/Packaging/' in item['source']:continue
    game= 'flip' if name.startswith('uno-flip') else 'liars' if name.startswith('liars-uno') else 'mercy' if name.startswith('uno-no-mercy') else 'dare' if name.startswith('uno-dare') else 'uno'
    pack=next((p for p in ['swap','speed','stack','reverse'] if f'uno-{p}-pack-' in name),None)
    if game=='mercy' and ('/Expansion/' in item['source']):pack='expansion'
    side='light' if '-light-' in name else 'dark' if '-dark-' in name else None
    source=packs[pack]['source'] if pack else next(g['source'] for g in games if g['id']==game)
    title,summary,heading=effects[name]
    matches=[s for s in sources[source]['sections'] if s['title'].casefold()==heading.casefold() and (not side or s['side']==side.upper()+' SIDE')]
    if heading and not matches:raise ValueError(f'Missing source section: {name} => {heading}')
    cards.append(dict(id=name,title=title,summary=summary,game=game,pack=pack,side=side,source=source,section=matches[0]['id'] if matches else None,image=item['output'],status='substitute' if game=='dare' else 'gap' if not heading else 'official'))
# Shared action types have no separate No Mercy artwork. Reuse the supplied classic image explicitly.
for name,heading in [('uno-draw-2-blue','Draw Two Card'),('uno-reverse-green','Reverse Card'),('uno-skip-red','Skip Card')]:
    orig=next(c for c in cards if c['id']==name);section=next(s for s in sources['uno-show-em-no-mercy']['sections'] if s['title']==heading)
    cards.append(orig|dict(id='mercy-'+name,game='mercy',source='uno-show-em-no-mercy',section=section['id'],summary={'Draw Two Card':'Next player draws 2 and loses their turn, unless they stack a qualifying Draw card.','Reverse Card':'Reverse direction. With two players, skip the other player and take another turn.','Skip Card':'Next player loses their turn.'}[heading],artNote='Classic UNO artwork shown as a visual reference for this shared action.'))

learn={
'uno':dict(setup=['Deal 7 cards to each player. The player with the highest number drawn is the dealer; symbols count as zero.','Put the rest face down as the draw pile. Turn one card over to start the discard pile.','The player left of the dealer starts. Opening actions have special effects—see the source-backed details below.'],turn='Match the top card by color, number, or symbol. If you cannot play, draw ONE card; you may play it immediately if it matches. You may choose to draw instead; after drawing, you may play only that drawn card.',win='Official: empty your hand to end a round, score opponents’ remaining cards, and race to 500 points.',tips=[('Can I stack a +2 on a +2?','The classic sheet makes the next player draw and miss their turn. It does not allow avoiding that penalty with another Draw card. Enable Stack Pack to see that pack’s specific responses.'),('Can I play a Wild Draw Four?','Only if your hand has no card matching the current COLOR. A matching number or symbol in another color does not prevent it. A successful challenge makes the offender draw 4; a failed challenge makes you draw 6.'),('What happens with an opening action?','Draw Two: the first player draws 2 and is skipped. Skip: skip the first player. Reverse: the dealer starts and play goes right. Wild: the player left of the dealer calls the color. Wild Draw Four: return it to the deck and reveal another card.'),('What if the draw pile runs out?','Reshuffle the discard pile and keep playing.'),('How do I score?','Numbers: face value. Draw Two, Reverse and Skip: 20. Wild and Wild Draw Four: 50. The first player to reach 500 wins; the sheet also offers an alternative lowest-score method.')]),
'mercy':dict(setup=['Choose a dealer. Shuffle and deal 7 cards to each player.','Start a draw pile; reveal a number card for the discard pile. Ignore opening action cards and reveal again.','Player left of the dealer starts clockwise. With the expansion, declare your coin side at the start.'],turn='Match by color, number, or symbol. If you have no match, draw UNTIL you draw a playable card, then play it.',win='Official: win by playing your final card OR by being the only player not knocked out.',tips=[('How does stacking work?','Respond with a Draw card equal to or higher than the LAST Draw card—not the total. Example: +4 followed by +6 means the next player needs +6 or higher, or draws 10.'),('When am I knocked out?','At 25 OR MORE cards. Set aside the eliminated hand until the deck needs reshuffling. The expansion Mercy coin has different threshold wording—see Sources.'),('What do 7 and 0 do?','7: you must swap with a chosen player. 0: everyone passes hands in the current direction.'),('Two-player Reverse Draw 4?','You reverse and skip the other player, then YOU draw 4. You can stack to send it back.'),('Optional scoring?','Numbers: face value; colored actions: 20; Wild actions: 50. Add 250 per knocked-out player; their eliminated hand does not score. First to 1000 wins.')]),
'flip':dict(setup=['Align the whole deck so all Light Sides face the same way. The player with the highest Light Side number is the dealer.','Deal 7 cards with Light Sides facing their holders. Draw pile: Light Side down. Discard pile: Light Side up.','Player left of the dealer starts. Begin on the Light Side; a starting Flip switches immediately to Dark.'],turn='Match on the side currently in play by color, number, or symbol. If you cannot play, draw ONE card and optionally play it if it matches. Keep new cards facing the same way as your hand.',win='Official: empty your hand to end the round. Score the side the round ENDED ON. First to 500 points wins.',tips=[('What actually flips?','First the whole discard pile (the Flip just played goes to the bottom), then the draw pile, then every hand. Ignore actions newly exposed on top. If the new top is Wild, the Flip player chooses the color.'),('Can I challenge a Wild penalty?','Both Wild Draw Two and Wild Draw Color require no matching-color card in the player’s hand. If guilty, the offender takes the penalty. If innocent, the challenger takes the original penalty plus 2.'),('How do I score?','Numbers: face value; Draw One: 10; Draw Five, Reverse, Skip, Flip: 20; Skip Everyone: 30; Wild: 40; Wild Draw Two: 50; Wild Draw Color: 60. Use the side on which the round ended.')]),
'liars':dict(setup=['Shuffle and deal 7 cards to each player.','Create draw and discard piles. Ignore opening actions; treat an opening Liar’s number as a normal card.','Player left of the dealer starts clockwise. Regular cards go face UP; Liar’s cards go face DOWN.'],turn='Match a Regular card normally, or play a Liar’s card face down and announce a plausible matching card. Any player may challenge before the next turn begins. If you cannot play, draw ONE and play it if possible.',win='Official: going out wins if the final card survives any challenge. Wild Liar’s Challenge can produce joint winners.',tips=[('Truth or bluff?','Challenged truth: challenger draws 1. Caught lying: take your card back AND draw 1. If unchallenged before the next turn, the declared action takes effect even if you lied.'),('Can a regular card go face down?','No. If caught, take it back and draw 6.'),('What about 7 and 0?','7 swaps with a chosen player; 0 passes all hands in the current direction. If challenged, draw the penalty card AFTER the exchange.'),('Wild Liar’s Challenge?','Choose a color; others offer face-down cards declared as that color (Wilds do not count). Challenge players until everyone is challenged or someone is truthful. A liar takes their card back and draws 1. The first truthful player and all still-unchallenged players discard their offered cards under the Wild. Multiple players going out this way win together.'),('Optional scoring?','Numbers: face value; Skip, Reverse, Draw Two: 20; Wild Draw Four and Wild Liar’s Challenge: 50. First to 500 wins.')]),
'dare':dict(setup=['Substitute reference only: the source is standard UNO Dare CDY11, NOT the Adults Only leaflet.','Standard Dare: choose a Dare List card, choose a dealer by highest drawn number, then deal 7 cards.','Standard Dare starts left of the dealer. Consult your physical Adults Only leaflet for its die, Truth result, reverse result, and dare levels.'],turn='Standard Dare reference: match by color, number, or symbol. Draw ONE if needed; optionally play that card. A Dare offers draw 2 or the numbered challenge on the chosen Dare List.',win='Standard Dare source: empty your hand to end a round, then score toward 500 points. Adults Only-specific rules remain unverified.',tips=[('What does the substitute establish?','In standard Dare, the target draws 2 or attempts the numbered dare. Failing the dare means drawing 2. Wild Dare also lets its player choose the color. These instructions do not verify the Adults Only die or four dare levels.'),('Where are the actual dares?','They are on separate Dare List cards, absent from the PDF. Use your physical game; no dares have been invented here.'),('Can I use this as a complete Adults Only guide?','No. The source is an accepted substitute, and all references here are labeled accordingly. Use the physical Adults Only leaflet for edition-specific mechanics.'),('Standard Dare scoring?','Numbers: face value; Reverse, Skip and Dare: 20; Wild Dare: 50. First to 500 wins. A final Dare still makes the next player draw 2 or perform the dare before scoring.')])
}
for g in games:g['learn']=learn[g['id']]
out={'games':games,'packs':packs,'sources':sources,'cards':cards}
(ROOT/'content.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(games)} editions, {len(packs)} packs, {len(cards)} card/marker references, {len(sources)} sources.')
