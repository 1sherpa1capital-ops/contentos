# AGENTS.md — Contentos

> Agent instructions for Contentos, the marketing content system.
> Always read `context/answers.md`, `context/context.md`, and `context/offer.md` before doing anything.

---

## Overview

Contentos generates brand content through an AI-native workflow: onboarding → positioning → avatar → offer → content engine. Skills (modular expertise packages) handle each phase.

**Key principle:** This is a content system, not a traditional codebase. No build step. No linters. Skills execute via Claude Code or OpenCode.

---

## Project Structure

```
contentos/
├── context/                    # Source of truth — read before anything
│   ├── answers.md             # Your answers, tone, voice (read-only by agents)
│   ├── context.md             # Brand positioning, avatar, content pillars
│   ├── offer.md               # Your offer, pricing, positioning
│   └── validation.md          # Real-world outreach feedback log
├── prompts/                    # Base layer prompts (immutable)
├── output/                     # Generated deliverables
├── results/                    # Autoresearch logs
└── scripts/                    # Python automation
    └── autoresearch.py         # Skill testing harness
```

Skills live in `.claude/skills/` at the repo root (shared across all modules).

---

## Commands

```bash
# Run single skill iteration
python3 scripts/autoresearch.py --skill customer-avatar --iterations 1

# Full autoresearch loop
python3 scripts/autoresearch.py --skill customer-avatar --iterations 10

# Dry run
python3 scripts/autoresearch.py --skill customer-avatar --iterations 1 --dry-run
```

---

## Workflow

1. **Onboarding** → Run `ONBOARDING.md` prompt → populates `answers.md` + `context.md`
2. **Brand Positioning** → Run `brand-positioning` skill
3. **Customer Avatar** → Run `customer-avatar` skill
4. **Offer** → Run `offer-builder` skill
5. **Content** → Run `content-engine` skill

---

## Available Skills

**Content** (`.claude/skills/`):
- `content-engine` — 4-week content calendar
- `content-strategy` — Content approach planning
- `copywriting` — Sales copy
- `docx` — Word document generation
- `email-sequence` — Email drip campaigns
- `social-content` — Social media posts

**Marketing** (`.claude/skills/`):
- `ai-seo`, `brand-positioning`, `cold-email`, `competitor-alternatives`
- `customer-avatar`, `launch-strategy`, `marketing-automation`
- `offer-builder`, `paid-ads`, `pricing-strategy`, `research-scraper`
- `sales-enablement`, `seo-audit`

**Dev** (`.claude/skills/`):
- `dispatching-parallel-agents`, `executing-plans`
- `mcp-builder`, `skill-creator`, `verification-before-completion`

---

## SKILL.md Format

```yaml
---
name: skill-name
description: Specific trigger phrases. Use third person: "This skill should be used when..."
version: 1.0.0
---

## Purpose
One sentence describing what the skill does.

## Instructions
Use imperative voice ("Do X", not "You should do X"). Explain WHY, not just WHAT.

## Constraints
- Never modify answers.md (human ground truth)
- Never use placeholder text like "TBD"
- Output must be specific, never generic
```

---

## Content Principles

- **Specific over generic** — "47 seconds" not "fast"
- **Numbers over claims** — "15 hours saved" not "save time"
- **Problems before solutions** — Lead with pain
- **Proof over promises** — Show real results

---

## Critical Constraints

- **Never modify `answers.md`** — human ground truth, read-only
- **Never modify `context.md` during autoresearch** — read-only during runs
- **Always revert on failure** — never leave skills in broken state
- **Binary evals only** — no Likert scales or numeric scoring

---

## Autoresearch Evals

Tests use binary Y/N evals (max 6 per skill). Evals live in `.claude/skills/{skill}/evals/`.
Pass threshold: 8/10 outputs must pass all criteria.
Log: `results/autoresearch-log.tsv`

---

## Reference

| Document | Purpose |
|----------|---------|
| `context/answers.md` | Your Q&A, voice, tone (read-only) |
| `context/context.md` | Brand, avatar, content (auto-generated) |
| `context/offer.md` | Your offer and positioning |
| `../AGENTS.md` | System-wide agent instructions |
