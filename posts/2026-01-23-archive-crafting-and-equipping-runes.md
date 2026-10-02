---
title: Crafting and equipping runes
date: 2026-01-23
number: 4
series: archive
period: 2025-12-10 to 2026-01-23
summary: The first connected flow from god paths and weighted rune crafting to upgrades, dust and saved loadouts.
cover: god-runes.jpg
cover_alt: Rune icons representing the god families
stories: S0109, S0110, S0112, S0113, S0114, S0115, S0123, S0127, S0128, S0129, S0131, S0132
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: The original cover capture date is not recorded. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

Runes needed a complete journey through the game. I began connecting the god-path screen, the crafting bench and the equipment page so a crafted rune could become part of a saved loadout.

## From a god path to a crafted rune

The early god-path screen handled selection, unlocking and saved progression, with localized descriptions. Rune crafting selected from eligible god configurations using weighted selection. Workbench level and quality influenced rarity, and the interface showed the relevant chances.

That was the rule set of this development phase. Later workshop work changed the default god-path gate for rune crafting; this archive entry does not describe every rule in the current build.

[![Blacksmith workbench variants]({{base}}/assets/img/archive-blacksmith.jpg)]({{base}}/assets/img/archive-blacksmith.jpg)
*Blacksmith workbench variants. Staged current-prefab comparison, captured October 2, 2026. Left to right: tier 1, tier 2, tier 3.*

Rune icons retained their god and rarity identity after loading a save. That small detail mattered: the inventory needed to explain what had been made even after the crafting moment was over.

## Upgrading, equipping and recycling

Rune-page sockets gained equipping, swapping, unlock costs and saved loadouts. Crafting and upgrade pages presented bench-dependent costs and rarity behavior, with blessing items used during upgrades. Tooltips showed tiers and stars and refreshed when an item changed.

[![Grinder variants]({{base}}/assets/img/archive-grinder.jpg)]({{base}}/assets/img/archive-grinder.jpg)
*Grinder variants. Staged current-prefab comparison, captured October 2, 2026. Left to right: tier 1, tier 2, tier 3.*

The grinder introduced a route from skulls to dust, while mineral, fossil, crop and tree content expanded the surrounding resource library. Production, upgrades and equipment were becoming parts of the same item flow.

The later forging presentation is covered in [Getting ready for Next Fest]({{base}}/posts/getting-ready-for-next-fest/). This entry records the earlier systems that presentation grew from.
