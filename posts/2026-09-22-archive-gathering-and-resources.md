---
title: Turning the landscape into materials
date: 2026-09-22
number: 11
series: archive
period: 2025-07-06 to 2026-09-22
summary: Mining, harvesting, scanning and the item safeguards that connected a gathering action to a saved reward.
cover: archive-ore-studies.jpg
cover_alt: Iron, coal and tin resource model examples
stories: S0041, S0043, S0049, S0099, S0086, S0092, S0095, S0096, S0103, S0121, S0227, S0233, S0234, S0238, S0239, S0240, S0243, S0257, S0258, S0215, S0253, S0276, S0277, S0303, S0315, S0318, S0324
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: Cover captured October 2, 2026. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

The first mining nodes turned scenery into something the player could act on. Drops, respawns, resource sounds and hit particles connected the swing of a tool to a material in the bag.

## Making the action readable

Prompts, highlights, held interaction progress and cancellation supported gathering. Tool animations, scanning emission and cursor handling kept the action and the interface in agreement.

Pickup icons and quantities animated into view. Ore definitions gained names and descriptions, while rarity colors, localized information and modifier details improved tooltips. Item-data corrections restored ore identities, rune dust and harvesting modifiers.

[![Iron, coal and tin prefab examples]({{base}}/assets/img/archive-ore-studies.jpg)]({{base}}/assets/img/archive-ore-studies.jpg)
*Iron, coal and tin prefab examples. Staged current-prefab illustration, captured October 2, 2026. Models are enlarged and arranged for illustration.*

Iron, coal and tin have visibly different shapes and colors in these current model examples. I enlarged and arranged them for this illustration; this is not their natural spawn layout or an exact world-scale comparison.

## Different materials, different actions

Woodcutting and corpse gathering shared a clearer tool presentation, with tool-specific rare drops. Plants could supply fiber; branches and stones could be picked up directly. Tool variants were consolidated while preserving resource-specific modifiers.

Tree-sap extraction gained its own tool visuals, trees showed cooldowns, and scanning gained range, cooldown feedback and a wave. Swimming gained splashes and ripples. Targeting began from the head, and kneeling farm harvests dismissed the weapon for the action.

[![Woodworking station variants]({{base}}/assets/img/archive-woodworkbench.jpg)]({{base}}/assets/img/archive-woodworkbench.jpg)
*Woodworking station variants. Staged current-prefab comparison, captured October 2, 2026. Left to right: tier 1, tier 2, tier 3.*

## Protecting the result

Harvesting checked the required life tool. Mining could provide secondary stone drops, while damage or weapon changes interrupted gathering safely. Ground pickups gained upper-body animation and sound, and combo feedback used a single number.

Inventory loading preserved unresolved item data rather than replacing a save with a partial result. Item-identity fixes addressed transfer duplication and recipe matching; empty quest rewards were handled safely. High-output gathering batched notifications and save writes while retaining individual loot rolls.

The work joined feedback to reliability: the action needed to read clearly, and the reward needed to remain the reward that had actually been earned.
