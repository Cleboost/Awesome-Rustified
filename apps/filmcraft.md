# FilmCraft

[← Back to list](../README.md)

| | |
|---|---|
| **Category** | creative-adobe |
| **Sort** | 3 |
| **Icon** | https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/128x128/apps/ai.storyteller.filmcraft.png |
| **Name** | FilmCraft |
| **Repo** | https://github.com/storytold/filmcraft |
| **Description** | Clean-room **Premiere Pro**–style NLE — timeline editing, color, sound. macOS, Windows, Linux, WASM. |
| **Replaces** | Adobe Premiere Pro–style nonlinear video editing |
| **Site** | [getartcraft.com/apps/filmcraft](https://getartcraft.com/apps/filmcraft) |
| **Suite** | [ArtCraft](https://getartcraft.com/) · [storytold](https://github.com/storytold) |
| **License** | MIT OR Apache-2.0 |
| **Platforms** | macOS, Windows, Linux, WebAssembly |

## Summary

FilmCraft targets the Premiere-style workflow: timeline editing, color, and sound in a clean-room NLE written from scratch in Rust, native on desktop and available via WebAssembly.

## Stack

- [craft-libs](https://github.com/storytold/craft-libs)
- Optional web front-end (`filmcraft-web`) alongside the desktop app

## Why Rust

Video pipelines and UI share one language; avoids shipping Electron/Chromium for a timeline-centric creative tool.

## Notes

Status: **young and moving fast**. Not affiliated with Adobe.
