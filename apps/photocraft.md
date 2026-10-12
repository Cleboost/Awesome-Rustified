# PhotoCraft

[← Back to list](../README.md)

| | |
|---|---|
| **Category** | creative-adobe |
| **Sort** | 1 |
| **Icon** | https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/128x128/apps/ai.storyteller.photocraft.png |
| **Name** | PhotoCraft |
| **Repo** | https://github.com/storytold/photocraft |
| **Description** | Clean-room **Photoshop**–style editor — layers, masks, adjustment layers, brushes, PSD. Native + WebAssembly. |
| **Replaces** | Adobe Photoshop–style raster editing |
| **Site** | [getartcraft.com/apps/photocraft](https://getartcraft.com/apps/photocraft) |
| **Suite** | [ArtCraft](https://getartcraft.com/) · [storytold](https://github.com/storytold) |
| **License** | MIT OR Apache-2.0 |
| **Platforms** | macOS, Windows, Linux, FreeBSD, WebAssembly |

## Summary

PhotoCraft is a clean-room image editor written entirely in Rust: layers, masks, adjustment layers, layer styles, type, vectors, brushes, and real PSD files — offline and open source.

## Stack

- Shared UI and tooling via [craft-libs](https://github.com/storytold/craft-libs) (`craft-ui`, in-repo imaging crates)
- Installs and updates with [ArtCraft Launcher](https://github.com/storytold/craft-launcher)

## Why Rust

One native codebase for desktop and WASM targets, with GPU-backed compositing and format work kept in Rust crates instead of a Chromium shell.

## Notes

Status: **early alpha**. Not affiliated with Adobe. Trademark names are used only to describe the workflow being reimplemented.
