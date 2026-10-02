---
title: The details between the big features
date: 2026-09-07
number: 10
series: archive
period: 2026-05-26 to 2026-09-07
summary: Health feedback, settings, achievements, sound and the safeguards around scene changes and longer sessions.
cover: achievements.jpg
cover_alt: The in-game achievement list
stories: S0275, S0284, S0288, S0295, S0308, S0251, S0256, S0282, S0296, S0301, S0302, S0298, S0300, S0304, S0305, S0309, S0314, S0312, S0317, S0319, S0320
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: The original cover capture date is not recorded. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

Once the main loops existed, many of the remaining problems lived between them: a setting that did not carry into gameplay, an effect that survived a transition or a screen that did not explain the player's state.

## Reading the character's state

Changes to maximum health updated the current value and display within the new limit. Buffs showed timed effects, auras and campfire healing. Potions applied healing, incoming damage drove screen feedback and numbers, and empty vessels could collect dirty shoreline water with movement and cancellation checks. Rune crafting received a fallback hammer visual too.

![The later landscape and water; an environment illustration]({{base}}/assets/img/world-vista.jpg)
*The later landscape and water; an environment illustration. Later-build illustration, not a screenshot from the development period. Captured October 1, 2026.*

## Settings that follow the player

The main menu gained patch notes. Resolution handling accounted for the native display, aspect ratio and borderless behavior, with safer resets. Pause settings shared persisted sensitivity and inverted-look choices and managed paused time.

Character creation gained preview rotation and idle variation, with one saved source for gender selection. Camera interpolation and jump animation received further fixes. Language selection was retained with English fallback behavior, translation-table changes and font handling. A water-shader compatibility fix supported the rendering API.

## Keeping transitions clean

Input setup tolerated references becoming available after startup. Scene teardown protected enemy spawning, casts and bench queues; guards rejected stale pooled returns. Texture and build-dependency settings were revised, and a bounded log buffer prevented unlimited log growth while preserving error reporting.

Tree and shadow culling and LOD settings were configured too. This history does not include measurements that would justify an FPS claim.

## Sound and progress

A central sound library connected gameplay and interface events to the mixers, with pause and ownership handling. Account-scoped local achievements gained a catalog, list and icons. Local achievement tracking was not a claim of Steam achievement synchronization.

Later snapshots of this work are covered in [Settings, safety nets and a sky that behaves]({{base}}/posts/settings-safety-nets-and-a-sky-that-behaves/), [Giving the forge a voice]({{base}}/posts/giving-the-forge-a-voice/) and [66 achievements and a better pickup]({{base}}/posts/66-achievements-and-a-better-pickup/).
