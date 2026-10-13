---
series: devlog
title: The runesmith finds a voice
date: 2026-10-12
number: 17
period: October 11 to 12
summary: Your character talks now, all 31 potions work, chests get a Take All button, getting hit reads at a glance, and a long list of things that used to fail without telling you why.
cover: chest-take-all.jpg
cover_alt: The player standing at a chest in the hideout with the chest window and the inventory open, a Take All button at the top of the chest window
---

The [last post]({{base}}/posts/a-codex-that-shows-you-how/) was about the Codex. The rest of those two days went into dozens of smaller things. None of them is a feature you would put on a store page, but together they change how the game feels to play.

## The character talks

Your runesmith has a voice now, a male one and a female one depending on the character you made, with 82 lines each. The lines cover three kinds of moments:

- **When something can't be done.** Your bag is full, you have no weapon summoned, the forge is still busy, you are out of rune dust or runic energy, a chest is locked, a skill is on cooldown.
- **When something goes right.** A rare forge, a high level upgrade, a level up, a long combo, several kills at once, a boss down, your first rune, a new map.
- **When it hurts.** Taking a hit, a heavy hit, and falling.

What I spent the most time on is when the character stays quiet. Only one line plays at a time, and a more important one cuts off a less important one. Nobody talks over Zeus, during cutscenes, while loading, in the pause menu or while dead. Each line has its own cooldown, and the same clip never plays twice in a row. Music and effects dip a little while a line is playing so you can hear it.

## Getting hit, at a glance

Taking damage used to look the same at full health and at death's door. Now the red edge of the screen depends on how much health you have left: faint above 75%, stronger between 25% and 75%, full below 25%. Damage over time ticks flash softer and no longer make the character grunt on every tick.

The camera shake for small hits is about half what it was, so a scratch and a heavy blow finally feel different. The health orb also shakes and glows when you are hit, and the health you lost drains away a moment later, so you can see how big the hit was.

## Every potion works

There are 31 potions and brews in the game, and until this week only two of them did anything. Now all of them work. Some heal or restore runic energy on the spot. Most give you an effect that lasts five minutes:

- **Miner's Brew:** ore and stone mining 30% faster.
- **Mule Elixir:** 500 more carry weight.
- **Scholar's Elixir:** 25% more experience.
- **Tonics and cures:** tonics give you resistance to burn, chill or poison, and cures clear them, along with bleeding.
- **Nectar of Mnemosyne:** lasts ten minutes and protects the experience you would lose when you fall.

![The inventory with the Mule Elixir tooltip open: increased carry weight capacity +500, duration 5:00]({{base}}/assets/img/potion-tooltip-mule-elixir.jpg)

Healing percentages are based on your maximum health, so a potion doesn't become useless as you level up. The effect lines in the tooltip are colored by type, in the same colors weapon tooltips use.

## Nothing fails silently

I went through every place where the game says no: interactions, crafting, equipping, placing, swimming, skills. Every one of them now gives a visible reason. Pressing the same thing ten times no longer fills the chat with ten lines; the last line just bumps.

Swimming got the most of it. You can't fight in the water, and now the game tells you so instead of just playing an error sound. Your weapon is put away when you swim; before, it stayed in your hand. A dash you pressed in the water no longer fires by itself the moment you reach the shore. The camera no longer sinks deep under the water, the jitter at the shoreline is gone, and the swimming sound no longer gets stuck in a loop if you jump back in too quickly.

## Chests

Chests have a Take All button. If your bag can't hold everything, what doesn't fit stays in the chest and you are told so, instead of spilling on the ground.

Behind that was a nasty bug. All 28 loot chests in the first area shared one inventory, so emptying one made the others vanish for good the next time you came back. Each chest has its own contents now. The chest in the arena is also no longer locked behind a quest.

## Placing and moving structures

You can now place structures up to 6 meters away. Beyond that the preview turns red and won't confirm. Something you already placed can be moved with F, contents and all, and cancelling puts it back where it was. Farm plots now use the same placement system as every other structure.

![Two placement previews of a workbench: a red one far away out of range, a green one close to the player]({{base}}/assets/img/placement-range-red-green.jpg)
*Out of range on the left, in range on the right.*

## Going home and coming back

The return spell now takes 2.5 seconds instead of 5. In the hideout the same key takes you back to the last map you were on, at the same world tier. The fall from Olympus into the first area now plays in full, and the runic energy bar no longer gets stuck at 99.

## Smaller fixes

- **Area skills.** Cone and area skills hit each enemy once. Enemies made of several colliders were taking two or three times the damage, with as many hit sounds.
- **Skills and auto attack.** Using a skill cuts into your auto attack chain right away, and the "already casting" message is gone.
- **Skeletal hounds.** They no longer jitter while chasing you; they were rerolling their attack choice every single frame.
- **Map to hideout.** Enemies from a map no longer follow you back into the hideout.
- **Camera.** It no longer clips into the terrain.
- **Gathering and the return key.** Pressing the return key in the middle of mining or chopping, then letting go, could leave the character standing idle while the work carried on.
- **Standing still.** The idle animation breathes instead of freezing.

The build with all of this is version 0.1.4.

## Next time

With the guides in place and the rough edges sanded down, the next stretch goes back into content. More on that soon.
