name: offer-builder
version: 1.0
input: context.md
output: context.md
autoresearch: true
dependencies: coreyhaines31/copywriting, coreyhaines31/pricing-strategy, coreyhaines31/page-cro
---

## Purpose

Build an irresistible offer using Alex Hormozi's value equation methodology. Transform product/service descriptions into high-converting offers that prospects can't refuse by maximizing perceived value while minimizing perceived risk.

## Core Framework: The Value Equation

Every irresistible offer optimizes this equation:

```
Value = (Dream Outcome × Perceived Likelihood of Achievement) / (Time Delay × Effort & Sacrifice)
```

**How to apply it:**
- **Dream Outcome (↑)** — Make the outcome bigger, more specific, more emotionally resonant
- **Perceived Likelihood (↑)** — Build certainty with proof, guarantees, and specific mechanisms
- **Time Delay (↓)** — Reduce wait time; deliver results faster than alternatives
- **Effort & Sacrifice (↓)** — Minimize what the customer has to do; "done for you" beats "do it yourself"

A high-value offer has a **big numerator** (outcome × likelihood) and a **small denominator** (time × effort).

## Reference Materials

**See prompts/irresistibleofferbp.md** — Full methodology for offer architecture, including:
- 5 levels of awareness (unaware → very aware)
- Delivery mechanism optimization
- Big Problem → Irking Pain Points framework
- Risk reversal tactics beyond "money-back"
- Unique mechanism naming and positioning

**See prompts/landingpagegen.md** — Direct response copywriting structure for:
- Headline variations (3 options)
- Sub-headline construction
- Lead/Problem amplification
- Transformation stories
- Call to action with risk reversal

## Input Requirements

**Read from context.md:**
- Customer Avatar section (demographics, psychographics, pain points, fears, verbatim language)
- Brand Positioning (niche, differentiation, origin story)
- Brand Seed (offer, unfair advantage, content pillars)

**If context.md is incomplete:**
Use the interview questions from prompts/irresistibleofferbp.md to gather:
- Target audience awareness level
- Current delivery mechanism
- Core problems and outcomes
- Competitive landscape
- Existing guarantees

## Output Structure

The offer blueprint must include ALL of these sections, written to context.md under `## Offer`:

### 1. Mechanism Name

Create a specific, ownable name for the proprietary method/system.

**Requirements:**
- Must be unique and memorable (not generic like "The Method")
- Should imply transformation or process
- Include 3-5 step breakdown with action verbs
- Each step should solve a specific part of the customer's problem

**Examples:**
- "The Synto Method" → Map, Prioritize, Ship, Stay
- "The Pipeline Acceleration Framework" → Audit, Automate, Accelerate, Analyze

### 2. Dream Outcome

Define the specific, tangible, measurable result.

**Requirements:**
- Must include specific numbers (hours saved, revenue, timeframes)
- Must be emotionally resonant (tie to avatar's deepest desire)
- Must be verifiable (pass the "can I prove this?" test)
- Must address the avatar's #1 fear directly

**Anti-patterns (never use):**
- "Help you grow your business"
- "Improve your marketing"
- "Make things easier"
- "World-class results"

**Correct patterns:**
- "Save 15+ hours/month within 30 days"
- "Reduce lead response time from 2.7 hours to 47 seconds"
- "Scale from $1.2M to $2M ARR in 18 months"

### 3. Value Stack

Create 3-5 components each with stated perceived value.

**Value Stack Structure:**
| Component | Description | Perceived Value |
|-----------|-------------|-----------------|
| Core deliverable | Primary service/product | $X,XXX |
| Bonus 1 | Accelerates outcome | $XXX |
| Bonus 2 | Removes friction | $XXX |
| Bonus 3 | Adds certainty | $XXX |
| **Total Value** | Sum of perceived values | **$XX,XXX** |

**Requirements:**
- Each bonus must have a specific name (not "Bonus 1")
- Each bonus must solve a specific objection or pain point
- Perceived values must be realistic (not inflated 10x)
- Total value should be 3-5x the actual price

### 4. Price Anchor + Final Price

Establish price context and deliver the offer price.

**Anchor Structure:**
1. Cost of alternative (hiring, doing nothing, competitor)
2. Cost of problem continuing (lost revenue, wasted time)
3. Value received vs. investment

**Example:**
```
Cost of hiring AI developer: $60,000-120,000/year
Cost of this offer: $4,000/month = $48,000/year
Your savings: $12,000-72,000/year
```

**Pricing tiers (if applicable):**
| Tier | Monthly | Scope | Delivery Speed |
|------|---------|-------|----------------|
| [Tier Name] | $X,XXX | [Scope] | [Timeframe] |

### 5. Guarantee

Provide a specific, risk-reversing guarantee.

**Requirements:**
- Must have teeth (not just "money-back")
- Must be specific about conditions and timeline
- Must address the avatar's biggest purchase fear
- Should have an "action" component (do X by Y or your money back)

**Examples:**
- "Save 15+ hours in 30 days or full refund"
- "If you don't get [outcome] in [timeframe], we'll [specific action]"
- "30-day guarantee: If you don't save 15+ hours/month, get a full refund. No questions, no hard feelings. We bet on ourselves."

### 6. Landing Page Copy Draft

Generate landing page copy using prompts/landingpagegen.md structure.

**Required sections:**
1. **Headline Variations (3 options)** — Test different angles (problem, outcome, mechanism)
2. **Sub-headline** — Expand headline with additional specificity
3. **Lead** — Amplify problem with bullet points (use avatar's verbatim language from context.md)
4. **Transformation** — Show before/after with proof elements
5. **Offer Introduction** — Feature-benefit presentation
6. **Testimonial Placeholder** — Mark where social proof goes
7. **Call to Action** — Urgency + price + guarantee

**Copy requirements from landingpagegen.md:**
- Vary sentence length (short and long)
- Use line breaks between most sentences
- Write conversationally (Gary Halbert style)
- 8th-grade reading level
- Bold for key points, italics for emphasis

## Self-Check Before Finishing

Apply these 5 binary Y/N checks (from evals/offer-evals.md):

- [ ] **Mechanism named?** — Is there a specific, ownable mechanism name?
- [ ] **Guarantee stated?** — Is there a specific guarantee with conditions and timeline?
- [ ] **Dream outcome specific?** — Is there at least one specific, measurable, tangible outcome?
- [ ] **Free of generic filler?** — No "world-class," "game-changing," "revolutionary" empty phrases?
- [ ] **Addresses named fear?** — Does the offer directly speak to the avatar's stated fear?

If ANY check fails: revise the offer before outputting.

## Content Principles

**From Contentos context.md:**
- **Specific over generic** — Never write vague content
- **Numbers over claims** — Use "47 seconds," "15 hours," "$2,340/month" — specific metrics
- **Problems before solutions** — Lead with pain, then fix
- **Proof over promises** — Show real results, not hype
- **Direct tone** — No jargon, no fluff

**Language Patterns:**
- Use avatar's verbatim language from context.md
- Lead with specific pain points (not solutions)
- Include specific metrics in every claim
- Write in 8th-grade reading level
- Avoid industry jargon unless avatar uses it

## Workflow

1. **Read context.md** — Extract customer avatar, pain points, fears, verbatim language
2. **Calculate value equation** — Identify how to maximize numerator, minimize denominator
3. **Create mechanism** — Name and structure the proprietary method
4. **Define outcomes** — Make them specific, measurable, emotionally resonant
5. **Build value stack** — 3-5 components with perceived values
6. **Set pricing** — Anchor against alternatives, show ROI
7. **Design guarantee** — Address avatar's biggest purchase fear
8. **Draft landing copy** — Apply prompts/landingpagegen.md structure
9. **Self-check** — Verify all 5 eval criteria pass
10. **Output to context.md** — Append under `## Offer` section

## Constraints

- Never use generic phrases: "world-class," "game-changing," "revolutionary," "cutting-edge"
- Every numeric claim must be specific: "47% increase" not "significant increase"
- No claims without credibility markers (proof, guarantee, or confidence)
- Guarantee must include specific timeline (not just "satisfaction guaranteed")
- Every bonus must have a specific name and value — no "Bonus 1, Bonus 2"
- Output must pass all 5 eval checks before finishing

## Output Format

Write the complete offer blueprint to context.md under a new `## Offer` section using markdown formatting:

```markdown
## Offer

### Offer Blueprint

**Mechanism: [Name]**
1. [Step 1]
2. [Step 2]
3. [Step 3]
...

**Dream Outcome**
[Specific, measurable outcome with timeframe]

**Value Stack**
| Component | Description | Perceived Value |
|-----------|-------------|-----------------|
| ... | ... | ... |

**Pricing**
[Anchor context + tiers]

**Guarantee**
[Specific terms with timeline]

### Landing Page Copy Draft

**Headline Variations:**
1. [Option 1]
2. [Option 2]
3. [Option 3]

**Sub-headline:**
[Copy]

**Lead:**
[Problem amplification with bullet points]

**Transformation:**
[Proof and before/after]

**Offer:**
[Feature-benefit presentation]

**Call to Action:**
[Urgency + price + guarantee + button]

---

**Positioning Recommendations**
[Strategic advice for communicating this offer]
```

## Example Output (Reference Only)

From context.md for Synto Labs (George avatar):

```
Mechanism: The Synto Method
1. Map — Deep-dive into specific workflows
2. Prioritize — Identify highest-ROI fix
3. Ship — Deploy in 48 hours
4. Stay — Remain as embedded AI team

Dream Outcome: Save 15+ hours/month within 30 days. Lead response time drops from 2.7 hours to 47 seconds.

Guarantee: 30-day guarantee. If you don't save 15+ hours/month, full refund. No questions.

Value Stack:
- Custom AI agent deployment: $15,000 value
- Workflow audit: $3,000 value
- Ongoing optimization: $5,000 value
- Direct founder access: $10,000 value
Total: $33,000 for $4,000/month

Sample Headline: "Your leads go cold while you sleep. We fix that in 47 seconds."
```

This follows Hormozi's value equation:
- **Dream Outcome ↑** — 15+ hours/month saved, leads followed up
- **Perceived Likelihood ↑** — 48-hour delivery, proven agents, guarantee
- **Time Delay ↓** — Working agent in 48 hours (fastest in market)
- **Effort & Sacrifice ↓** — Zero learning required; done for you