---
series: devlog
title: A new look for the interface
date: 2026-10-05
number: 9
period: October 4 to 5
summary: The gothic frames are gone. The HUD, health bars, inventory, tooltips and equipment panel all moved to a new, calmer style I've been calling Night Sky, built to a design mockup down to the pixel.
cover: ui-equipment.jpg
cover_alt: The equipment panel and the inventory side by side in the new dark navy style, with category tabs and a Sort button
commits: 734dbd92ce..94c1471b14
---

The old interface had grown in layers. A gothic bar with a skull at the bottom of the screen, a cartoon ribbon for quests, lavender headings, and every new window styled a little differently from the one before. Each piece was fine on its own. Together they were noisy, and they didn't look like one game.

So I stopped and designed it properly. First a mockup of the whole HUD and the main panels, then a style sheet, and only then the actual work in the game, matched against the mockup at its real pixel size.

## Night Sky

The direction is simple:

- **Flat, dark navy panels** instead of ornate frames.
- **One accent color, gold**, for whatever is selected, active or important.
- **A single heading font, Tilt Warp**, for titles and every number in the game.
- **The nebula look is saved for two places**: the health and energy orbs, and the rune pages, where the gods live.

Tilt Warp doesn't cover every alphabet, so headings in 13 of the 33 languages fall back to Noto. Numbers use Tilt Warp everywhere, so a damage number or a stack count looks the same in Japanese as in English. Even the XP percentage follows the language: 100.0% in English, %100.0 in Turkish.

## The HUD

![The new HUD: quest card in the top left, pickup feed on the left, orbs and a slim hotbar at the bottom, round ability buttons on the right]({{base}}/assets/img/ui-hud.jpg)
*The new HUD. This is my development save, which is why I'm level 99 with 600 health.*

Everything on the main screen was rebuilt:

- **The hotbar** is a slim row of nine slots with the XP bar under it, level on the left and percentage on the right. Slots show the rarity of what's in them.
- **The ability buttons** are round, with line icons and the key above each one. While an ability is on cooldown, the button fills up from the bottom and shows the seconds left.
- **The quest card** shows the quest title, each step with a status mark and a counter, and a gold progress bar. It collapses into a single line in place instead of disappearing.
- **The pickup feed** has the item name on the left and the count on the right, and bonus drops from your runes get a frame in your god's color.
- **The interaction hint** lost its panel and is just the key and the action now.

![Four round ability buttons, first with Dash highlighted, then with cooldown fills and seconds remaining]({{base}}/assets/img/ui-abilities.jpg)
*Ready and on cooldown*

## Health bars

Resource and boss health bars moved to the same style: a thin dark frame, level on the left, health on the right. The Shatter break line from the [rune post]({{base}}/posts/runes-that-keep-their-promises/) sits on the new bar too.

![Two health bars, one with a purple Shatter section and a break line, one plain red]({{base}}/assets/img/ui-health-bars.jpg)
*A bar with the Shatter break line, and one without*

## Inventory

This one changed the most. Here's where it started:

![The old inventory: a framed panel with two tabs, a plain grid and slot count and weight at the bottom]({{base}}/assets/img/ui-inventory-before.jpg)
*The old inventory, next to the old Alchemy Bench and Craft windows (September 12)*

And here's where it is now:

![The new inventory: a dark navy panel with All, Materials, Gear, Runes, Consumables and Benches tabs and a Sort button]({{base}}/assets/img/ui-inventory-after.jpg)
*The new inventory*

The inventory got two features along with the new look:

- **Category tabs**: All, Materials, Gear, Runes, Consumables and Benches. A tab shows only that kind of item, packed together, with empty and locked slots hidden. It's only a view: your slots stay exactly where they are.
- **Sort** puts everything in order and merges partial stacks.

I also decided against darkening the whole screen when the inventory is open. You're usually looking at the world and your bag at the same time.

## Tooltips

Tooltips now have a header in the item's rarity color and stat lines in two columns, the stat on the left and the value on the right, so a rune's numbers line up and are easy to compare.

![Four tooltips: a Normal stone, an Epic brew, a Rare Hades rune with three stat lines, and a Superior jerky]({{base}}/assets/img/ui-tooltips.jpg)

## Equipment

The equipment panel is now a proper companion to the inventory, with **Combat** and **Life** tabs for weapons and tools. Weapons that come in sets lay themselves out by family: two daggers side by side, or bow, quiver and arrow in a row. The panel opens from a button in the inventory header, and a strip of control hints sits under it.

## Tools

To make the switch, I built a small editor tool that applies the new kit to the existing interface: sprites, fonts, sizes and positions, all from one place. That meant I could change a measurement once and rerun it, instead of nudging dozens of objects by hand. It also caught a sneaky problem: the game renders in linear color space, which made the dark semi-transparent panels come out noticeably lighter than in the mockup. The tool compensates for that now.

## What's next

The crafting benches and the Craft window are next. They're still in the old style, as you can see in the before shot. After that, the whole interface will finally look like one game.

*Interface screenshots captured October 4 and 5 on a development build.*
