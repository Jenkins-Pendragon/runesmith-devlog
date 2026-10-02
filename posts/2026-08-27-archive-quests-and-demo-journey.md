---
title: Giving the demo a beginning and an ending
date: 2026-08-27
number: 8
series: archive
period: 2026-06-25 to 2026-08-27
summary: An opening quest chain, rebuilt god statues, cinematic control and a stopping point for the demo journey.
cover: statue-artemis.jpg
cover_alt: The assembled Artemis statue
stories: S0264, S0265, S0269, S0311, S0297, S0306, S0313, S0316
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: Cover captured October 1, 2026. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

Gathering, crafting and equipment can become a list of disconnected menus if the first journey does not bring them together. I built an opening quest chain around the actions the player needed to learn.

## Connecting the first tasks

The chain tracked crafting, equipping, placement, runes and encounters. Active-step progress was saved, and English and Turkish text assets supported the early quest presentation.

Claiming a reward advanced the chain. Panel and input cleanup mattered around that transition, and a completed quest could open its reward screen when other interface activity allowed it. The aim was to keep the next step connected to the reward that had just been earned.

![Artemis statue fragments before the reveal]({{base}}/assets/img/artemis-fragments.jpg)
*Artemis statue fragments before the reveal. Later-build illustration, not a screenshot from the development period. Captured October 1, 2026.*

## Rebuilding a god

Rebuilding god statues triggered narrated and subtitled sequences. Prerequisites, watched-state handling and fallbacks supported those reveals. A boss introduction coordinated character control and interface visibility, while cinematic input handling blocked gameplay shortcuts and added a held skip action for god reveals.

![The assembled Hades statue, staged for the capture]({{base}}/assets/img/statue-hades.jpg)
*The assembled Hades statue, staged for the capture. Later-build illustration, not a screenshot from the development period. Captured October 1, 2026.*

Out-of-bounds recovery also gained a fade back to safe ground and cleanup for displaced enemies. It was another place where the game needed to return control cleanly after interrupting the usual flow.

## Reaching the stopping point

The historical demo-ending screen offered Steam, Discord and exit options and kept developer commands out of that flow. The end screen has since changed substantially. Its later personal summary and full-game cards are described in [Getting ready for Next Fest]({{base}}/posts/getting-ready-for-next-fest/).

This phase gave the early systems a guided route, with introductions, rewards and a conclusion rather than only a collection of things to try.
