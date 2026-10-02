---
series: devlog
stories: S0317, S0318, S0312
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
title: 66 achievements and a better pickup
date: 2026-08-31
number: 4
period: August 27 to 31
summary: The Runesmith now has 66 Steam achievements, each with its own hand-made icon and an in-game panel to track them. Picking things off the ground got an animation, and combat got a combo counter.
cover: achievements.jpg
cover_alt: A grid of round bronze and gold achievement icons showing anvils, axes, runes and skulls
commits: c33b3c7f9e..f3340f74ce
---

## 66 achievements

The game now has **66 Steam achievements**. They follow the whole journey: your first axe, your first campfire, your first rune, every kind of bench, the first boss, all six gods. Each one has its own icon in the same bronze-and-stone style, plus a greyed-out version for the ones you haven't earned yet.

A few design notes:

- **Progress counts properly.** Crafting a stack of ten counts as ten, not one, so the "craft a lot of things" achievements move at the speed you actually play.
- **Some achievements are collections.** "Use every bench" remembers which benches you've already worked at, so you can see what's left.
- **You don't need Steam open to see them.** There's an in-game achievements panel on the radial menu (**Q**) that lists everything, what you've unlocked and what's still ahead.

All of the achievement hooks live in one place, so adding a new one later doesn't mean digging through gameplay code.

## Picking things up

The very first thing you do in The Runesmith is pick up twigs and stones off the ground. It's also the action you repeat most in the early game, and it used to have no animation at all: you pressed E and the item simply vanished into your bag.

Now your character reaches down with a quick upper-body pickup. Your legs keep doing whatever they were doing, so you can grab things on the move without stopping. Small, but it changes how the first five minutes feel.

## A combo counter

Chain hits together in combat and a **"3x Combo"** counter appears above your head, popping a little with every hit. It's a single counter that updates in place rather than a stack of numbers, so it stays readable in a busy fight.

## Smaller things

- A **4K screenshot key** for capturing store and press images. It re-renders the scene at full resolution instead of upscaling, so edges and effects stay crisp.
- Sound fixes and new hooks for the pickup and the god statue moments.

Next time: The Runesmith learns a lot of new languages.
