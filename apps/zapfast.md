# ZapFast

[← Back to list](../README.md)

| | |
|---|---|
| **Replaces** | WhatsApp Web / Electron wrappers (no official Linux app) |
| **Repo** | [github.com/crmne/zapfast](https://github.com/crmne/zapfast) |
| **Site** | [zapfast.rocks](https://zapfast.rocks/) |
| **License** | MIT |
| **Platforms** | Linux, macOS, Windows |

## Summary

ZapFast is a WhatsApp client for desktop, built in Rust with egui. It talks to WhatsApp through [whatsapp-rust](https://github.com/crmne/whatsapp-rust) (whatsmeow lineage). Layout is familiar if you use WhatsApp Web, but the app stays a single native process without Chromium.

## Stack

- **UI:** egui on fastframe (sibling of Spotifast)
- **Protocol:** whatsapp-rust, companion-device linking (phone stays primary)

## Why Rust

On their published Linux comparison, ZapFast opens in under a second and uses about **200 MB** idle RAM, versus about **1.13 GB** for WhatsApp Web plus Chromium.

## Notes

- You link your phone as a **companion device**, same model as WhatsApp Web.
- Independent project; not affiliated with WhatsApp or Meta.
