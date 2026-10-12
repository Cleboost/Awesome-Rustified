# Awesome Rustified

A public list of **open source** apps **rewritten in Rust**, often to replace **Electron** clients, **embedded-browser** shells, or heavy **proprietary** desktop apps — same job, less complexity under the hood.

> Listed projects are for reference only. Trademarks belong to their owners. No affiliation implied.

## Table of contents

- [How to read this list](#how-to-read-this-list)
- [Entry template](#entry-template)
- [Music & streaming](#music--streaming)
- [Messaging](#messaging)
- [Backlog](#backlog)
- [Contributing](#contributing)

## How to read this list

| Field | Meaning |
|--------|---------|
| **Replaces / alternative to** | Original product or app type (often closed-source or resource-heavy) |
| **Stack** | Notable Rust libraries / UI toolkit |
| **Why Rust** | Practical wins (RAM, startup time, no Chromium, single binary, etc.) |

Entries are grouped **by category**, not ranked by quality or popularity.

## Entry template

When you add an app, copy this block into the right section:

```markdown
### ProjectName

- **Replaces / alternative to:** …
- **Repo:** https://github.com/…
- **Site:** https://… (optional)
- **License:** …
- **Platforms:** Linux, macOS, Windows, …
- **Stack:** …
- **Why Rust:** one or two factual sentences.
- **Notes:** requirements, known limits, recent rename, etc. (optional)
```

---

## Music & streaming

### Spotifast

- **Replaces / alternative to:** **Spotify** desktop client (often Electron / high memory use)
- **Repo:** [crmne/spotifast](https://github.com/crmne/spotifast)
- **Site:** [spotifast.rocks](https://spotifast.rocks/)
- **License:** MIT
- **Platforms:** Linux, macOS, Windows
- **Stack:** [egui](https://github.com/emilk/egui), [librespot](https://github.com/librespot-org/librespot), [fastframe](https://github.com/crmne/fastframe) (shared foundation with ZapFast)
- **Why Rust:** native client with **no browser engine**; fast startup; typical memory use around **100–250 MB** (vs often **600 MB–1 GB+** for the official app).
- **Notes:** formerly **Fastpotify** (renamed around 0.8.0). Playback via librespot + Spotify Web API; Spotify Connect, library, MPRIS on Linux. Independent project; not affiliated with Spotify AB.

---

## Messaging

### ZapFast

- **Replaces / alternative to:** **WhatsApp Web** / Electron-style desktop wrappers; no official WhatsApp app for Linux
- **Repo:** [crmne/zapfast](https://github.com/crmne/zapfast)
- **Site:** [zapfast.rocks](https://zapfast.rocks/)
- **License:** MIT
- **Platforms:** Linux, macOS, Windows
- **Stack:** egui, [whatsapp-rust](https://github.com/crmne/whatsapp-rust) (whatsmeow lineage), fastframe
- **Why Rust:** single binary, **no Chromium**; opens quickly; ~**200 MB** idle RAM in their published Linux test (vs ~**1.13 GB** for WhatsApp Web + Chromium on the same bench).
- **Notes:** **companion device** linked to your phone (WhatsApp Web model). Sibling of Spotifast on the same fastframe base. Independent project; not affiliated with WhatsApp / Meta.

---

## Backlog

Sandbox for upcoming entries — move each row into a section once the category is clear.

| Project | Replaces (idea) | Repo | List status |
|---------|-----------------|------|-------------|
| *…* | *…* | *…* | draft / ready |

**Planned categories** (add a section only when it has at least one entry):

- Productivity & office
- Development & DevOps
- Social & forums
- Reading & media (non-music)
- System & desktop utilities
- Games & emulation (clients, not game engines)

---

## Contributing

1. Confirm the project is **open source** on GitHub (or equivalent) and the **listed desktop client is primarily Rust**.
2. Add an entry using the template above; one “why Rust” sentence is enough — no marketing fluff.
3. If it replaces paid or closed software, name **what** (e.g. “the X desktop client”, not just “an alternative”).
4. Open a PR or issue with the repo link and proposed category.

**We skip:** unmaintained forks, toy demos with no real use, or thin wrappers around the official app in another shell.

---

## License for this list

**Content** in this repo (text, structure): [CC0 1.0](LICENSE) — use it however you like. Each listed project keeps **its own** license.
