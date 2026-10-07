---
series: devlog
title: Every window, one game
date: 2026-10-06
number: 10
period: October 5 to 6
summary: The Night Sky style now covers the whole game, from the crafting benches to the main menu. Along the way the game picked up save slots called Realms, a cursor size setting and a handful of fixes.
cover: ui-craft-window.jpg
cover_alt: The Craft window between the recipe list and the inventory, with Wood and Stone rows in green and a missing Iron row in red
commits: 5524f037e0..35b713c308
---

At the end of the [last post]({{base}}/posts/a-new-look-for-the-interface/) the HUD, inventory and tooltips had the new Night Sky look, and the crafting benches were still in the old gothic style. That's done now. So is every other window I could find, which turned out to be a lot more than the benches.

<video src="{{base}}/assets/video/ui-tour.mp4" poster="{{base}}/assets/img/ui-tour-poster.jpg" autoplay muted loop playsinline controls preload="metadata" aria-label="A quick tour of the new interface: the Craft window, the Hades rune page, achievements, settings and the pause menu"></video>

*A quick tour: crafting, a rune page, achievements, settings and the pause menu (sped up slightly)*

## Crafting

All eleven benches and the Craft window you open from your bag now share one panel:

- **On the left**, the bench itself: its name, its tier, an Upgrade button, the recipe grid and the bench's own storage. Recipes from higher tiers are listed too, faded and locked, so you can see what an upgrade gets you.
- **In the middle**, the Craft panel: the selected recipe, one row per ingredient with what you have and what you need, an amount box with Max, and a gold Craft button.
- **If you're short of something**, that row turns red and a line under the button tells you exactly what's missing and how many.
- **The queue** sits at the bottom. The job that's running gets a wide row with its progress, the ones waiting get small slots.

Scrolling works better too. The mouse wheel and dragging used to work only in the gaps between slots, because the slots swallowed the input. Now you can scroll from anywhere in the list, one row per tick, and the top row of the Craft list no longer gets clipped.

The Grinder got its own version: a hopper ring with twelve places around the grinder, and a Grind panel that lists what goes in and how much Rune Dust comes out. While something is grinding, a Refund button sits next to Grind.

![The Grinder: a ring of items around the grinder icon, and a Grind panel listing five inputs and +53 Rune Dust]({{base}}/assets/img/ui-grinder.jpg)

## The rune pages and the forge

The rune page for each god now has the god's title above the heading (Goddess of the Hunt, God of Travelers and so on), an 8 by 6 grid of sockets, and a list of your total bonuses from every socketed rune across all six paths. Unlocking a socket opens a small window with the cost in the same "have / need" format as crafting.

I also fixed a band that cut through the page title. The nebula background was being tiled, and one seam ran right across the heading. It's a single image now that covers the whole screen.

The Rune Furnace, where runes are made, got sub tabs, an upgrade counter for the bench and a proper empty state for Enhance when there's nothing to enhance.

## In the world

- **Farming.** The Plant menu sorts seeds into category boxes and shows how many of each you own. The Growth menu fits on one screen. The little panel above each farm plot got the new look as well.
- **The action wheel.** Things you can interact with in more than one way (like a carcass you can flay or butcher) show a wheel with dots for each option. If you're missing the tool for an action, its node turns red with a lock and a note like "Skinning Knife not equipped", before you press anything. Objects with only one action, like stone, hide the Next hint.

![Six states of the action wheel: Flay, Butcher, Gather Wood, Collect Stone, a red Flay with "Skinning Knife not equipped", and Flay again]({{base}}/assets/img/ui-action-wheel.jpg)

- **Key caps.** Every control hint in the game now shows the key as a light key cap with the letter on it: inventory shortcuts, farming, placing props, menus.
- **No more one second wait.** Control hints used to sit empty for a full second when they first appeared, because of a fixed delay in the code. Now they only wait until the player is ready.
- **A cleaner screen while you work.** When a bench, chest, rune page or the skill tree is open, the quest card and the bottom HUD step aside. They used to peek out from behind the panels.
- **Smaller pieces.** Item labels on the ground, the "not enough" popup, the region name banner, buff badges (now in the top right), the loot chest window, the wood harvesting timer, chapter titles and cutscene text all moved to the new style.

## Travel

![The World Access panel: map cards for Grasslands, Desert, Jungle and Swamp, a World Tier 2 to 3 bar with its costs, and a list of available resources]({{base}}/assets/img/ui-world-access.jpg)

The World Access panel was rebuilt. Map cards run along the top, with the tier you'll travel at on the selected card. Locked maps tell you which World Tier opens them. The World Tier upgrade moved to a strip at the bottom with a progress bar and its costs, and the resource list on the right now runs the full height. It counts how many of the world's resources your current World Tier gives you access to, and colors each row by whether it's already open, opens with the next map, or is still locked.

## Windows and menus

The rest of the game's windows went through the same treatment:

- **Quests.** The quest detail window shows rewards in cells with the amount in the corner. Optional rewards get a gold frame and a tick when you choose them.
- **Chests.** A chest opens to the left of your inventory with the same slots and grid. The speed up confirmation now shows what it costs against what you have. If you can't afford it, the frame turns red and Confirm is disabled. Before, you could press it and the window just closed without doing anything.
- **The skill tree** has tabs per god, a skill point badge and node shapes by type: squares for skills, circles for passives, diamonds for upgrades. Locked, available and unlocked nodes each look different, and the info box shows cost and requirements. The trees themselves are still being written, so for now each path says so.
- **Choosing a god's path** is a row of six cards. The one you hover lifts and gets a frame. Paths you've already opened are marked with a tick.
- **Achievements** have a summary badge, a total progress bar, and rows with a tick, a counter with a ring, or a lock. Achievements you've made progress on no longer look faded.
- **The quick menu wheel** and the **weapon strip** got the same look: gold for selected, faded for locked.
- **Small windows**: the right click menu (Destroy is in a warning color) and the split stack window with a slider.
- **Pause, Settings and the demo end screen.** Settings sliders show their value next to them.

## Floating text

![All the floating text styles side by side: white damage, a larger gold critical hit, gold Blocked, blue Dodged, red damage taken, green healing, status hits, a combo counter and Shatter +3]({{base}}/assets/img/ui-floating-text.jpg)
*Every floating text style at once. In the game they come one at a time.*

The numbers above enemies are now in the new heading font, in colors and sizes from the style sheet. Regular damage is white, critical hits are gold and bigger, Blocked is gold, Dodged is in Hermes' blue, and damage you take is red.

## The main menu and Realms

![The new main menu, the Realms panel with one realm and three empty slots, and the delete confirmation]({{base}}/assets/img/ui-realms.jpg)

The main menu has the logo and studio name, a gold Continue, then Play, Options and Exit, a short note about the game being in Pre-Alpha, and buttons for patch notes, Discord and the Steam wishlist. Character creation, the patch notes panel and the loading screen were redesigned to match.

The bigger change here is **Realms**, which are save slots:

- You can have up to **four Realms**. Each one is a separate character with its own progress: inventory, skills, placed props, farms, quests and the loot chest.
- **The character's name is the Realm's name**, and each Realm shows its level and how long you've played it.
- **Continue** picks up the Realm you played last. **Play** opens the Realms panel, where you can start a new one or delete one, with a confirmation.
- **Settings and achievements are shared** across Realms. "Reset Game Progress" in the settings now only resets the selected Realm.
- If you already have a save, it moves into your first Realm automatically the first time you start the game.

## Other changes

- **Cursor size.** There's a new slider in Settings for the size of the mouse cursor, and tooltips now move aside so the cursor doesn't cover them.
- **Wrong item types.** Iron Ingot, Copper Ingot and Purified Clay were labeled "Bench" in their tooltips, and the chest was labeled as a plant. Copper Ingot and Purified Clay also wouldn't stack. That came from a bug in my spreadsheet import, which copied a bench recipe's settings onto the ingredients in it. Fixed at the source.
- **God statues.** I've turned off praying at the god statues for now. The god card screen that opens there is getting a redesign, and I'd rather it stays closed than shows the old one.

## Tools

The same editor tool from the last post did most of the heavy lifting: it applies the kit to each window from one place, so a change in the style sheet reaches every panel at once. It now covers everything above, from the benches to the floating text.

## What's next

The interface finally looks like one game. Next up is the god card screen at the statues, so praying can come back, and then filling in the skill trees that now have a home waiting for them.

*Interface screenshots captured October 5 and 6 on a development build. The Craft window was captured with sample items in the bag. The Realms panel shows my development save, which is why it says level 99.*
