---
series: devlog
title: New skills, new enemies
date: 2026-10-07
number: 12
period: October 6 to 7
summary: Six skills you earn back through the gods' skill trees, three new kinds of enemies in the meadow, and a pass on how every hit feels and sounds.
cover: combat-echo.jpg
cover_alt: Echo of the God: the translucent ghost of Hades with his trident rising behind the player in the middle of a goblin fight
---

The [prologue]({{base}}/posts/falling-from-olympus/) ends with Zeus taking your power away. This post is about getting some of it back, and about the things in the meadow that would rather you didn't.

## Skills you earn back

There are six new skills, one or two per god:

- **War Cry** (Ares): nearby enemies are knocked back and start bleeding, and for 15 seconds you get +20% attack and +15% attack speed.
- **Crimson Arc** (Ares): a crimson sword wave that travels about ten meters, pierces every enemy in its path and makes them bleed. It follows the ground and stops at walls and rocks, so you can't hit things through a cliff.
- **Tartarus Rift** (Hades): the ground tears open in front of you in three quick strikes, and the last one chills.
- **Talaria Dash** (Hermes): a dash on winged sandals that damages everything you pass through.
- **Earth's Embrace** (Demeter): a ring of thorns poisons nearby enemies, and for 12 seconds you heal 2% of your max health every second.
- **Echo of the God**: the big one. The god you're most devoted to rises behind you as a ghost and strikes the ground. On the cover it's Hades, trident and all.

![Tartarus Rift: purple crystals bursting out of the ground around the player next to a goblin]({{base}}/assets/img/combat-tartarus.jpg)
*Tartarus Rift*

![War Cry: a red shockwave bursting around the player as goblins are knocked back]({{base}}/assets/img/combat-warcry.jpg)
*War Cry*

War Cry and Earth's Embrace are auras, and only one aura can be active at a time. The active one shows up as a badge in the top right corner. I also redid how they look while they last: War Cry's aura used to be a big swirl of blood around your feet, and now it's a thin red ring on the ground with a slow pulse. You can still see the enemies you're trying to hit.

![Earth's Embrace: green leaves swirling in a ring around the player while goblins close in]({{base}}/assets/img/combat-earths.jpg)
*Earth's Embrace*


To make room for these, the runic energy bar now goes up to 100 instead of 50, and refills twice as fast, so it still takes the same time to fill. Echo of the God costs the whole bar.

### Only from the tree

Skills now come from one place: the skill trees. Hades, Hermes and Demeter each have their skill on the first node of their tree. Crimson Arc sits deeper in Ares' tree, and Echo of the God is there too, locked until his statue awakens. Locked nodes tell you why they're locked and what opens them.

There's also a new Legendary rune for Ares, **Trial of Ares**. It carries Berserk Oath: below 40% health you get bonus attack and attack speed, and fire wraps around you so you know it's active.

## New enemies

The meadow got crowded:

- **Goblins** live in camps, three of them spread across the first area. Your first fight is clearing one and opening its chest.
- **Skeletal hounds** hunt in packs. They're fast and fragile, and they can leap up ledges to reach you, so standing on a rock no longer makes you safe.
- **The Cyclops** keeps to itself, far from the camps. It's slow, and before its big blows a circle appears on the ground. Get out of the circle.

![A Cyclops on a beach raising its arm for a crushing blow while a red circle fills on the sand under the player]({{base}}/assets/img/combat-cyclops.jpg)

The ground circle works for the big bear boss too, the Lord of the Wild. He also roars a lot less now: only below half health, only when you back away, and never more than once every 12 seconds. Before, he roared eleven times a minute.

When an enemy dies, its loot flies straight to you and the body dissolves, so you don't have to walk over and pick things up in the middle of a fight.

### A new look for the creatures

All the creatures moved to a new shading setup: soft shadows, a light rim around the edges, and brighter colors in shade. It's the same stylized look as the rest of the world, and creatures stay readable when they walk into shadow.

![A lineup of creatures on a beach: a goblin, the Cyclops, a skeletal hound and two bears, all with soft shading and rim light]({{base}}/assets/img/combat-creatures.jpg)
*The creature lineup with the new shading*

## How hits feel

I went through the feedback for every kind of hit:

- **Hitstop** now freezes both sides for a split second, you and the enemy, so the impact reads as a real contact.
- **Critical hits** get a tiny slowdown and a small camera pulse. Kills get a slightly bigger one. Normal hits get neither, so the special ones stand out.
- **Crowds** have a budget. When a lot of enemies are getting hit at once, the effects scale down instead of flooding the screen.
- **Resisted** now appears over enemies that shrug off a status effect, so you know the bleed or chill didn't land.
- **Two new settings** in the Game tab: Screen Shake and Reduce Flashing. Reduce Flashing turns off the camera pulse and softens flashes across the game.

## Sound

Most of what's above now makes noise: sword impacts, critical hits, all five active skills, both auras, Shatter, blocks and dodges, and a special sound when you forge something Legendary. The game also got eight new music tracks, including one that plays while you're doing the Trial of Ares.

## Tools

To check over two hundred sounds without hunting for them in the game, I built a Sound Tour window in the editor. It lists every sound with a play button, lets me leave a note and mark it "keep" or "change", and puts the risky ones at the top.

## What's next

You have the skills and something to use them on. The next post is about why you're out there at all: the new quest line, and the first god who answers you.

*Screenshots captured October 7 on a development build.*
