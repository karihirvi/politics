# CLAUDE_GOAL_EN.md - Strategic Goal-Based Communication Guide

## Overview

This document provides Claude with a systematic approach to creating effective political communication campaigns based on strategic goals. It maps communication styles to psychological stages for maximum impact.

**Important**: All style names in this document refer to the 7 political communication styles defined in detail in CLAUDE_STYLE_EN.md and CLAUDE_STYLE_FI.md.

## Style Name Reference
- **Oratory** = Paasaustyyli/Oratory Style (from CLAUDE_STYLE_*.md)
- **Analytical** = Analyyttinen/Analytical Style
- **Conceptual** = Konseptuaalinen/Conceptual Style
- **Argumentative** = Argumentoiva/Argumentative Style
- **Critical-Political** = Kriittis-poliittinen/Critical-Political Style
- **Philosophical-Religious** = Filosofis-uskonnollinen/Philosophical-Religious Style
- **Populist** = Populistinen/Populist Style

## The 5-Stage Communication Journey

### 1. AWAKEN - Create Awareness
**Purpose**: Break through ignorance or apathy
**Psychological need**: Attention
**Post frequency**: 1-2 posts
**Primary styles**: Critical-Political, Conceptual
**Content focus**: Shocking revelations, paradigm shifts, exposing hidden problems

### 2. AGITATE - Generate Emotional Investment
**Purpose**: Transform awareness into emotional concern
**Psychological need**: Emotional activation
**Post frequency**: 3-5 posts
**Primary styles**: Oratory, Populist, Critical-Political
**Content focus**: Building urgency, creating stakes, us-vs-them dynamics

### 3. EDUCATE - Provide Framework
**Purpose**: Give tools to understand the issue
**Psychological need**: Cognitive clarity
**Post frequency**: 2-4 posts
**Primary styles**: Analytical, Argumentative, Conceptual
**Content focus**: Systematic explanation, addressing objections, building competence

### 4. ACTIVATE - Channel Into Action
**Purpose**: Convert energy into specific behaviors
**Psychological need**: Agency/efficacy
**Post frequency**: 1-2 posts
**Primary styles**: Oratory, Populist
**Content focus**: Clear commands, simple actions, removing barriers

### 5. INTEGRATE - Embed Into Identity
**Purpose**: Make position part of self-concept
**Psychological need**: Belonging/meaning
**Post frequency**: Ongoing/periodic
**Primary styles**: Philosophical-Religious, Oratory, Analytical
**Content focus**: Values, meaning, community celebration

## Strategic Sequences by Goal Type

### Goal: Launch New Political Movement
**Sequence**: Conceptual → Analytical → Argumentative → Oratory
1. AWAKEN with new concept/vision
2. AGITATE around current system failures
3. EDUCATE on alternative framework
4. ACTIVATE specific joining actions
5. INTEGRATE through shared values

### Goal: Win Support for Controversial Policy
**Sequence**: Analytical → Conceptual → Argumentative → Populist → Oratory
1. AWAKEN to hidden benefits/necessity
2. AGITATE about costs of status quo
3. EDUCATE with reframed understanding
4. ACTIVATE simple support actions
5. INTEGRATE as moral imperative

### Goal: Build Opposition Movement
**Sequence**: Critical-Political → Populist → Argumentative → Oratory
1. AWAKEN through scandal/failure exposure
2. AGITATE with economic/cultural threats
3. EDUCATE on systematic problems
4. ACTIVATE protest/voting actions
5. INTEGRATE as resistance identity

### Goal: Manage Crisis/Maintain Base
**Sequence**: Philosophical-Religious → Oratory → Populist
1. AWAKEN to deeper meaning of crisis
2. AGITATE around external threats
3. EDUCATE on our strength/response
4. ACTIVATE unity actions
5. INTEGRATE renewed commitment

## Implementation Guidelines

### Timing Patterns

**Rapid Campaign** (1 week)
- Day 1: AWAKEN
- Days 2-4: AGITATE (multiple daily)
- Days 5-6: EDUCATE
- Day 7: ACTIVATE
- Ongoing: INTEGRATE

**Extended Campaign** (6 weeks)
- Week 1: AWAKEN
- Weeks 2-3: AGITATE
- Weeks 4-5: EDUCATE
- Week 6: ACTIVATE
- Monthly: INTEGRATE

### Message Repetition Psychology

**Core Principle: Theme Repetition, Not Post Repetition**

Research shows people need 7-12 exposures to a message before behavior change. On social media:
- Only 10-20% of followers see any given post
- Each post should present the SAME THEME through DIFFERENT CONTENT
- Never repost identical content (algorithms punish this)

**Repetition Requirements by Stage**

**AWAKEN** (1-2 unique posts)
- Goal: Break through with novelty
- One powerful post often sufficient
- If needed, one follow-up from different angle

**AGITATE** (3-5 unique posts)
- Goal: Build emotional investment
- Same core emotion, different triggers
- Example: Immigration concern through crime stats → victim story → job loss → cultural change → personal threat

**EDUCATE** (2-4 unique posts)
- Goal: Layer understanding
- Each post adds new dimension
- Build complexity gradually

**ACTIVATE** (2-3 unique posts)
- Goal: Overcome action barriers
- Initial CTA → Reminder → Final push
- Each with slightly different framing

**INTEGRATE** (Ongoing, 1-2 monthly)
- Goal: Reinforce identity
- Celebrate wins, share values
- Always fresh content

### Multi-Post Strategies

**AGITATE Stage** (Example: Immigration)
1. Statistical shock post
2. Personal victim story
3. Economic impact analysis
4. Cultural threat warning
5. "This affects you" message

Note: Each post is unique content reinforcing the same emotional message.

**EDUCATE Stage** (Example: Energy Policy)
1. Problem explanation
2. Solution framework
3. Myth debunking
4. Success examples

### Spacing Guidelines

- Minimum 1 day between posts on same theme
- Maximum 3-4 days to maintain momentum
- AWAKEN can be standalone
- AGITATE benefits from 2-3 day rhythm
- EDUCATE works with 2-4 day spacing
- ACTIVATE should be concentrated (daily during action period)

### Style Selection Matrix

**Note**: Style names below are shortened. See "Style Name Reference" section above for full names.

```
Stage     | Never Use        | Sometimes Use    | Primary Use
----------|------------------|------------------|------------------
AWAKEN    | Oratory         | Populist         | Critical, Conceptual
AGITATE   | Analytical      | Philosophical    | Oratory, Populist, Critical
EDUCATE   | Oratory         | Critical         | Analytical, Argumentative, Conceptual
ACTIVATE  | Analytical      | Argumentative    | Oratory, Populist
INTEGRATE | Critical        | Conceptual       | Philosophical, Oratory, Analytical
```

## Key Principles

1. **Diagnose Starting Point**: Where is your audience psychologically?
   - Unaware → Start at AWAKEN
   - Aware but passive → Start at AGITATE
   - Emotional but confused → Start at EDUCATE
   - Informed but inactive → Start at ACTIVATE
   - Active but uncommitted → Start at INTEGRATE

2. **Match Style to Psychology**: Each stage requires different emotional/cognitive approach

3. **Build Momentum**: Early stages create energy, later stages channel it

4. **Measure and Adapt**: Track engagement at each stage, adjust sequence as needed

5. **Cultural Context**: Adapt examples and references to Finnish context

## Usage Instructions for Claude

When user requests a campaign:
1. Identify the main goal (G)
2. Assess target audience starting point
3. Select appropriate sequence from templates
4. Map specific styles to each stage (refer to CLAUDE_STYLE_*.md for full style descriptions)
5. Create campaign folder in campaigns/ directory (c###-topic-name)
6. Generate ALL stages at once in first iteration:
   - 01b-iter/1-awaken.md (1-2 posts)
   - 01b-iter/2-agitate.md (3-5 posts)
   - 01b-iter/3-educate.md (2-4 posts)
   - 01b-iter/4-activate.md (1-2 posts)
   - 01b-iter/5-integrate.md (1-2 posts)
7. Auto-generate 02a-refine.md template for user feedback
8. After final iteration, generate posted.txt for URL tracking

## Campaign Folder Structure

### Folder Naming Convention

Campaign folders use the pattern `c###-topic-name` where:
- **c** = "campaign" (generic prefix for all goal-driven message sequences)
- **###** = three-digit sequential number (001, 002, etc.)
- **topic-name** = descriptive name using lowercase and hyphens

**Why 'c' prefix?**
- Generic enough to cover all goal types (not just electoral campaigns)
- Distinguishes from old single-post system (which used W-XXX)
- Ensures alphabetical grouping of all campaigns
- Short and easy to type
- A "campaign" here means any coordinated sequence of messages pursuing a specific goal

Examples:
- `c001-stop-wind-power` (Goal: Build Opposition Movement)
- `c002-crisis-response` (Goal: Manage Crisis)
- `c003-launch-movement` (Goal: Launch New Political Movement)
- `c004-recruit-youth` (Goal: Convert/Recruit Demographics)

```
campaigns/
├── c001-topic-name/
│   ├── 00-plan.md (optional strategy overview)
│   ├── 01a-request.md (user's initial request)
│   ├── 01b-iter/
│   │   ├── 1-awaken.md
│   │   ├── 2-agitate.md
│   │   ├── 3-educate.md
│   │   ├── 4-activate.md
│   │   └── 5-integrate.md
│   ├── 02a-refine.md (auto-generated feedback template)
│   ├── 02b-iter/ (refined versions)
│   └── posted.txt (auto-generated after final iteration)
```

## Refinement Template Format

After generating 01b-iter/, create 02a-refine.md:

```markdown
# Refinement Instructions for Iteration 02

## AWAKEN Stage Feedback
### Post 1: [First few words...]
<!-- User comments here -->

## AGITATE Stage Feedback
### Post 1: [First few words...]
<!-- User comments here -->
### Post 2: [First few words...]
<!-- User comments here -->
[etc...]

## General Campaign Feedback
<!-- User comments here -->
```

## Posted URL Tracking Template

After final iteration, generate posted.txt:

```
# Campaign: [Campaign Name]
# Final iteration: [##b-iter/]
# Generated: [Date]

AWK1: [AWAITING URL]
AGI1: [AWAITING URL]
AGI2: [AWAITING URL]
[etc...]
```

Remember: This is a psychological journey design tool. Success depends on matching the right style to the right psychological moment in the audience's journey.