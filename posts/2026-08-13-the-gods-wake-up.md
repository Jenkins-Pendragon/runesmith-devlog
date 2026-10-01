---
title: The gods wake up
date: 2026-08-13
number: 1
period: August 10 to 13
summary: The six god statues now shatter and reassemble in their reveal, the first boss gets a proper entrance, and every bench can finally reach into your chests. Plus a long, quiet optimization pass.
cover: statue-artemis.jpg
cover_alt: A stone statue of Artemis drawing her bow on a grassy hill
commits: 5c46a59366..57c3167252
---

Welcome to the first devlog for **The Runesmith**. You play a fallen god in a mortal world, and the only way home is through the forge: mining, hunting and farming raw materials, then turning them into runes blessed by the old gods.

I'm building it solo, and from now on I'll be writing up what changes every week or two. This first entry covers a busy few days in mid August.

## Statues that pull themselves together

Each of the six gods (Ares, Hades, Hermes, Hephaestus, Demeter and Artemis) has a statue somewhere in the world. When you first meet one, the statue is a broken pile of stone. During the reveal cinematic, thousands of fragments leap back into place and the god stands whole again.

![The broken statue of Artemis lying in pieces on a grassy hill]({{base}}/assets/img/artemis-fragments.jpg)
*Before the reveal: what's left of Artemis*

That moment looked great but cost a lot: the fragments stayed in the scene forever, even after the cinematic was long over. Now, as soon as you've seen the reveal (or when you load a save where you already have), the fragments are removed and swapped for a single, intact statue. Same view, a fraction of the cost.

## A proper entrance for the boss

The first boss, a huge bear, used to just... be there. Now, when its quest begins, the camera cuts away for a short reveal, the boss arrives, and an off-screen arrow keeps pointing at it until you find it. It's a small change, but it turns "a big enemy" into an event.

## Benches that reach into your chests

![The alchemy bench, its craft panel and the player inventory side by side]({{base}}/assets/img/alchemy-bench.jpg)
*The alchemy bench pulling from everything you own*

This is the one I'm happiest about. Before, crafting meant hauling materials from bench to bench. Now your inventory, every bench and every chest in the area act as **one shared material pool**. Click craft and the bench takes what it needs from wherever it is.

A few rules keep this honest:

- The bench's own storage is always used first.
- Finished items always land in the bench, never in a random chest.
- A craft either takes everything it needs or nothing at all. No half-spent materials.
- Any chest that gives up materials is saved right away, so nothing comes back on your next session.

## Under the hood

- A new **loading screen** with rotating artwork and gameplay tips, used for every scene change.
- Enemy skins now load on demand instead of all sitting in memory at once.
- A pass over texture sizes and build settings to trim memory and load times.
- A tool that checks and fixes the navigation setup on every enemy at once, instead of one by one.

None of that is glamorous, but it's the kind of work that keeps the game running smoothly on more machines.

Next time: settings, a safety net for when you fall off the world, and a sky that behaves.
