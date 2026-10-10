---
series: devlog
title: Every weapon pulls its weight
date: 2026-10-10
number: 15
period: October 7 to 10
summary: Twelve weapon families tuned to the same baseline, arrows that burn and daggers that poison, enemies that last long enough to fight, and a long list of things that used to trip you up while moving around.
cover: fight-hounds.jpg
cover_alt: A pack of skeletal hounds closing in on the player in a sunny meadow, one of them about to leap
---

The [last post]({{base}}/posts/finding-your-feet/) was about finding your way through the first hour. This one is about what happens when you get into a fight there, and about the ground under your feet.

## Twelve weapons, one baseline

Until now the sword was the only weapon I had really tuned. Now every weapon family's auto-attack combo is measured against the sword's damage per second, so picking a bow or a spear is a matter of style, not a trap.

- **Craft them early.** The Craft window has basic recipes for a quiver and arrows, fist weapons, a spear and a shield, next to the sword and tools.
- **Weapons carry status effects.** Arrows have a 30% chance to set enemies on fire, and the basic dagger has a 30% chance to poison.
- **Tooltips show it.** Weapon tooltips now list base damage and the chance and damage of each status effect.
- **Projectiles behave.** Staff and bow shots used to hit the shooter's own trigger or a random world volume. Now they only hit enemies, with a little forgiveness on the aim.

## Fights that last

With the new skills, a bear went down in about two seconds and the boss in seven. I measured how long every creature should take and set their health to match. A regular bear is a proper fight now, the Cyclops needs a plan, and the Lord of the Wild is a real boss.

- **Each species has its own resistances**, so the same status effect doesn't land equally on everything.
- **Status resistance works the same everywhere.** Before, bleeds from cones, areas and Crimson Arc skipped the resistance roll that single-target hits made.
- **Bleed doesn't stack to absurd numbers anymore**, and the sword combo's last hit was toned down to sit closer to the first two.

![The player's sword cutting a purple arc through a goblin by the lake]({{base}}/assets/img/fight-sword.jpg)

## Enemies you can find

- **Hunt markers.** When a quest sends you after something, the creatures it wants get a marker over their heads. It goes away on your first hit.
- **Goblins and skeletal hounds are bigger**, one and a half times their old size, so you can read them in a fight. Hound packs also moved out of the rocky corners and onto open meadow.
- **They stopped jittering.** Packs used to vibrate in place while trying to avoid each other. Turning and acceleration are calmer now.
- **The Cyclops lives near the Statue of Ares**, where the trial sends you.
- **Bears don't roar mid-fight.** Only the boss does. Bears, boars and deer also finally have their own sounds instead of sharing one.

## Loot

All 28 chests in the first area got their own loot tables, and so did the breakable objects around them. A chest at the boss arena only opens once its quest is active, so you can't loot the reward before the fight.

## Things that tripped you up

A lot of small movement and interaction bugs, most of them found by playing:

- **Water.** One lake's surface acted like solid ground, so you could walk on it. Swimming was jittery at the shore. Both are fixed, skills are now blocked while you swim, and Talaria Dash glides properly in the air.
- **Falling off the world.** If you leave the playable area, the screen fades and you're put back on the last safe ground you stood on.
- **Dash cancels attacks.** Holding attack used to lock you in place, so dash did nothing. Now dash interrupts the swing.
- **Steep slopes** could swallow the player into the terrain. Not anymore.
- **Gathering.** Pressing E while moving, or looking away from a node at the wrong moment, could leave your tool out with nothing happening, or stuck in a loop of animations. Gathering now starts and stops cleanly, and dead or empty nodes never pull out your tool.
- **The hideout** had 88 objects you could walk straight through. They have collision now.

## Sound

- **War Cry** now uses your character's own battle shout, with a different voice for each body type, layered with a tone for Ares. **Earth's Embrace** got an earth spell sound with a tone for Demeter.
- **Footsteps** are tied to the actual steps in the walk and run animations.
- **Crimson Arc's wave** fades out at the end of its path instead of hanging in the air.

## What's next

All of this goes into the next demo build, 0.1.3. After that, back to playing it from the start, and seeing what still gets in the way.

*Screenshots captured October 10 on a development build.*
