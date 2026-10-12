# Engineering & AI Knowledge Base

A personal, Markdown-based knowledge base for engineering and AI. Each note is short, structured and checkable: a TL;DR, diagrams, key equations, a worked example with real numbers or runnable code, and the pitfalls people actually hit.

Every note is plain Markdown, so it reads well right here on GitHub, in any editor, or in [Obsidian](https://obsidian.md) (open the `docs/` folder as a vault). An optional static site (MkDocs Material) adds search, navigation, tags and rendered math.

## What is inside

| Topic | Notes |
|---|---|
| [Artificial intelligence](docs/ai/index.md) | [ML fundamentals](docs/ai/machine-learning-fundamentals.md) · [Neural networks & backprop](docs/ai/neural-networks-and-backprop.md) · [Transformers](docs/ai/transformers.md) · [Reinforcement learning](docs/ai/reinforcement-learning.md) · [ML systems lifecycle](docs/ai/ml-systems-lifecycle.md) |
| [Robotics](docs/robotics/index.md) | [Sense-plan-act](docs/robotics/sense-plan-act.md) · [Kinematics](docs/robotics/kinematics.md) · [State estimation](docs/robotics/state-estimation.md) · [Motion planning](docs/robotics/motion-planning.md) |
| [Control systems](docs/control-systems/index.md) | [PID control](docs/control-systems/pid-control.md) · [Stability & frequency response](docs/control-systems/stability-and-frequency-response.md) · [State space & LQR](docs/control-systems/state-space-and-lqr.md) |
| [Physics](docs/physics/index.md) | [Classical mechanics](docs/physics/classical-mechanics.md) · [Thermodynamics](docs/physics/thermodynamics.md) · [Electromagnetism](docs/physics/electromagnetism.md) · [Quantum & semiconductors](docs/physics/quantum-and-semiconductors.md) |
| [Electronics](docs/electronics/index.md) | [Circuit fundamentals](docs/electronics/circuit-fundamentals.md) · [Microcontrollers & buses](docs/electronics/microcontrollers-and-buses.md) |
| [Aerospace](docs/aerospace/index.md) | [Orbital mechanics](docs/aerospace/orbital-mechanics.md) · [Rocket equation & staging](docs/aerospace/rocket-equation-and-staging.md) · [Aerodynamics basics](docs/aerospace/aerodynamics-basics.md) |
| [Mathematics](docs/mathematics/index.md) | [Linear algebra](docs/mathematics/linear-algebra.md) · [Probability & statistics](docs/mathematics/probability-and-statistics.md) · [Calculus & optimization](docs/mathematics/calculus-and-optimization.md) |

Reference: [Glossary](docs/glossary.md) · [Reading list](docs/reading-list.md) · [Conventions](docs/meta/conventions.md). New here? The [home page](docs/index.md) has four suggested learning paths.

## How the knowledge base is organized

The system has three layers, from coarse to fine.

**1. Topics are folders.** Each topic (`ai`, `robotics`, `physics`, ...) is a folder under `docs/` with an `index.md` *hub*. The hub states the scope, shows a visual summary diagram, lists every note with a one-line summary, and suggests a reading order. Start at a hub when you want an overview.

**2. Notes are single ideas.** Each note covers one concept and follows the same anatomy, so you always know where to look:

```text
TL;DR → Why it matters → Core ideas → Diagram → Key equations
      → Worked example → Pitfalls → Related → Further reading
```

**3. Links and tags form the real graph.** Folders are only a first cut; the *Related* section of each note links across topics (a Kalman filter note links to probability and to LQR), and tags in the front matter allow cross-cutting browsing.

Every note starts with front matter:

```yaml
---
title: State Estimation
tags: [robotics, estimation, probability, slam]
status: growing        # seed | growing | evergreen
updated: 2026-10-10
---
```

`status` is an honest maturity signal: `seed` (rough draft), `growing` (useful, still improving), `evergreen` (reviewed and stable).

### Repository layout

```text
engineering-ai-kb/
├── README.md                     this file
├── LICENSE                       MIT
├── mkdocs.yml                    site configuration and navigation
├── requirements.txt              site dependencies
├── docs/                         ALL content lives here
│   ├── index.md                  home page, concept map, learning paths
│   ├── ai/                       topic folders, each with index.md + notes
│   ├── robotics/
│   ├── control-systems/
│   ├── physics/
│   ├── electronics/
│   ├── aerospace/
│   ├── mathematics/
│   ├── meta/conventions.md       the full writing and style rules
│   ├── assets/diagrams/          SVG diagrams (circuits, orbits)
│   ├── glossary.md
│   ├── reading-list.md
│   └── tags.md
├── templates/note-template.md    skeleton used for new notes
├── scripts/
│   ├── new_note.py               scaffold a note (or a whole topic)
│   └── check_links.py            lint front matter, links, nav coverage
└── .github/workflows/site.yml    CI: lint, build, deploy to GitHub Pages
```

### Visual summaries

Diagrams are first-class. **Mermaid** blocks (flowcharts, concept maps, decision guides) render natively on GitHub and on the site. **SVG** files in `docs/assets/diagrams/` cover what Mermaid cannot draw, such as circuit schematics and orbit geometry. Every hub page opens with a diagram of its topic.

### Math and code

Equations use LaTeX (`$...$`, `$$...$$`), which GitHub and the site both render. Code examples are short and runnable; where a note quotes a numeric result, it was produced by running the code.

## Using it

### Just read it

Browse `docs/` on GitHub, or open the folder in Obsidian or any Markdown editor. No tooling needed.

### Run the site locally

```bash
python -m venv .venv && source .venv/bin/activate     # optional but recommended
pip install -r requirements.txt
mkdocs serve                                          # http://127.0.0.1:8000
```

`mkdocs build --strict` produces the static site in `site/` and fails on broken links.

### Add a note

```bash
python scripts/new_note.py robotics "Inverse Dynamics" --tags robotics,dynamics
```

The script creates the note from the template and prints the remaining steps: add it to the `nav` in `mkdocs.yml`, add a row to the topic's `index.md`, and link it from related notes. To start a new topic folder, add `--new-topic`.

### Check quality

```bash
python scripts/check_links.py
```

This standard-library-only script fails on missing front matter, broken relative links and pages missing from the nav, and warns about orphan pages and bad anchors. CI runs it on every push and pull request.

## Publishing to GitHub

1. Create an empty repository on GitHub (suggested name: `engineering-ai-kb`).
2. In `mkdocs.yml`, replace `YOUR-USERNAME` in `repo_url` and `repo_name` with your GitHub username (optionally set `site_url` to your Pages address).
3. From this folder:

   ```bash
   git init -b main
   git add .
   git commit -m "Initial knowledge base"
   git remote add origin https://github.com/YOUR-USERNAME/engineering-ai-kb.git
   git push -u origin main
   ```

4. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**. The workflow in `.github/workflows/site.yml` then lints, builds and deploys the site on every push to `main`. The site appears at `https://YOUR-USERNAME.github.io/engineering-ai-kb/`.

## Extending it

- **Grow a topic:** add notes until a hub's table gets long, then group the table under subheadings. Split folders only when a topic passes roughly 15 notes.
- **Add topics:** chemistry, signal processing, computer architecture, neuroscience and materials fit the same pattern; use `--new-topic`.
- **Promote notes:** when you have verified a note's claims and examples, move it from `growing` to `evergreen`.
- **Keep the glossary current:** add a term when it appears in two or more notes.

## License

[MIT](LICENSE). Books and papers cited in the notes belong to their authors; the notes paraphrase and link to them rather than reproduce them.
