---
series: devlog
title: Runes that keep their promises
date: 2026-10-04
number: 7
period: October 2 to 4
summary: Thirty-four rune stats used to show up on your runes and then do nothing at all. This week every one of them got wired into the game, and Shatter, the strangest of them, got a look of its own.
cover: rune-shatter-veins.jpg
cover_alt: An iron ore node with glowing golden veins running across its surface
commits: af3eba3340..8823918aec
---

Here's an uncomfortable confession. A rune in The Runesmith rolls a handful of stats from its god's pool, and a good number of those stats were only text. They appeared in the tooltip, they counted toward the rune's value, and then no part of the game ever read them. You could forge a rune with "chance for refined ore on hit" and mine for an hour without seeing a single ingot.

That's fixed. I went through every stat that had nothing behind it, 34 of them, and made each one actually happen. The starter runes from my last post were already limited to stats that worked. Now the rest of the pool does too.

## Shatter

Shatter is the stat I'm proudest of, and the one that took the most iterations.

The rule: a Shatter hit can only land once the resource is below 30% of its health. When it lands, it breaks off everything that's left in one go, and that last chunk drops **double** loot. The catch is that the roll happens earlier. If your rune's Shatter chance procs while the node is still healthy, the node gets **bound**. From then on it's a promise: the moment its health dips under 30%, it shatters, no second roll.

A promise needs to be visible, so a bound resource now carries veins of light in your god's color across its whole surface. They spread out from where you hit it, and as its health drops toward the threshold they grow brighter and pulse faster.

![The same iron ore with bright, dense golden veins covering almost the whole rock]({{base}}/assets/img/rune-shatter-threshold.jpg)
*Close to the threshold, the veins nearly take over the rock*

The first version did this with an outline and a spinning icon above the resource. On a tree the icon floated 23 meters up, out of frame, and the outline traced every jagged edge of the leaf cards. So the mark moved onto the object itself, and on trees it only draws on the trunk.

![A tree trunk covered in bright blue veins]({{base}}/assets/img/rune-shatter-tree.jpg)
*Hermes blue on a tree trunk (captured October 4)*

Health bars got a matching hint: a small break line at the 30% mark with the god's sigil under it, so you know exactly where the payoff is.

The shatter itself is a short, sharp moment: a 120 ms freeze, a ring and burst in the god's color, the loot flying from the node to you, and a "Shatter +N" count. A faint silhouette of the god's statue rises behind the node. I tried a longer slow motion first, but Shatter can happen every few nodes, and a long pause broke the rhythm of gathering.

![The shatter moment: a golden ring around the ore, sparks, a faint statue silhouette rising behind it and the Shatter +14 text fading in]({{base}}/assets/img/rune-shatter-moment.jpg)
*A few frames into a Hephaestus shatter*

## Gathering

The rest of the gathering stats are simpler, and each one now does what it says:

- **Rune Dust** (the material for forging and upgrading runes) can drop on any gathering hit from Hephaestus, or more generously from ore with Hades.
- **Refined drops**: a chance to get the processed version straight from the node, like an ingot from iron ore or processed leather while skinning.
- **Potions and food**: herbs and mushrooms can drop a random potion, and harvesting a corpse can drop a ready meal.
- **Clean Cut**: critical hits on a corpse give Rune Dust.
- **Harvest Echo** (Demeter): the final pick of a plant can drop its loot twice.
- **Ares** gets blood and meat the moment you kill something, without having to harvest the corpse.
- **Sonar** can knock a stone loose when its pulse hits rock.
- Skinning and butchering can **speed up** the longer you keep going without a break.

Bonus loot is rolled once per hit, not once per item. A single hit can produce dozens of drops, and rolling for each one would have made a 5% stat close to guaranteed.

## Crafting

Hephaestus's crafting stats work at the bench now:

- **Instant Craft** skips the wait for a crafting step.
- **Double Craft** gives you the step's output twice.
- **Automated Smelter** triples the output when refining in the furnace.
- **Fail Protection** gives your materials back when a chance-based craft fails, keeps the orb when an orb roll fails, and covers rune upgrades too.
- **Successful Craft** raises success chances in proportion. A 10% craft with a +20% stat becomes 12%, not 30%. Adding it flat would have made the rarest upgrades trivially easy.
- **Bench speed** shortens crafting time.

They also apply to the crafting that happens while you're away from the bench, so returning to a full queue pays out the same as watching it.

## Combat

Two defensive stats now work the way Path of Exile players will recognize:

- **Evasion** makes an attack miss completely. It isn't a dice roll each time. Every hit fills a hidden counter by your evasion value, and when it passes 100 you dodge. At 30% you dodge exactly 3 hits out of 10, so there are no lucky or unlucky streaks. A dodged hit also can't poison or burn you.
- **Block** is a real dice roll, capped at 75%. A blocked melee attacker staggers and gets pushed back.

Same result, no damage, but they feel different on purpose: one you can count on, one that occasionally hits back.

And one Hermes stat, **lighter load**, now reduces the slowdown from a heavy bag. Four Artemis stats tied to ammo and marks were taken out of the pool for now.

## Smaller fixes

- The Shatter descriptions were rewritten in all 33 languages to match how it actually works.
- Stats on the rune page now show as percentages or flat bonuses, whichever they are, instead of bare numbers.

## Tools

For testing I added a set of test runes to my rune generator: 34 of them, each carrying a single stat at a fixed value, so I can equip one and see its effect immediately instead of hoping for a lucky roll.

## Next time

With runes doing what they say, the next post is about making all of it, and combat in general, feel better in your hands.

*Cover and shatter images captured October 5 on a development build.*
