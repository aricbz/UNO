<div align="center">

<br>

```
██╗   ██╗███╗   ██╗ ██████╗     ████████╗██╗  ██╗███████╗    ██████╗ ██╗   ██╗██╗     ███████╗███████╗
██║   ██║████╗  ██║██╔═══██╗       ██╔══╝██║  ██║██╔════╝    ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██║   ██║██╔██╗ ██║██║   ██║       ██║   ███████║█████╗      ██████╔╝██║   ██║██║     █████╗  ███████╗
██║   ██║██║╚██╗██║██║   ██║       ██║   ██╔══██║██╔══╝      ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
╚██████╔╝██║ ╚████║╚██████╔╝       ██║   ██║  ██║███████╗    ██║  ██║╚██████╔╝███████╗███████╗███████║
 ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
```

### **Never argue about UNO rules again.**

A growing collection of mobile-optimized, beautifully designed rulebooks for UNO variants —  
built for NFC tags and designed to live *inside* the game box.

<br>

[![Live Site](https://img.shields.io/badge/🃏_Play_Now-Live_Site-E8272A?style=for-the-badge&labelColor=1a1a1a)](https://aricbz.github.io/UNO/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-gold?style=for-the-badge&labelColor=1a1a1a)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
![Made with love](https://img.shields.io/badge/Made_with-❤️-E8272A?style=for-the-badge&labelColor=1a1a1a)

<br>

</div>

---

## 🎯 What is this?

You're mid-game. Someone plays a Wild Draw 4. Chaos erupts. *Can you stack on that? Does Reverse count as Skip with two players?* Someone pulls out the crumpled paper rulebook. Someone else Googles it. You get five different answers.

**This project fixes that.**

UNO — The Rules is a dark-mode, mobile-first web app that puts the complete, unambiguous rulebook for every UNO variant one tap away. Stick an NFC tag inside your game box, program it with the link, and every time someone needs a rule, they just tap their phone.

No app to download. No login. No ads. Just the rules.

---

## 🃏 Game Editions

| Edition | Players | Age | Vibe |
|---|---|---|---|
| 🃏 **UNO Classic** | 2–10 | 7+ | The original. Still chaotic. |
| 🔄 **UNO Flip!** | 2–10 | 7+ | Light side vs. brutal Dark side |
| 🤥 **Liar's UNO** | 2–6 | 7+ | Bluffing meets card-matching |
| 💀 **Show 'Em No Mercy** | 2–6 | 7+ | Stack without limits. Feel nothing. |
| 🔥 **UNO Dare** *(18+)* | 2–10 | 18+ | Draw cards or face a dare |

Each edition includes full rules, a complete card reference with tap-to-expand descriptions, special modes, and colorblind accessibility symbols.

---

## ✨ Features

- **📱 Mobile-first** — designed for the phone in your hand at the table, not a desktop browser
- **🌑 Dark mode always** — easy on the eyes in dim lighting
- **🃏 Interactive card reference** — tap any card to see its full rules in a modal
- **♿ Colorblind accessible** — every card has a graphic symbol alongside its color
- **📡 NFC-ready** — program a tag, stick it in the box, done
- **⚡ Zero dependencies** — pure HTML/CSS/JS, no frameworks, no build steps
- **📦 Add-on packs** — Classic UNO includes Stack Pack, Speed Pack, Swap Pack, and Reverse Pack rules
- **🔞 Adults Only section** — UNO Dare has its own experience with dare levels and a die system

---

## 🚀 Getting Started

No installation. No build tools. No server required.

```bash
git clone https://github.com/aricbz/UNO.git
cd uno-the-rules
open index.html
```

Or just drop the files anywhere and open `index.html` in a browser. That's it.

---

## 📡 NFC Setup (the fun part)

This is what the project was built for. Here's how to set it up:

1. **Buy NFC stickers** — NTAG213 tags work great and are cheap (~$0.10–$0.50 each)
2. **Use an NFC writing app** — [NFC Tools](https://www.wakdev.com/en/apps/nfc-tools.html) (iOS/Android) is free and simple
3. **Write your URL** — set the record type to `URL` and point it at the hosted page for your game edition (e.g. `https://aricbz.github.io/UNO/uno.html`)
4. **Stick the tag inside the box lid** — that's it

Anyone at the table taps their phone to the box and the rules open instantly. No app download. No QR code awkwardness. Just magic.

---

## 🗂️ Project Structure

```
uno-the-rules/
├── index.html                  # Edition selector — the home page
├── uno.html                    # UNO Classic + all add-on packs
├── uno-flip.html               # UNO Flip! (Light & Dark sides)
├── liars-uno.html              # Liar's UNO
├── uno-show-em-no-mercy.html   # Show 'Em No Mercy + Expansion Pack
├── uno-dare.html               # UNO Dare — Adults Only (18+)
├── LICENSE
└── README.md
```

Each HTML file is fully self-contained — inline styles, inline scripts, no external assets beyond Google Fonts.

---

## 🎨 Design

The UI takes cues from the physical cards themselves: bold typography, high contrast, vivid color coding. Each edition has its own visual identity — the neon-red glow of Dare, the deep navy grid of Liar's, the punishing crimson of No Mercy.

**Typography:** [Boldonse](https://fonts.google.com/specimen/Boldonse) for headers · [Rubik](https://fonts.google.com/specimen/Rubik) for body · [Tilt Neon](https://fonts.google.com/specimen/Tilt+Neon) for Dare accents

**Color system:**

| Token | Hex | Used for |
|---|---|---|
| `--red` | `#E8272A` | UNO red, actions, warnings |
| `--gold` | `#D4A017` | Classic UNO accent |
| `--blue` | `#005BAA` | Liar's UNO |
| `--green` | `#00A651` | Speed Pack |
| `--purple` | `#9B5CF6` | Stack Pack, No Mercy expansion |
| `--teal` | `#00B5A3` | Reverse Pack |

---

## 🤝 Contributing

Found a rule that's wrong? Missing an edition? Have a sick idea for a new add-on pack?

1. Fork the repo
2. Create a branch: `git checkout -b fix/wild-draw-4-challenge-rule`
3. Make your changes
4. Open a pull request with a clear description

For new game editions, try to match the existing structure and visual system. Each rulebook should feel like it belongs in the same family.

---

## ⚠️ Disclaimer

UNO is a trademark of Mattel, Inc. This is an unofficial, fan-made rules reference — not affiliated with or endorsed by Mattel in any way. Built for personal use and shared because arguing about rules is the worst part of game night.

---

## 📄 License

This project is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

You can share it, remix it, and build on it — just give credit, keep it non-commercial, and share under the same terms.

Copyright © 2026 Ariel Cobos

---

<div align="center">

**Brought to you by Ari** · because nobody should lose a friendship over a Draw 4

<br>

*Now go shuffle.*

</div>
