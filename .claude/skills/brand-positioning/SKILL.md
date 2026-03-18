---
name: brand-positioning
version: 0.1
input: context.md
output: context.md
autoresearch: false
dependencies: anthropics/brand-guidelines, anthropics/copywriting
---

## Purpose
Define your personal brand identity and position in the market.

## Prompt Dependencies
This skill uses the following base prompts. Read them before executing:
- prompts/personalbrand.md — Personal brand strategy framework with 10-phase discovery, research, voice definition, and monetization approach

## Runtime Instructions
1. Read context.md ## Brand Seed section in full before running
2. Use the base prompt above with the human's Brand Seed answers as input
3. Run the full prompt — do not summarise or shortcut
4. Output must populate context.md ## Brand Positioning section
5. Output must include: niche, differentiation, origin story, tone of voice, 1-2 sentence bio
6. Be specific — no generic positioning statements

## Tools
- anthropics/brand-guidelines skill
- anthropics/copywriting skill
- websearch (for competitive research)

## Notes
- Do not modify answers.md
- Do not modify /prompts/
- Output must be specific, never generic

## Evals
See evals/brand-positioning-evals.md for binary pass/fail criteria
