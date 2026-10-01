---
title: Giving the forge a voice
date: 2026-08-26
number: 3
period: August 25 to 26
summary: Two days rebuilding how The Runesmith sounds. Every sound now comes from one place, the main menu finally makes noise, and every button in the game clicks. Cutscenes also stopped letting you open your inventory mid-scene.
cover: hideout.jpg
cover_alt: The player's hideout, a marble plaza with a small temple, a statue and a teleport ring
commits: ed9883cc00..65581a6aba
---

Sound in a crafting game is half the feedback. The ring of a hammer, the thud of ore breaking, the little click when an item lands in your bag. Until now, those sounds were wired up wherever each system happened to need them, scattered across dozens of files. That made the game hard to tune and easy to break. So I tore it out and rebuilt it.

## One place for every sound

There is now a single **sound director** that listens to what happens in the game (a rune forged, a tool striking ore, a prop placed in your hideout, a level gained) and decides what to play. Gameplay code no longer plays sounds directly. If a moment sounds wrong, there is exactly one line to change.

All of the sound settings live in **one sound library** file: which clips a moment can pick from (without repeating the same one twice in a row), volume, pitch, how far a sound carries in the world, and a minimum gap so nothing can spam. A side effect I didn't expect: the main menu used to be completely silent, because its old sound setup only existed once you were in-game. With the library on its own, the menu now has sound like everywhere else.

To make tuning easier, there's also a small in-editor overlay that lists every sound as it plays, so I can hear and see exactly what fires and when.

## Every button clicks

The game has a lot of buttons: inventory slots, quest rows, recipe cards, menus. Instead of touching each one, a single hook now gives **every button in the game** a hover and click sound, including the ones that are created on the fly.

## Cutscenes are cutscenes

![The statue of Hades on the shore]({{base}}/assets/img/statue-hades.jpg)
*Hades, waiting for his reveal*

During the god reveals and the boss entrance, the game used to stop you moving and hide the HUD, but your shortcuts still worked. You could open the inventory, the crafting menu or the weapon wheel in the middle of a cinematic. Now the game knows when a cutscene is playing, and all of those shortcuts wait until it ends.

## Smaller things

- When you finish a quest, its reward window now opens by itself if nothing else is on screen. Before, you had to click the quest to notice the reward was waiting, and some players never did.
- The god reveal cutscene got another polish pass on timing and camera.
- Weapon wheel and radial menu fixes.

Next time: achievements, and making the smallest action in the game (picking up a twig) feel right.
