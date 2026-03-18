# Contentos

An open-source personal brand and offer system powered by Claude Code and skills architecture.
Inspired by Dan Koe's one-person business framework and Karpathy's autoresearch loop.

## What It Does

Builds three things:
- **Brand** — who you are, what you help people achieve, why they should care
- **Content** — ideas and a production system to attract the right people
- **Offer** — a product or service people can't say no to

## Features

- **Onboarding Agent** — Structured interview to extract your brand truth
- **Brand Positioning** — Define your niche, voice, and differentiation
- **Customer Avatar** — Build a specific picture of who you serve
- **Offer Builder** — Create irresistible offers with proof and guarantees
- **Content Engine** — Generate content across platforms systematically
- **Autoresearch Loop** — Continuous skill improvement via binary evals

## Install

```bash
git clone https://github.com/1sherpa1capital-ops/contentos.git
cd contentos
```

## Quick Start

1. Fill out `context/answers.md` manually (or run the onboarding agent)
2. Open Claude Code or OpenCode in this directory
3. Run: `"Begin the initiation process using ONBOARDING.md"`

## Project Structure

```
contentos/
├── context/                    # Source of truth
│   ├── answers.md             # Your answers (edit manually)
│   ├── context.md             # Brand, avatar, offer, content (auto-generated)
│   ├── offer.md               # Your offer details
│   └── validation.md          # Real-world feedback log
├── prompts/                   # Base prompts (immutable, from Dan Koe)
├── output/                    # Generated deliverables
├── results/                   # Autoresearch logs
└── scripts/                   # Automation scripts
    └── autoresearch.py        # Skill testing harness
```

## Stack

- **Claude Code / OpenCode** — orchestrator
- **Skills** (`.claude/skills/`) — modular expertise packages
- **Prompts** (`/prompts/`) — Dan Koe base prompts (never modified)
- **Autoresearch loop** — continuous skill improvement via evals

## Core Skills

Skills live in `.claude/skills/`:

| Category | Skills |
|----------|--------|
| Content | `content-engine`, `content-strategy`, `copywriting`, `docx`, `email-sequence`, `social-content` |
| Marketing | `ai-seo`, `brand-positioning`, `cold-email`, `competitor-alternatives`, `customer-avatar`, `launch-strategy`, `offer-builder`, `paid-ads`, `pricing-strategy`, `research-scraper` |
| Sales | `sales-enablement`, `revops` |
| Optimization | `page-cro`, `form-cro`, `ab-test-setup`, `onboarding-cro` |

## Workflow

1. **Onboarding** → Run `ONBOARDING.md` → populates `answers.md` + `context.md`
2. **Brand Positioning** → Run `brand-positioning` skill
3. **Customer Avatar** → Run `customer-avatar` skill
4. **Offer** → Run `offer-builder` skill
5. **Content** → Run `content-engine` skill

## Autoresearch

Test and improve skills using binary evals:

```bash
# Run single iteration
python3 scripts/autoresearch.py --skill customer-avatar --iterations 1

# Full autoresearch loop
python3 scripts/autoresearch.py --skill customer-avatar --iterations 10

# Dry run
python3 scripts/autoresearch.py --skill customer-avatar --iterations 1 --dry-run
```

Pass threshold: 8/10 outputs must pass all criteria.

## Customization

All personal information lives in `context/`:
- `answers.md` — your ground truth (never modified by agents)
- `offer.md` — your specific offer, pricing, positioning
- `context.md` — your brand, avatar, content pillars

Edit these files to make Contentos yours.

## License

MIT License — use it for anything, no attribution required.

## Credits

- Dan Koe — for the one-person business framework
- Andrej Karpathy — for the autoresearch concept
- Anthropic — for Claude and the skills architecture
