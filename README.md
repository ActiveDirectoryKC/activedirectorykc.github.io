# activedirectorykc.net source

MkDocs + Material source for https://www.activedirectorykc.net.

Rebuilt 2026-10-03 from the published output after the original project was lost.

## Build locally

    pip install -r requirements.txt
    mkdocs serve        # preview
    mkdocs build        # output to site/

## Layout

- `mkdocs.yml`: theme, palette, blog plugin, footer social links
- `docs/index.md`, `docs/about.md`: pages
- `docs/posts/`: blog posts (front matter: title, date, author, tags). Published at `/posts/YYYY/MM/DD/slug/`.
- `docs/resources/`: wiki-style Resources section, imported from the r/ActiveDirectory wiki backup and Blog notes
- `hooks/copyright.py`: sets the footer end year at build time
- `hooks/legacy_redirects.py`: redirect stubs from the old root post URLs (`/2021/04/22/...`) to `/posts/...`. Add a row only for URLs that were already public.
- `docs/assets/`: logo, icon, custom.css
- `docs/CNAME`: custom domain (`www.activedirectorykc.net`)

## Notes

- Nested lists need 4-space indentation. Python-Markdown ignores 2-space nesting.
- A list item that starts with `#tag` must be written `\#tag`, or it renders as a heading.
- Resources carries a "Work in progress" banner (`docs/resources/index.md`). Remove it when the section is ready.

## Publishing

Built output goes to `ActiveDirectoryKC/activedirectorykc.github.io` (main branch).
Do not edit files in that repo by hand. They get overwritten on the next build.
