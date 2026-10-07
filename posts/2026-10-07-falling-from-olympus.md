---
series: devlog
title: Falling from Olympus
date: 2026-10-07
number: 11
period: October 6 to 7
summary: Every new realm now begins on Olympus, in a short playable fight against Zeus. You start as a god with all your power, and he takes it back.
cover: prologue-zeus.jpg
cover_alt: Zeus walking through a broken stone arch on Olympus with lightning crackling around him and glowing sigil pillars on either side
---

The Runesmith is about a god who lost everything and has to forge their power back, rune by rune. Until now the game skipped the part where you lose it. You woke up already fallen, and a short cinematic told you what happened.

Now you play it. Every new realm starts with a prologue on Olympus: about a minute and a half, ending with a fall you can't stop.

## A lazy afternoon on Olympus

You start on a daybed with a bowl of grapes while three angels fan you. Then the sky cracks, the angels look up, and Zeus lands in front of you.

> "Idling again. When will you ever shoulder your duties?"

That's the whole setup. He's not angry yet. He's disappointed, which is worse.

## The arena

The fight takes place on a broken island floating above a sea of clouds. Six pillars stand around the edge, one for each god whose path you can walk later, each topped with a glowing sigil in that god's color. A golden glyph with the six gods' marks is set into the floor, and the sun sits behind Zeus, so he's always lit from behind.

![The player getting up from the daybed to face Zeus, with glowing sigil pillars and a broken arch behind him]({{base}}/assets/img/prologue-arena.jpg)

## Learning to fight in a minute and a half

You start the fight with a Legendary sword, four skills and a full bar of runic energy. That's too much to hand a new player at once, so the skill slots start locked and open one at a time, right when the fight needs that skill. The first time, it tells you which key to press. After that, it trusts you.

Zeus fights in three phases, and along the way the fight asks three things of you:

- **The circle duel.** Zeus circles you and sends three sword waves, one after another. "Eyes on me." "Don't blink." "Once more." Time slows as each wave arrives, a key cap appears with a countdown ring, and pressing E at the right moment knocks the wave up into the sky.
- **Blade locks.** Twice he closes in for a heavy blow. Get the timing right and your swords lock with a "Perfect". The second time, the right answer is to dodge.
- **Echo of the God.** When your energy is full, the game tells you to let it out. Every god you'll ever serve rises behind you at once, and the ground breaks.

![Zeus circling the player on the arena floor during the duel, with the subtitle "Eyes on me."]({{base}}/assets/img/prologue-duel.jpg)
*The circle duel*

![The player's sword locked against Zeus' blade, with a small gold "Perfect" above them]({{base}}/assets/img/prologue-qte.jpg)

![Six translucent god figures rising behind the player in their own colors while Zeus braces in front of them]({{base}}/assets/img/prologue-echo.jpg)

> "All six at once? So that's how it is."

## What I gave, I take back

You don't win this fight. Zeus pulls the power out of you, and for four seconds you can't do anything. There's one last blade lock, and this time it breaks. Then a blow you can't avoid, a kick off the edge of the island, and seven seconds of falling through the clouds.

> "Since you won't value what you were given... then dig for it with your own hands."

You land in a white flash, on the meadow where the actual game begins, and the title card reads "The Land of the First Gods". Of the three lights that fell with you, one comes down at the start of a lit path. That's where your first quest starts.

![The player falling through the clouds below Olympus]({{base}}/assets/img/prologue-fall.jpg)

## Details that took the longest

- **Zeus speaks.** All his lines are voiced, along with roars, grunts and a choir for the Echo. While he talks, the music and effects duck so you can hear him.
- **Subtitles and prompts** got their own style for cinematic moments: two lines above the hotbar with the speaker's name in gold. Key prompts show a key cap with a countdown around its edge. It bursts gold when you hit it and cracks gray when you miss.
- **The camera** cuts to about a dozen hand-placed shots during the cinematic beats, and comes back behind you for the fighting. A lot of the work was making sure Zeus never ends up filling the screen, and that no pillar ever sits between you and the camera.
- **The arena itself** got a full art pass: backlighting from the sun, soft shadows, a bit of haze on the horizon, and a cloud sea with its own shader so it drifts and darkens away from the sun.

## Skipping it

The prologue plays once per realm. From your second realm on, you can hold E to skip it, and the Realms panel has a "Skip prologue" switch. Nothing you have in the prologue carries over. The sword, the skills and the full energy bar all stay on Olympus. You fall with nothing, and that's the point.

## What's next

The fall is in place. The next post covers what you find when you land: new skills to earn back, the enemies waiting in the meadow, and the first god who'll answer you.

*Screenshots captured October 7 on a development build.*
