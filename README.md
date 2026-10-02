# The Runesmith Devlog

Source of the development log for [The Runesmith](https://therunesmith.com/), published with GitHub Pages from the `docs/` folder.

## Add a post

1. Put images in `assets/img/` (JPG, 1600 px wide is plenty).
2. Create `posts/YYYY-MM-DD-slug.md`:

   ```markdown
   ---
   title: Post title
   date: 2026-10-05
   number: 7
   series: devlog
   period: September 23 to October 5
   summary: One or two sentences shown on the list and in link previews.
   cover: cover-image.jpg
   cover_alt: What the cover shows
   commits: abc1234..def5678
   stories: S0319, S0324
   source_snapshot: e2f2ba8e3f92a4221bcbd8e404b45bec5d071fae
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

## Development Archive

The current Devlog stays at `/`. Retrospective entries are listed oldest first at `/archive/` with separate numbering. Set `series: archive` for an archive post; posts without a series keep their existing Devlog behavior. Existing URLs are preserved. Previous/next links stay within each series, and the RSS feed contains current devlogs only.

`stories` is a comma-separated list of canonical IDs from the vault's `.devlog/runesmith/` catalog. Include the full `source_snapshot` when story IDs are present. The fields record source attribution, not proof of publication: local posts are drafts until pushed and checked live. A later update may reference the same story ID when it describes new evidence after an earlier post.

Archive dates describe when the work happened. Use period-appropriate images when available; label images captured later with their actual capture date. Archive content is written retrospectively and does not repeat historical promises as current announcements.
