---
name: content-engine
version: 0.1
input: context.md
output: context.md
autoresearch: false
dependencies: coreyhaines31/content-strategy, coreyhaines31/social-content, coreyhaines31/email-sequence
---

## Purpose
Build a 4-week content engine with newsletter drafts and social media hooks.

## Prompt Dependencies
This skill uses the following base prompts. Read them before executing:
- prompts/newsletterwriting.md — APAG format newsletter framework for educational, entertaining deep-expertise content
- prompts/xdrafts.md — Viral X/Twitter post framework with one-sentence, multi-line, and listicle formats

## Runtime Instructions
1. Read full context.md before running
2. Run Newsletter prompt first — produce one full newsletter draft
3. Run X Drafts prompt second — pull 10 post hooks from the newsletter
4. Apply content waterfall:
   - Newsletter → YouTube script → podcast
   - Posts pulled from newsletter
   - Best posts → Reels/Shorts scripts
   - Other posts → carousels (LinkedIn, Instagram, YouTube community)
5. Output must populate context.md ## Content section with:
   - 4-week content calendar
   - 3 newsletter drafts
   - 10 post hooks
   - Content waterfall mapped per platform
6. Do not post content — drafts only
7. After producing post hooks, pass top 3 hooks to video-engine.md
   for video rendering — only if video-engine.md is present

## Tools
- coreyhaines31/content-strategy skill
- coreyhaines31/social-content skill
- coreyhaines31/email-sequence skill
- .agents/skills/content/video-engine.md (optional - for video rendering)

## Notes
- Do not modify answers.md
- Do not modify /prompts/
- Output must be specific, never generic
- Do not post content — drafts only

## Evals
See evals/content-engine-evals.md for binary pass/fail criteria
