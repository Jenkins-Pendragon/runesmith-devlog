---
series: devlog
title: A codex that shows you how
date: 2026-10-12
number: 16
period: October 11 to 12
summary: An in-game guide library with short videos for every core system, cards that tell you when a new page opens, and a looping clip beside every skill in the tree.
cover: codex-panel-tempers.jpg
cover_alt: The Codex window open on the Weapon Tempers entry, with a video on the left and a numbered how-it-works list on the right
---

The [last post]({{base}}/posts/every-weapon-pulls-its-weight/) was about fighting well. This one is about knowing how. The Runesmith has a lot of systems stacked on top of each other: runes, tempers, benches, farming, god statues, world tiers. Until now the only way to learn most of them was to poke at them and hope. So I built a place in the game that shows you.

## The Codex

The Codex is a library of short guides that lives inside the game. It opens from a new button that sits above the bottom right corner of the HUD. There is no hotkey on purpose: it is there when you want it and quiet when you don't.

Inside, entries are split into seven tabs: Basics, Combat, Runes, Crafting, Farming, Gods and World. There are 22 entries so far. Each one has:

- a slideshow of images or a video recorded in the game,
- a numbered "how it works" list that highlights the step the slide is showing,
- a tip in the gold box at the bottom, the kind of thing you would only learn after a few hours,
- links to related entries, plus search and filters for videos or guides.

<video src="{{base}}/assets/video/codex-weapon-tempers.mp4" poster="{{base}}/assets/img/codex-weapon-tempers-poster.jpg" autoplay muted loop playsinline controls preload="metadata"></video>
*The Weapon Tempers entry's video: summon a weapon, use a temper from the hotbar, watch the blade light up.*

The tips are where I put the details that are easy to miss. Every 10 hits of combo add 10% damage, up to 50%, as long as you don't pause for 3 seconds. Falling costs you 10% of your progress toward the next level, but never the level itself. A planted farm plot can't be dismantled until you harvest it.

## Pages open as you play

The Codex doesn't hand you everything at once. An entry opens when you reach the thing it explains: a feature unlocks, a quest starts or finishes, an item lands in your bag, or you place a structure for the first time. Once a page is open it stays open.

![A "New Codex entry: Weapon Tempers" card sliding in above the Codex button in the corner of the HUD]({{base}}/assets/img/codex-new-entry-card.jpg)
*A new entry card. It waits for a quiet moment, stays for three seconds, then flies into the Codex button.*

When a new page opens, a small card slides in from the right. It waits if you are in a cutscene, loading or have a window open. After three seconds it flies into the Codex button and the badge on the button bumps. Clicking the card takes you straight to that page. To keep it from turning into a stream of popups, cards are at least 45 seconds apart, and anything that unlocks in between is bundled into a single card.

## A video beside every skill

The skill tree got the same idea. Hover over a skill and a short looping clip plays next to its tooltip, showing what the skill actually does before you spend a point on it. Eight skills have one: War Cry, Tartarus Rift, Crimson Arc, Earth's Embrace, Echo of the God, Moon Arrow, Talaria Dash and Hermes Boots.

![The Ares skill tree with the Crimson Arc tooltip open and a clip of the crimson wave cutting through goblins beside it]({{base}}/assets/img/skill-tree-video-tooltip.jpg)

The poster frame shows up instantly. The video itself starts a moment later, so sweeping the mouse across the tree doesn't start and stop a dozen videos.

## Moon Arrow, retuned

Recording those clips made a few skills look wrong on camera, and Moon Arrow was the worst. Its description said it pierces through enemies, but it stopped at the first one. It also cost almost nothing and hit far too hard.

<video src="{{base}}/assets/video/skill-moon-arrow.mp4" poster="{{base}}/assets/img/skill-moon-arrow-poster.jpg" autoplay muted loop playsinline controls preload="metadata"></video>
*Moon Arrow's new tree clip: one arrow, three goblins.*

Now it goes through up to three enemies, has a 6 second cooldown and costs 20 runic energy, the same class as Crimson Arc. Its damage dropped from 25 times your attack to 5 times. The archer also steps back when firing instead of forward. While I was there, Earth's Embrace got a fix too: its healing effect now stands upright instead of tilting with the character.

## Tools

Every Codex video and skill clip comes from the same recording tool inside the editor. It records the game frame by frame, draws a fake cursor and key prompts so you can see what is being pressed, and zooms toward the part of the screen that matters. That last part came from feedback on the first clips: on a full screen recording the interface was too small to read. Adding a new Codex page is now a matter of writing the steps and recording a take.

## Next time

The next post is a grab bag from the same few days, and it is a big one: the character starts talking, every potion finally does something, and a lot of quiet failures now tell you why.
