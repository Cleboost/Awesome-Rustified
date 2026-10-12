# LightCraft

[← Back to list](../README.md)

| | |
|---|---|
| **Category** | creative-adobe |
| **Icon** | https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/128x128/apps/ai.storyteller.lightcraft.png |
| **Name** | LightCraft |
| **Repo** | https://github.com/storytold/lightcraft |
| **Description** | Clean-room **Lightroom**–style library and raw development. Desktop + WASM; MCP server for agent workflows. |
| **Replaces** | Adobe Lightroom–style library and raw development |
| **Site** | [getartcraft.com/apps/lightcraft](https://getartcraft.com/apps/lightcraft) |
| **Suite** | [ArtCraft](https://getartcraft.com/) · [storytold](https://github.com/storytold) |
| **License** | MIT OR Apache-2.0 |
| **Platforms** | macOS, Windows, Linux, WebAssembly |

## Summary

LightCraft is a non-destructive photo library and raw developer in pure Rust — catalog, develop, export — on the desktop or in the browser, with an MCP server so agents can drive workflows end to end.

## Stack

- [craft-libs](https://github.com/storytold/craft-libs) shared UI and platform code
- MCP server for automation ([README](https://github.com/storytold/lightcraft))

## Why Rust

Same Rust core on native OSes and WASM; heavy pixel pipelines stay in-process without embedding a browser engine for the desktop app.

## Notes

Status: **young and moving fast**. Not affiliated with Adobe.
