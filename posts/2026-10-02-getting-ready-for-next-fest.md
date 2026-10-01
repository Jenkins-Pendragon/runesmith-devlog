---
title: Getting ready for Next Fest
date: 2026-10-02
number: 6
period: October 2
summary: The demo is heading to Steam Next Fest, October 19 to 26. This update is all about the first hour and the last minute of it: hits that land harder, forging that reveals its rarity, a starter rune you get to pick, and a proper goodbye when the demo ends.
cover: demo-over-panel.jpg
cover_alt: The end of demo screen with a personal summary, three full game cards and a Wishlist on Steam button
commits: ff7a5aee91..04e9bd619a
---

The Runesmith demo goes live on Steam ahead of **Next Fest, October 19 to 26**. A festival demo gets one shot: people try a dozen games in an afternoon and remember the ones that felt good in the first few minutes. So this round of work wasn't about new content. It was about the moments that decide whether someone keeps playing, and whether they wishlist when they stop.

## Hits that actually stop

When a heavy hit lands, the game freezes your character for a split second. It's called hitstop, and it's most of what makes a swing feel solid. Mine was measured in frames, which sounds fine until you remember that a frame at 144 fps lasts about 7 milliseconds. On a fast PC the freeze was so short you couldn't see it. It's now measured in real time, so the hit feels the same at 60 fps and at 240.

Two other timings were backwards:

- **Killing a boss** gave you a shorter slow motion moment than killing a regular enemy. Now the boss kill gets a proper 0.6 second slowdown, the longest in the game.
- **Critical hits while gathering** froze the game for 0.4 seconds. That's great once. Across hundreds of swings at ore and trees, it felt like lag. It's down to 0.1 seconds, enough to notice a crit without breaking the rhythm.

## Forging that knows what it made

![Six god rune icons glowing red on a dark blue background]({{base}}/assets/img/god-runes.jpg)
*One rune family per god*

Before, a rune's rarity was decided at the very end of the forging animation, so the animation itself had no idea what it was building. A common rune and a rare one looked exactly the same until the result popped up.

Now the rarity is rolled the moment you press forge, and the animation plays along. The glow takes on the rarity's color, and the higher you go, the bigger the finale: Epic, Legendary and Mythic each get a stronger flash and a harder punch. Glyph forging works the same way.

The sound followed. Forging a rune used to play a breaking gem sound, which was the wrong message entirely. Now a normal result plays a craft complete sound, Epic and above get their own rare sound, and upgrading a rune plays a level up when it succeeds and the breaking gem when it fails. Items that finish in the crafting queue while you're watching also chime when they're done.

## Pick your first rune

Your first real rune used to show up late, after a stretch of gathering and crafting. Runes are what this game is about, so that wait was a problem.

Now the second main quest ends with a choice of three Rare runes: one from **Hades**, one from **Hermes** and one from **Demeter**. Each leans into its god's style, and I made sure every stat on them does something you'll notice inside the demo. Pick the one that matches how you want to play.

## A proper ending

When you beat the demo's final boss, a closing screen now opens with a short personal summary: how many runes you forged, how many creatures you hunted, how long you played, and your finest rune, shown in its rarity color. Below that are three cards with a taste of what the full game adds: six gods, seven biomes and runes that go up to +15.

The **Wishlist on Steam** button now opens the store page right inside the Steam overlay, so you never leave the game. If the overlay is turned off, it opens the page in the Steam client instead. The whole screen is translated into all 33 languages.

*(The cover shows the screen with sample numbers.)*

## Smaller fixes

- In rune tooltips, the stat lines were squeezed so tight that numbers like 1.13% could blur into each other, and the star rating at the end of a line sometimes dropped to the next one. They now have normal spacing and stay on one line.

## What's next

Next up is testing all of this in full playthroughs before the demo goes live. If you'd like to be there on day one, the best thing you can do right now is add The Runesmith to your wishlist.
