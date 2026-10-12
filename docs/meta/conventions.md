---
title: Conventions
updated: 2026-10-10
---

# Conventions

The rules that keep this knowledge base consistent as it grows. The short version lives in the repository README; this page is the full reference.

## Principles

1. **One idea per note.** If a note needs two unrelated TL;DRs, split it.
2. **Write for your future self,** who has forgotten everything. Define symbols, state units, link prerequisites.
3. **Prefer checkable content.** Worked examples with numbers or runnable code beat prose. If a number appears, you should be able to reproduce it.
4. **Link generously, organize simply.** Folders give coarse structure; links give the real graph.
5. **Notes are living.** Update `status` and `updated` honestly.

## Folder layout

```text
docs/
├── index.md              home page and learning paths
├── <topic>/              one folder per topic, lowercase-kebab-case
│   ├── index.md          topic hub: scope, visual summary, note table, reading order
│   └── <note-name>.md    individual notes
├── assets/diagrams/      SVG files referenced by notes
├── meta/                 this page and other housekeeping
├── glossary.md
├── reading-list.md
└── tags.md
```

A new topic needs a folder, an `index.md` hub, and an entry in `mkdocs.yml`. Use `python scripts/new_note.py <topic> "<Title>" --new-topic` to scaffold it.

## File naming

- Lowercase, hyphen-separated, descriptive: `state-space-and-lqr.md`, not `Note3.md`.
- File names are permanent links; rename only with a search-and-fix of inbound links (`check_links.py` will find breakage).

## Front matter

Every note starts with:

```yaml
---
title: Human-Readable Title
tags: [topic-tag, subtopic-tag]
status: seed        # seed | growing | evergreen
updated: YYYY-MM-DD
---
```

| Status | Meaning |
|---|---|
| `seed` | Skeleton or rough draft; may have gaps or unchecked claims |
| `growing` | Useful and mostly correct; still being improved |
| `evergreen` | Reviewed, verified, unlikely to need change |

Hub pages (`index.md`) and reference pages need only `title` and `updated` (hubs usually carry `tags` and `status` too).

## Tag vocabulary

- **Topic tags** (one per note, matching its folder): `ai`, `robotics`, `physics`, `electronics`, `control`, `aerospace`, `mathematics`.
- **Subject tags** (one to three): `deep-learning`, `kinematics`, `estimation`, `thermodynamics`, `orbits`, and so on.
- Reuse existing tags before inventing new ones; browse the [Tags](../tags.md) page to see what exists.

## Note anatomy

In this order, omitting sections that do not apply:

1. **TL;DR** (blockquote): one or two sentences.
2. **Why it matters**
3. **Core ideas**
4. **Diagram**
5. **Key equations / facts**
6. **Worked example**
7. **Pitfalls**
8. **Related** (links to other notes)
9. **Further reading**

## Diagrams

- **Mermaid** (fenced ```` ```mermaid ```` blocks) for flowcharts, state machines, sequences and concept maps. It renders on GitHub and on the site.
- **SVG** in `docs/assets/diagrams/` for things Mermaid cannot draw (circuits, orbits). Give each SVG a `<title>` and `<desc>` for accessibility, and a white background so it reads in dark mode.
- Quote Mermaid labels that contain punctuation: `A["Q = softmax(QK^T)"]`.
- A diagram should answer a question the prose alone answers poorly: flow, structure, comparison. Do not draw decoration.

## Math

- Inline `$...$`, display `$$...$$` (LaTeX). Works on GitHub and on the site.
- Define every symbol on first use, with units where relevant.
- Avoid a dollar sign for currency in running text; it can be parsed as math.

## Code

- Keep examples short, complete and **runnable**; state the expected output when it is a number you verified.
- Python by default; use NumPy and the standard library where possible.

## Links

- Use relative links with the `.md` extension: `[Kinematics](../robotics/kinematics.md)`.
- Every note should link to at least one other note (Related section) and be linked from its topic hub.
- External links go in *Further reading*; cite books and papers by author and title.

## Quality checklist before committing

- [ ] TL;DR states the point in one or two sentences
- [ ] Symbols defined, units stated
- [ ] Every number in a worked example reproduced
- [ ] At least one diagram or table that earns its place
- [ ] Pitfalls section contains mistakes people actually make
- [ ] Linked from the topic hub and from at least one other note
- [ ] `python scripts/check_links.py` passes
- [ ] `mkdocs build --strict` passes (if you have the site tooling installed)
