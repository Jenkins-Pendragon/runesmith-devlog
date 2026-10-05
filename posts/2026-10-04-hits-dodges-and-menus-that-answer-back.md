---
series: devlog
title: Hits, dodges and menus that answer back
date: 2026-10-04
number: 8
period: October 4
summary: A stat you can't see working might as well not exist. This round gave dodges, blocks and bonus loot their own feedback, put motion into every menu, and fixed a camera that kept jumping at you.
cover: feel-dodge.jpg
cover_alt: The player character with a pale blue afterimage sliding off to the side and the word Dodged above it
commits: 2c4c8e5974..9a60c90baa
---

The [last post]({{base}}/posts/runes-that-keep-their-promises/) was about rune stats finally doing something. The problem with that kind of work is that a lot of it is invisible. If Evasion makes an attack miss, and nothing on screen tells you, it just looks like the enemy missed. So this round was about making the game answer back.

## Dodge and block

Both results are the same on paper, no damage taken, but I wanted them to feel opposite.

**A dodge is light.** A pale blue afterimage of your character slides off to the side and fades, with "Dodged" above you. No freeze, nothing heavy, you just weren't there.

**A block is heavy.** A shield ring flashes in the direction of the attack, metal sparks fly, and the game holds for 60 ms, like a hit landing on you that didn't get through. "Blocked" gets its own styled text, separate from the damage numbers.

![The player character with a golden shield ring and sparks on one side]({{base}}/assets/img/feel-block.jpg)
*A block, with the ring on the side the attack came from (captured October 4, before the HUD redesign)*

## Loot your runes earned

When a rune stat gives you a bonus item, you should know that it came from your rune and not from the regular drop table. So bonus drops now:

- show up in the pickup feed in your god's color, with the god's sigil and name on the line,
- fly from the resource to you as little icons,
- play their own sound.

Double and triple drops used to be silent too. The only way to notice one was to read the number in the pickup feed. Now a hit that doubles or triples its loot drops a small **x2** or **x3** stamp next to the hit, with its own sound, a little higher for a triple.

![The pickup feed with a normal Iron x2 line and an Iron Ingot line marked with an orange stripe and Hephaestus's sigil]({{base}}/assets/img/feel-bonus-drop.jpg)
*A regular drop and a bonus ingot from Hephaestus (captured October 4, before the HUD redesign)*

The skinning and butchering speed streaks from the last post got feedback too. Every hit in a streak throws a small spark in your god's color that grows as the streak builds, the sound rises in pitch, and a ring pops once when you reach full speed. Before, the only sign was the animation getting a bit faster, which was easy to miss.

## Menus that move

Up to now, every window in the game simply appeared and disappeared. Twelve of them, from the inventory and crafting benches to the skill tree, achievements and the rune pages, now open with a short fade and scale and close with a quick fade. Buttons react when you hover over or press them, and that includes buttons you select with the keyboard.

The important detail is that only the visuals are animated. The window is clickable the moment you open it and stops taking clicks the moment you close it, so the animation never sits between you and your input. Item tooltips wait a beat before appearing so they don't flicker while you sweep the mouse across the inventory, then show instantly as you move from one item to the next.

## Camera

- **Running and dashing** now widen the camera slightly, so speed reads as speed. It's tied to actually moving: holding Shift while standing still doesn't do anything.
- **The camera kept jumping toward you** around mined ore. When an ore node breaks, its pieces lie on the ground for about 12 seconds, and the camera was treating them as walls and snapping forward to avoid them. The same happened around the broken god statues, which still had the collision volume of the whole 9 meter statue. Both are now ignored by the camera, while you still can't walk through them. The camera also eases in and out of collisions now instead of snapping.

## Tools

All the combat feel values (hitstop lengths, camera pulses on crits and kills) used to be constants in code. They now live in a settings asset I can tune while the game is running, with exactly the same values as before. The menu timings got the same treatment.

## Next time

Most of these screenshots still show the old interface. That's because right after this, I started redesigning it. That's the next post.
