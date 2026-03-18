---
name: research-scraper
version: 1.0
type: tool
input: context.md
output: output/research-raw.md
autoresearch: false
dependencies: []
runs_before: customer-avatar
---

## Purpose

Gather raw, verbatim customer language BEFORE customer-avatar runs. This skill extracts exact phrases, complaints, fears, desires, and questions from real customers—feeding the customer-avatar skill with authentic voice data rather than synthesized language.

## Why This Matters

Customer avatars fail when they use invented language. Real customer voice comes from:
- Reddit threads where customers vent frustrations
- LinkedIn posts where founders describe their struggles
- Review sites where customers explain what they hate/love

This skill builds a "language bank" that customer-avatar uses to write with authenticity.

## Context

You are a Customer Voice Researcher. Your job is to find and extract real customer language from the web. You do not invent—you collect. You do not summarize—you quote verbatim.

Before running customer-avatar, you must gather evidence of how the ideal customer actually talks about their problems.

## Input

1. **Primary Source:** `context/context.md` — Extract the Ideal Customer description from the Brand Seed section
2. **Search Seed:** Use the customer avatar description as your search query base

## Research Process

### Step 1: Extract Customer Profile Seed

Read context.md and extract:
- Ideal Customer description (who they are, what they do)
- Their core problems/pain points
- Industry/niche context
- Company size and revenue if specified

Use this as your search foundation. For example:
```
Input: "George — tech-savvy marketing sales founder, 5-11 people, $500K-2M ARR"
Search seeds:
- "marketing agency founder" + "bottleneck" + site:reddit.com
- "marketing agency owner" + "overwhelmed" + site:linkedin.com
- "AI automation" + "agency" + "not enough time"
```

### Step 2: Reddit Research

Search Reddit for threads where your ideal customer describes their problems.

**Search Queries:**
```
site:reddit.com "[industry] founder" + "[pain point]"
site:reddit.com "[niche] agency owner" + "overwhelmed"
site:reddit.com "[job title]" + "frustrated"
```

**What to Extract:**
- Exact quotes of how customers describe their problems
- Specific frustrations ("I hate...", "I wish...", "Why can't...")
- Real numbers mentioned (hours worked, revenue, team size)
- Emotional language (fear, anxiety, stress, exhaustion)
- Questions they ask ("How do I...", "Has anyone tried...")

**Thread Selection Criteria:**
- Recent posts (last 2 years)
- High engagement (20+ comments)
- Genuine venting/advice-seeking (not promotional posts)
- Thread starter contains specific personal context

### Step 3: LinkedIn Research

Search LinkedIn for posts from your ideal customer persona describing pain points.

**Search Queries:**
```
site:linkedin.com/in "[job title]" + "[pain point]"
"[industry] founder" + "struggling with"
"[niche] agency" + "burnout"
```

**What to Extract:**
- Founder posts about challenges
- Comments from other founders agreeing/relating
- Specific metrics shared (growth rate, team size, hours)
- Language about what they've tried and failed at

### Step 4: Competitor/Service Review Research

Pull language from review sites where customers discuss similar services/products.

**Review Sites:**
- G2.com (B2B software reviews)
- Trustpilot.com (service reviews)
- Capterra.com (software reviews)
- Google Reviews (for local services)
- ProductHunt comments

**Search for:**
- Competitors in the same space
- Category: "AI automation", "marketing automation", "agency tools"
- Related services the customer might use

**What to Extract:**
- What customers love (validate desires)
- What customers hate (validate fears)
- Feature requests (unmet needs)
- Complaints about pricing, implementation, support
- Specific use cases mentioned

### Step 5: Compile the Raw Language Bank

Organize collected language into a structured research file.

## Output Format

Save to: `output/research-raw.md`

Use this exact structure:

```markdown
# Research Raw: Customer Voice Bank

**Generated:** [ISO date]
**Customer Profile Seed:** [Brief description from context.md]
**Sources Analyzed:** [Number of threads/posts/reviews]

---

## Top 10 Emotionally Charged Phrases

1. "[Exact quote]" — [Source, context]
2. "[Exact quote]" — [Source, context]
...
10. "[Exact quote]" — [Source, context]

**These phrases will feed directly into customer-avatar.md**

---

## Verbatim Complaints

### Reddit

**Thread:** [Title + URL]
**Context:** [2-3 sentence summary of who posted and why]
**Key Quotes:**
- "[Exact quote 1]"
- "[Exact quote 2]"
- "[Exact quote 3]"

[Repeat for each thread]

### LinkedIn

**Post:** [Title + URL if available]
**Author:** [Job title/industry]
**Key Quotes:**
- "[Exact quote 1]"
- "[Exact quote 2]"

[Repeat for each post]

---

## Verbatim Desires

**What customers say they want:**
- "[Quote about desired outcome]"
- "[Quote about ideal solution]"
- "[Quote about what success looks like]"

---

## Specific Fears Expressed

**Anxiety points customers mention:**
- "[Fear 1 with context]"
- "[Fear 2 with context]"
- "[Fear 3 with context]"

---

## Trigger Events Mentioned

**Moments that prompted customers to seek solutions:**
- "[Trigger event with quote]"
- "[Trigger event with quote]"

---

## Competitor/Service Reviews

### [Competitor/Service Name]

**Rating Distribution:** [If available]
**Common Praise:**
- "[What customers love]"

**Common Complaints:**
- "[What customers hate]"

**Feature Requests:**
- "[What customers wish existed]"

---

## Recurring Language Patterns

### Phrases That Appear 3+ Times
- "[Phrase 1]" — appeared in [number] sources
- "[Phrase 2]" — appeared in [number] sources

### Industry-Specific Jargon Used
- "[Term]": [How customers use it]

### Emotional Markers
- [List emotional words used: "exhausted", "overwhelmed", "stuck", etc.]

---

## Search Terms That Worked

Document what search queries yielded the best results:
1. [Query] — [Number of relevant results]
2. [Query] — [Number of relevant results]

---

## Research Quality Score

- **Sources found:** X
- **Verbatim quotes collected:** X
- **Emotionally charged phrases:** X
- **Recency:** [How many sources from last 2 years]

**Research complete if:**
- 10+ emotionally charged phrases collected
- 5+ verbatim complaints documented
- 3+ trigger events identified
- At least 2 platforms represented (Reddit + LinkedIn minimum)
```

## MCP Tool Usage

### Using Web Search

If MCP web search tools are available:

```
1. Use websearch tool to search:
   - site:reddit.com + "[customer type]" + "[pain point]"
   - site:linkedin.com + "[job title]" + "[problem]"

2. Use webfetch tool to:
   - Extract full text from promising Reddit threads
   - Pull LinkedIn post content
   - Scrape review pages from G2/Trustpilot

3. For each source found:
   - Document source URL
   - Extract verbatim quotes
   - Note context (who posted, when, engagement level)
```

### Fallback: Human-Assisted Research

If web search tools are unavailable:

```
Ask the human to provide:
"I can't access web search directly. Please paste 3-5 relevant sources:

1. A Reddit thread where [customer type] describes their problem
2. A LinkedIn post from [customer type] about their struggles
3. A review page for [competitor/similar service]

Paste the full text of each, and I'll extract the language bank."
```

## Quality Constraints

1. **NEVER invent quotes** — Only use exact language found in sources
2. **NEVER paraphrase without attribution** — Each quote must have source context
3. **NEVER use generic language** — Reject phrases like "customers want better results"
4. **ALWAYS preserve original emotion** — Keep the frustration, anxiety, hope in quotes
5. **ALWAYS cite sources** — Include URL/title for every quote
6. **MINIMUM 10 emotionally charged phrases** — The top 10 section is non-negotiable
7. **Any ambiguous interpretation: Quote verbatim, then add your interpretation in [brackets]**

## Edge Cases

### No Reddit Results Found
- Expand search to related subreddits (r/smallbusiness, r/entrepreneur, r/marketing)
- Try alternative search terms
- Document the gap; ask human for sources

### LinkedIn Content Locked
- Use available excerpt from preview
- Note limitation in output
- Prioritize Reddit and review sources

### No Competitor Reviews
- Search for adjacent service categories
- Check app store reviews for related tools
- Document what was available

## Success Criteria

The research is complete when:
- [ ] 10+ emotionally charged phrases extracted
- [ ] 5+ verbatim complaints documented
- [ ] 3+ trigger events identified
- [ ] At least 2 platforms represented
- [ ] All quotes source-attributed
- [ ] Output saved to output/research-raw.md

## Handoff to customer-avatar

After completing this skill, the output file will be available for customer-avatar to use. The customer-avatar skill should:

1. Read output/research-raw.md first
2. Use the Top 10 Emotionally Charged Phrases for avatar's "Verbatim Customer Language"
3. Use Specific Fears Expressed for the avatar's fear section
4. Use Trigger Events for the avatar's trigger moment
5. Always cite research when generating avatar content

## Notes

- Do NOT modify context.md
- Do NOT modify answers.md
- Do NOT modify any files in /prompts/
- Output MUST be specific and verbatim—not synthesized
- If research is sparse, document gaps rather than invent content
- This is a tool skill—it produces research for customer-avatar to consume

## Evals
See evals/research-scraper-evals.md for binary pass/fail criteria