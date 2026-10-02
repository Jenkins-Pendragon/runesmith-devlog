---
title: A bag that supports a crafting game
date: 2026-09-07
number: 9
series: archive
period: 2025-07-20 to 2026-09-07
summary: Stacks, transfers, dropped items and controls that follow the screen you are using.
cover: alchemy-bench.jpg
cover_alt: A later crafting interface with recipes, queue and player inventory
stories: S0056, S0058, S0059, S0061, S0062, S0057, S0071, S0081, S0228, S0270, S0272, S0273, S0280, S0310
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: The original cover capture date is not recorded. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

Gathering only becomes useful if the inventory can keep up. I built the early bag around the actions a crafting game repeats: collecting, splitting, moving, using and occasionally dropping an item back into the world.

## The item actions

Slots and stacks handled storage and overflow across inventory panels. Right-click exposed use, split, drop, transfer and destroy actions. Alt-click transferred between inventories, while dragging supported splitting, stacking and swapping with a carried-item preview.

Dropped items entered the world with physics and could be collected again. Tooltip corrections helped explain what was in the bag before the player acted on it.

[![Leatherworking station variants]({{base}}/assets/img/archive-leatherworkbench.jpg)]({{base}}/assets/img/archive-leatherworkbench.jpg)
*Leatherworking station variants. Staged current-prefab comparison, captured October 2, 2026. Left to right: tier 1, tier 2, tier 3.*

The bench comparison is a later visual illustration of the stations around those inventory actions. It does not show the original inventory interface.

## Moving between controls

Controller support reached the interface as well as the character. Input maps followed the active context; gamepad focus, popup handling and device-aware icons supported inventory navigation. Interaction cleanup was revised so closing an action did not leave navigation in the wrong state.

Later shortcuts opened inventory crafting where the map allowed it, and a rune bench could open the player bag beside its page. Categories and delayed text received localized labels. Inventory and skill-tree controls distinguished pressing from dragging and releasing outside a control.

Ctrl released the mouse for panel interaction, and supported items gained quick equipping through right-click or context actions. Typing in the system-message log captured input so inventory shortcuts did not fire through the text field.

This work made the bag and its controls follow the player's current task, instead of demanding the same interaction in every screen.
