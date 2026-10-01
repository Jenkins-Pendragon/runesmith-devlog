# The Runesmith Devlog

Source of the development log for [The Runesmith](https://therunesmith.com/), published with GitHub Pages from the `docs/` folder.

## Add a post

1. Put images in `assets/img/` (JPG, 1600 px wide is plenty).
2. Create `posts/YYYY-MM-DD-slug.md`:

   ```markdown
   ---
   title: Post title
   date: 2026-10-05
   number: 6
   period: September 23 to October 5
   summary: One or two sentences shown on the list and in link previews.
   cover: cover-image.jpg
   cover_alt: What the cover shows
   commits: abc1234..def5678
   ---

   Body in Markdown. Images: ![alt]({{base}}/assets/img/file.jpg)
   ```

3. Build and preview:

   ```bash
   pip install markdown
   python build.py --serve
   ```

4. Commit `posts/`, `assets/` and the regenerated `docs/`, then push.

## Custom domain

To serve from `devlog.therunesmith.com`: add a `CNAME` record pointing to `jenkins-pendragon.github.io`, put the domain in a `CNAME` file at the repo root, set `base_url` to `""` and `site_url` to `https://devlog.therunesmith.com` in `site.json`, rebuild and push.
