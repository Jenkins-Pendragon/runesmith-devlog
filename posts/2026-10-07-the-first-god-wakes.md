---
series: devlog
title: The first god wakes
date: 2026-10-07
number: 13
period: October 6 to 7
summary: A new quest line from the meadow to the Statue of Ares, a god you wake with offerings and a trial, and a Shatter that fires as often as it should.
cover: gods-ares-awakens.jpg
cover_alt: The Statue of Ares glowing red through its cracks, with three lit braziers at its feet
---

After the [fall]({{base}}/posts/falling-from-olympus/) and the [new fights]({{base}}/posts/new-skills-new-enemies/), this post is about the thread that ties the first hours together: what you do in the meadow, and why.

## A quest line with a destination

The demo's quests used to be a list of chores in the right order. Now they're a chain of 21 quests that goes somewhere. Roughly:

1. **Echo of Power**: set your first rune and feel it work while you gather.
2. **Your First Point**: spend your first skill point and put the skill on your hotbar.
3. **Tools of the Forge** and your first sword.
4. **First Blood**: clear a goblin camp and open its chest.
5. **Birth of the Runes**: light the dormant forge in your hideout and strike your first rune.
6. **Fate's Anvil**: push a rune to +3. The first two strikes always hold. The third is up to fate.
7. **The War God's Altar**: follow a trail of red light to a broken statue of Ares and bring him three bear hides.
8. **Bones of the Hound** and **The Cyclops' Eye**, the two new hunts.
9. **Trial of Ares**: clear the camp he points you to.
10. The bear boss, the Lord of the Wild, and then **The Statue Awakens**.

Benches, the campfire and the furnace still fit in between, where you need them.

The first rune you forge for each god is guaranteed to be Epic. Your first forge should feel like a reward, not a coin flip.

## The Statue of Ares

In the [last post]({{base}}/posts/every-window-one-game/) I turned off praying at the statues until the god screen was redesigned. The Statue of Ares is back, and now it's a place you return to over the whole quest line.

Three braziers stand in front of it: one for your offering, one for his trial and one for his awakening. Each one you light makes the cracks in the stone glow brighter.

![Four stages of the Statue of Ares: dark and silent, glowing faintly after the offering, brighter after the trial, and fully lit when it awakens]({{base}}/assets/img/gods-ares-stages.jpg)
*Silent, offered to, tested, awake*

> "The war god's stone remembers blood and iron."

Your offering already opens Ares' path at the forge. When the statue finally awakens, the camera turns to it, the stone flares, and the last node of his skill tree, Echo of the God, unlocks.

While the statue has something for you to do, a trail of red light runs from wherever you are to the statue, so you never have to guess where it is.

![A thin red trail of light running across the meadow ahead of the player toward the statue]({{base}}/assets/img/gods-trail.jpg)

## Choosing a god

At the start you choose one god's gift, a rune and a tool in one package, from Hades, Hermes or Demeter. That god's path is open at the forge from the beginning.

![The Awakening of the Gods reward panel with three choices: Gift of Hades, Gift of Hermes and Gift of Demeter]({{base}}/assets/img/gods-gift.jpg)

The god path screen at the forge shows the rest: Ares opens with an offering at his statue, and the other gods are locked, each telling you how it will awaken. Once you have more than one path open, there's a Mixed option that forges runes from all of them.

There's also a new currency, **Divine Ember**, earned through offerings and trials. For now you just collect it. The gods will ask for it later.

## Shatter, take two

Shatter breaks a resource open and gives you everything left in it, with a bonus. It was firing far less than its numbers promised. The old rule was "after a hit, the resource has to be alive and under 30% health." With a strong rune, an ore would go 6 → 3 → 0 health and never live under 30%. One test run had 44 hits and zero Shatters.

Now Shatter triggers when a hit crosses the line, even if that hit takes the resource straight to zero. The chance also no longer depends on how hard you hit. It's spread over the health above the line, so a tree that takes six weak hits and an ore that takes two strong ones end up with the same odds.

![An ore node veined with Hades' purple, with the Shatter seal on its health bar]({{base}}/assets/img/gods-shatter.jpg)
*An ore bound to Shatter, in Hades' color*

The look changed too. A resource that's going to Shatter gets a seal on its health bar and a frame in the god's color that pulses. The god's figure that appears when it breaks is now player-sized and steps to the side instead of standing in front of you. Bonus drops fly to you in the god's color, and the sound gets brighter for purer materials. Hit fast enough in a row and your impact sound rises in pitch while your blade trail turns your god's color.

## Economy

- **The Grinder** now turns three Normal raw materials into one Rune Dust instead of one to one. Leftovers are saved, so nothing is lost.
- **Bench upgrades** got their own costs per bench. Tier 2 asks for something from the new creatures, like goblin ears or bones. Tier 3 costs about double and wants a Cyclops eye.
- **Old saves** are upgraded automatically. Your realm is backed up first, and if anything goes wrong, the game keeps the previous version and tells you.

## Tools

Most of the numbers above came from a new Economy Session Simulator in the editor. It plays 500 simulated sessions for three kinds of players and shows when each one gets their first Rare, Epic and Legendary rune, with the Grinder at one to one or three to one. It can also lay my own recorded playtests over the curves, so I can see where real play and the model disagree.


## What's next

The first god is awake. Next I want to get this whole stretch, from Olympus to the awakened statue, in front of players and see where they get lost.

*Screenshots captured October 6 and 7 on a development build.*
