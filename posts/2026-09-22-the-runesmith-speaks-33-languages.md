---
title: The Runesmith now speaks 33 languages
date: 2026-09-22
number: 5
period: September 5 to 22
summary: The whole game is now translated into 33 languages, from Japanese to Ukrainian. Also in this update: a fix for the freeze when a big hit drops a mountain of loot, crafted gear you can finally pull out of a bench, and better tools for testing.
cover: statue-hades.jpg
cover_alt: A stone statue of Hades holding a bident on a sunny tropical shore
commits: a32fa49638..fdfe747a63
---

## 33 languages

The Runesmith is now playable in **33 languages**: English, Turkish, German, French, Spanish, Italian, Portuguese, Polish, Russian, Ukrainian, Czech, Slovak, Slovenian, Hungarian, Romanian, Bulgarian, Greek, Dutch, Danish, Swedish, Norwegian, Finnish, Estonian, Latvian, Lithuanian, Japanese, Korean, Chinese (Simplified and Traditional), Thai, Vietnamese, Indonesian and Arabic.

Translating is the easy half. The hard half is finding every single piece of text. Item names and tooltips were already set up for translation, but menus, panels and buttons had plenty of words typed straight into the interface over the months. Those would have stayed in English no matter which language you picked.

So I built a sweep tool. It walks through every scene and every interface prefab the game uses, finds each text label, and flags the ones that aren't hooked up to the translation system yet. After a review, it connects them all in one go. Every language then got its own audit pass for missing or broken entries, and the English text got a typo pass of its own.

If you play in a language other than English and something reads oddly, I'd genuinely love to hear about it on the Discord.

## No more freeze on big hits

Gathering in The Runesmith works like a small fight: the harder you hit a node, the more you get out of it. With a strong rune setup, a single swing at an ore vein could drop well over a hundred pieces.

Each of those pieces was being written into your inventory one at a time, and every write told the whole interface to refresh. A big hit meant over a hundred refreshes in a row, and the game would hitch for a second or more. Your reward for building a great gathering setup was a stutter.

Now everything a single hit drops is gathered up first and added to your bag in one go. The same hit, one refresh, no freeze. It applies to ore, stone, trees, plants and animal corpses alike.

## Pulling crafted gear out of a bench

Quick transfer (alt-click to move an item between your bag and an open storage) used to refuse any equipment or glyph. That was meant to stop gear from being dropped somewhere it didn't belong, but it also meant a weapon or tool you'd just crafted was stuck inside the bench unless you dragged it out by hand. Equipment and glyphs now quick-transfer like everything else, with the few places they really can't go (your hotbar, the rune pages) still protected.

## Tools for testing

A couple of things players won't see, but which make every future update faster to test:

- A **build checklist** that runs the routine pre-release checks in one window. It exists because an earlier demo build shipped with the previous version number on the main menu.
- A **rune generator** that drops a hand-picked rune straight into my inventory, built through the exact same path as a real forged rune.
- A **world tier tool** to jump to any map at any difficulty without grinding the requirements first.

## What's next

The demo is getting ready for **Steam Next Fest, October 19 to 26**. I'll write about what's going into it soon. If you'd like to try it, the best thing you can do right now is add The Runesmith to your wishlist.
