---
title: From workshop output to a loadout
date: 2026-09-22
number: 12
series: archive
period: 2026-03-09 to 2026-09-22
summary: Divine weapons, equipment, skill choices and progression across gathering, crafting and combat.
cover: archive-engineer.jpg
cover_alt: Three engineering workbench variants
stories: S0169, S0170, S0172, S0175, S0177, S0211, S0212, S0173, S0174, S0176, S0178, S0180, S0182, S0183, S0188, S0190, S0194, S0201, S0204, S0203, S0230, S0236, S0241, S0242, S0246, S0287, S0293, S0323
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: Cover captured October 2, 2026. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

The output of a workshop needed to connect to the character. I worked on equipment, summoned weapons and progression so crafting choices could carry into exploration and encounters.

## Moving with a weapon

Dashing and swimming gained controls and animations, with dash effects and a radial cooldown display. Camera zoom let the player adjust distance. Divine weapons gained summoning, swapping and dissolve presentation, with locomotion following the weapon family.

Casting applied movement and cancellation rules. Swimming dismissed a summoned weapon and prevented another summon until the player left that state. A radial submenu handled manual summoning during part of this development period; later, holding Tab opened weapon selection and swapping.

[![Engineering station variants]({{base}}/assets/img/archive-engineer.jpg)]({{base}}/assets/img/archive-engineer.jpg)
*Engineering station variants. Staged current-prefab comparison, captured October 2, 2026. Left to right: tier 1, tier 2, tier 3.*

## Learning and chaining actions

God-path skill trees spent points, displayed locked skills and applied configured cost reductions. Melee auto-attacks connected to movement and ammunition. Buffered input and cooldown displays helped carry a queued action into the next available moment.

A combo counter tracked chains and bonuses. Status effects gained resistance, intensity and stack rules, while initialization and interrupted visual-state fixes protected skill and weapon transitions.

## Equipment and longer-term progress

Equipment and glyphs gained crafting, upgrading, equipping and saved state, alongside boss reward bags. Life tools had to be equipped for harvesting and appeared through dissolve transitions. Weapon parts and icons broadened the catalog, with per-combo attack configuration for weapon families. These additions were not a finished balance pass.

[![Tailoring station variants]({{base}}/assets/img/archive-tailor.jpg)]({{base}}/assets/img/archive-tailor.jpg)
*Tailoring station variants. Staged current-prefab comparison, captured October 2, 2026. Left to right: tier 1, tier 2, tier 3.*

Gathering, crafting and defeating enemies awarded experience. Levels granted skill points and configured stat bonuses, with a death penalty in the progression rules. Glove visuals followed the character rig; movement bonuses responded to item-weight tags. Summoning brightened arm tattoos, and meta orbs worked on runes and glyphs.

World-tier initialization, rune multipliers and missing Artemis identities and pool entries received corrections. By the end of this period, a loadout connected workshop output to more than the damage of a single attack.
