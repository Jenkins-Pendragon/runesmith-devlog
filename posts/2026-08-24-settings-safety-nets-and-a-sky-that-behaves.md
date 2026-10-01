---
title: Settings, safety nets and a sky that behaves
date: 2026-08-24
number: 2
period: August 14 to 24
summary: A real pause menu and settings screen, a no-penalty rescue for when you fall off the world, hits you can actually feel, and a day-night cycle that stays in its best hours.
cover: world-vista.jpg
cover_alt: Golden birch trees on a grassy cliff above a turquoise sea, with snowy peaks behind
commits: 8ec2ebbacf..0f1ce07377
---

This stretch was about the things players only notice when they're missing. None of it is a headline feature, all of it makes the game feel finished.

## Pause, and one settings screen for everything

Pressing **Esc** now opens a proper pause menu. From there, and from the main menu's Options button, you reach the same settings screen with **Video**, **Audio** and **Game** tabs. There is only one settings screen in the whole game, so the two can never drift apart.

New in the Game tab: **mouse sensitivity** and **invert Y**. Both apply instantly and stick between sessions.

## Falling off the world is an accident, not a punishment

![Artemis' statue overlooking the coast]({{base}}/assets/img/artemis-overlook.jpg)
*Plenty of cliffs to slip off*

The world has a lot of edges: cliffs, coasts, the occasional gap in the terrain. If you ever fall out of the playable area, the screen fades out and you're placed back on solid ground. **No health, experience or items are lost.**

The fun detail is *where* you land. The game keeps a short memory of the last few spots where you stood safely. It deliberately puts you back on one of the older ones, because the newest is usually the exact edge you just slipped off, and nobody wants to fall twice.

## Hits you can feel

Taking damage now pulses a red vignette and a slight lens warp at the edges of the screen, for both enemy attacks and damage over time like poison. It's brief and subtle, but you always know when something got through.

## A sky that stays in its best hours

The world runs on a full day-night cycle. I added a way to keep a map's clock inside a chosen window, so a map can live in a long golden afternoon instead of cycling through a dark night that hides the art. Each map can choose whether time bounces back and forth inside that window or wraps around.

## Smaller things

- **Right-click to equip.** With the equipment or rune panel open, right-clicking gear, glyphs or runes in your inventory equips them straight away. With the panels closed, right-click still opens the usual menu, so Drop and Destroy are always one click away.
- Fixed a camera jitter while running and jumping. The camera was reading the character's position one step too early every frame; it now waits for the final pose.
- Text font fixes across several menus.

Next time: the game gets its voice.
