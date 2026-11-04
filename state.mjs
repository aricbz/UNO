export function normalizeConfig(game, value = {}) {
  value = value && typeof value === 'object' ? value : {};
  return { packs: [...new Set(Array.isArray(value.packs) ? value.packs.filter(p => game.packs.includes(p)) : [])], house: value.house === true, continue: game.id !== 'mercy' && value.house === true && value.continue === true };
}
export function readConfig(game, search, saved = {}) {
  const p = new URLSearchParams(search);
  if (p.get('v') === '1') return normalizeConfig(game, { packs: (p.get('packs') || '').split(','), house: p.get('house') === '1', continue: p.get('continue') === '1' });
  return normalizeConfig(game, saved);
}
export function shareURL(base, game, config, hash = '#learn') {
  const url = new URL(game.route, base);
  const c = normalizeConfig(game, config);
  url.search = new URLSearchParams({v:'1',packs:c.packs.join(','),house:c.house?'1':'0',continue:c.continue?'1':'0'}).toString();
  url.hash = hash;
  return url.href;
}
export function visibleCards(cards, game, config, side = 'all') {
  const c = normalizeConfig(game, config);
  return cards.filter(card => card.game === game.id && (!card.pack || c.packs.includes(card.pack)) && (side === 'all' || !card.side || card.side === side));
}
export function victoryText(game, config) {
  const c = normalizeConfig(game, config);
  if (!c.house) return game.learn.win;
  if (game.id === 'mercy') return 'Our table: the last person standing wins. Going out is not an automatic win. Empty-hand handling is not specified by this house rule; agree on it before playing.';
  return 'Our table: the first player to empty their hand wins.' + (game.id === 'liars' ? ' A final Liar’s card must survive a challenge. The official Wild Liar’s Challenge can produce joint winners; agree before play if your table wants to change that.' : '') + (c.continue ? ' Keep playing until the last player holding cards is the loser.' : ' Enable “Play to the last loser” if your group wants to continue.');
}
