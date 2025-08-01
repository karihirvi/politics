# CLAUDE.md

The purpose of this repo is to provide a comprehensive system for creating effective political 
communication in the Finnish context, particularly for the Perussuomalaiset (PS) party. It includes 
insights from various experts in political communication, psychology, and cultural studies.

## Main Goal
To iteratively produce textual social media content that resonates with Finnish voters.

## Content Creation Process

The system supports two types of content creation:

### 1. Single Posts (Quick, One-off Content)

For quick responses to current events or single ideas that don't need a full campaign:

**Organization:**
- All single posts are created in the `posts` folder
- Each post topic gets its own folder: `p###-topic-name`
  - p = post
  - ### = Three-digit number (001, 002, etc.)
  - topic-name = User-chosen descriptive name (lowercase, hyphens)

**File Structure:**
- Follows the A-B iteration pattern:
  - **A files**: User instructions (e.g., `p001-01-a-instructions.md`)
  - **B files**: Claude's response (e.g., `p001-01-b-response.md`)
- Continue with 02-a, 02-b for refinements

**Example Structure:**
```
posts/
├── p001-burkakielto-jatko/
│   ├── p001-01-a-ohjeet.md
│   ├── p001-01-b-burkakielto-paastaustyyli.md
│   ├── p001-02-a-ohjeet.md
│   └── p001-02-b-muokattu-versio.md
```

### 2. Campaigns (Goal-Driven Multi-Stage Content)

For comprehensive messaging campaigns using the 5-stage psychological journey model from CLAUDE_GOAL_*.md:

**5-Stage Structure:**
1. **AWAKEN** - Create awareness (1-2 posts)
2. **AGITATE** - Generate emotional investment (3-5 posts)
3. **EDUCATE** - Provide framework (2-4 posts)
4. **ACTIVATE** - Channel into action (1-2 posts)
5. **INTEGRATE** - Embed into identity (ongoing)

**Organization:**
- All campaigns are created in the `campaigns` folder
- Each campaign gets its own folder: `c###-topic-name`
  - c = campaign
  - ### = Three-digit number (001, 002, etc.)
  - topic-name = User-chosen descriptive name (lowercase, hyphens)

**Iteration System:**
- User creates initial request: `01a-request.md`
- Claude generates full campaign in subfolder: `01b-iter/`
  - `1-awaken.md` - All AWAKEN stage posts
  - `2-agitate.md` - All AGITATE stage posts
  - `3-educate.md` - All EDUCATE stage posts
  - `4-activate.md` - All ACTIVATE stage posts
  - `5-integrate.md` - All INTEGRATE stage posts
- Claude auto-generates refinement template: `02a-refine.md`
- User adds feedback to refinement file
- Claude creates refined campaign in: `02b-iter/`
- Process continues with 03a, 03b, etc.

**Post Tracking:**
- After final iteration, Claude generates `posted.txt`
- Template includes all posts with placeholders for URLs
- User adds actual social media URLs after posting

**Example Structure:**
```
campaigns/
├── c001-wind-power/
│   ├── 00-plan.md (optional campaign strategy)
│   ├── 01a-request.md
│   ├── 01b-iter/
│   │   ├── 1-awaken.md
│   │   ├── 2-agitate.md
│   │   ├── 3-educate.md
│   │   ├── 4-activate.md
│   │   └── 5-integrate.md
│   ├── 02a-refine.md (auto-generated)
│   ├── 02b-iter/
│   │   └── ... (refined versions)
│   └── posted.txt (auto-generated after final iteration)
```

### Naming Convention Summary

**All lowercase throughout:**
- Posts: `p###-topic-name/`
- Campaigns: `c###-topic-name/`
- User files: end with `a` (e.g., `01a-request.md`, `p001-01-a-ohjeet.md`)
- Claude files: end with `b` (e.g., `01b-iter/`, `p001-01-b-response.md`)
- Topics: lowercase with hyphens (e.g., `stop-wind-power`, `burkakielto-jatko`)

VERY IMPORTANT:
- Choose single posts for quick, reactive content
- Choose campaigns for strategic, goal-driven messaging
- Always maintain consistent lowercase naming
- Never modify existing files - create new iterations

### Content Generation Guidelines

1. **When User Provides Instructions**
   - If constraints are unclear, ask for clarification
   - If multiple valid interpretations exist, provide multiple options
   - Reference background materials when instructed (party programs, framing techniques, style examples)

2. **Response Format**
   - For multiple options: Create all variations in a single B file, clearly separated
   - Use descriptive headers for each version
   - Keep Finnish text separate from English instructions/comments

## Background Information

For writing text, you can use background information and other resources:
- **party-programs** - contains official programs for various political parties
- **framing** - contains information about framing techniques
- **resources** - contains examples and other materials
- **style-examples** - contains selected examples of earlier posts, which you can use as inspiration or reference.
  The examples are selected due to their estimated effectiveness in Finnish political communication. They are numbered 
  for easy reference, e.g., e001-..., e002-..., etc. The prefix "e" stands for "example" for Claude to recognize 
  them easily. Posts from posts/ or campaigns/ folders may be lifted to this folder if they are considered particularly effective.

## Style and Goal Guides

### Style Guides
Two comprehensive style guides are available for creating effective political content:
- **CLAUDE_STYLE_FI.md** - Finnish language style guide with 7 distinct writing styles
- **CLAUDE_STYLE_EN.md** - English language style guide with the same 7 styles

### Goal-Based Strategy Guides
Two strategic guides for campaign planning:
- **CLAUDE_GOAL_FI.md** - Finnish guide for goal-driven campaign strategy
- **CLAUDE_GOAL_EN.md** - English guide for goal-driven campaign strategy

These guides explain the 5-stage psychological journey and how to map styles to campaign goals.

### How to Use the Guides
1. User describes their campaign goal
2. Claude identifies the goal type and recommends a strategic sequence
3. Claude maps appropriate styles to each stage (AWAKEN, AGITATE, etc.)
4. Content is created following both style characteristics and stage psychology
5. Example files (e###) serve as concrete references

### The 7 Political Communication Styles
1. **Paasaustyyli/Oratory** - Emotional, commanding, mobilizing
2. **Analyyttinen/Analytical** - Strategic, educational, legitimizing
3. **Konseptuaalinen/Conceptual** - Introduces new ideas and frameworks
4. **Argumentoiva/Argumentative** - Logical, refutes opposition
5. **Kriittis-poliittinen/Critical-Political** - Criticizes opponents, scandals
6. **Filosofis-uskonnollinen/Philosophical-Religious** - Values, meaning, tradition
7. **Populistinen/Populist** - Simple solutions, economic appeals

### Common Campaign Goal Types
- **Launch** - New movement or initiative
- **Policy** - Specific policy support
- **Oppose** - Build opposition movement
- **Crisis** - Manage crisis/maintain base
- **Convert** - Win new demographics
- **Defend** - Counter attacks
- **Mobilize** - Immediate action
- **Agenda** - Set public discourse
- **Values** - Reinforce identity
- **Recruit** - Grow membership

## Language Guidelines
- The language of the posts is **Finnish**, so you must write the posts in Finnish
- If you need help with Finnish, ask the user
- English is used for prompts and other instructions

## Key Reminders
- Follow the iterative process carefully
- Use version numbering consistently
- Keep the posts and campaigns folders organized
- Leverage background materials effectively
- Ensure messages resonate with the Finnish audience

## Technical details
Max line length: 120 characters
