---
title: Enemies, attacks and the feeling of a hit
date: 2026-07-24
number: 6
series: archive
period: 2025-08-25 to 2026-07-24
summary: Patrols, coordinated encounters, projectile hits and the feedback that made combat easier to read.
cover: statue-hades.jpg
cover_alt: The Hades statue and its surrounding landscape
stories: S0091, S0100, S0102, S0104, S0106, S0135, S0138, S0140, S0141, S0142, S0145, S0147, S0163, S0165, S0168, S0195, S0196, S0210, S0290, S0187, S0184, S0186, S0200, S0206, S0252, S0202, S0205, S0207, S0208, S0209, S0247, S0248, S0249
source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
---

*Image note: Cover captured October 1, 2026. The cover is a later-build illustration, not a screenshot from this development period. Current prefab comparisons below are dated individually.*

Combat developed in layers. I first needed enemies to respond to the world, then attacks to connect reliably, and finally feedback that explained what had happened.

## More than a spawn point

Enemy behavior grew through patrol, detection, roaring, pursuit and weighted attacks. Habitats managed populations and variants, including fleeing and pack assistance. Discovery sequences revealed meshes and moved the camera, with nearby enemies able to react. God-item collection also gained an early local achievement display, alongside Steam startup and overlay work.

Later, a combat director coordinated attack permission and inner and outer positioning rings. Enemy roster, scale, audio pitch and dissolve presentation added variation. Cancellation, death, corpse interaction and respawn resets received fixes, with level, rarity and configurable low-health fleeing helping define an encounter.

![An exploration landmark in the later build; this image does not demonstrate combat]({{base}}/assets/img/artemis-overlook.jpg)
*An exploration landmark in the later build; this image does not demonstrate combat. Later-build illustration, not a screenshot from the development period. Captured October 1, 2026.*

## Making attacks connect

Skills gained targeting, casting, cancellation and projectiles. Health regeneration and healing-over-time sat alongside burning, poison and bleeding. Health bars and hit numbers made those states visible.

Animation timing was connected to effects, projectile release and ammunition use. Attacks could combine distinct hit moments with cone or projectile targeting, and barrels and chests could receive skill hits. Projectile checks followed the distance traveled and prevented the same pierced target being hit repeatedly.

## Reading the impact

Trails and swing distortion described the path of an attack. Knockback, enemy status effects, hit-stop, camera shake and flashes added feedback around contact. Floating numbers distinguished normal, critical and status damage and healing. Channel attacks consumed mana until stopped; proc items applied timed weapon effects and projectile statuses.

Combo transitions and leftover weapon visuals needed cleanup too. These were the foundations, not the final timing pass. The later hit-stop changes are described in [Getting ready for Next Fest]({{base}}/posts/getting-ready-for-next-fest/).
