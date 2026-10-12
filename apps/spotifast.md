# Spotifast

[← Back to list](../README.md)

| | |
|---|---|
| **Replaces** | Spotify desktop client (often Electron) |
| **Repo** | [github.com/crmne/spotifast](https://github.com/crmne/spotifast) |
| **Site** | [spotifast.rocks](https://spotifast.rocks/) |
| **License** | MIT |
| **Platforms** | Linux, macOS, Windows |

## Summary

Spotifast is a Spotify client written in Rust with [egui](https://github.com/emilk/egui). Audio goes through [librespot](https://github.com/librespot-org/librespot). There is no embedded browser engine: one native binary, fast startup, and lower typical memory use than the official desktop app.

## Stack

- **UI:** egui on [fastframe](https://github.com/crmne/fastframe) (shared with ZapFast)
- **Playback:** librespot, Spotify Web API
- **Linux:** MPRIS media controls, Spotify Connect

## Why Rust

Published figures land around **100–250 MB** RAM versus often **600 MB–1 GB+** for Spotify’s Electron client, with startup in well under a second on typical hardware.

## Notes

- Formerly **Fastpotify** (renamed around v0.8.0); settings generally carry over.
- Independent project; not affiliated with Spotify AB.
