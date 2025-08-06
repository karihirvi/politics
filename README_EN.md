# AI-powered Political Communication Design System

Practical tools for effective political communication in the Finnish context.

## What is this?

This is an AI-powered **optimization system** for political communication. Instead of relying on intuition alone, the system systematically optimizes messages toward defined goals. It's about transforming communication from intuition into a measurable process.

### Scientific Foundation

The optimization process leverages research from multiple fields, for example:
- **Cognitive linguistics**: How language shapes our thinking
- **Framing theory**: How metaphors and frames guide our understanding
- **Priming effect**: How repeated concepts change our worldview
- **Psychology of emotions**: How emotions affect decision-making

The system combines these research findings with AI optimization and continuously evolves through use.

### Optimization Process

The system works like this:

```
1. Human describes what they want to achieve
2. AI creates the first version of the message
3. Human reads the message
4. If human is satisfied → go to step 8
5. If human is not satisfied → give feedback
6. AI creates a new version based on feedback
7. Return to step 3
8. Message is ready and published
```

In short: Human and AI work on the message together round by round, until the result is satisfactory. Each round improves the message compared to the previous one. The human decides when the message is ready.



## How does it work?

### 1. Learning from examples - the foundation of the system
**IMPORTANT**: The system needs human-created examples to work well.

Learning materials can be found in:
- `tyyliesimerkit/` - Proven effective political messages
- `resurssit/oppaat/` - Communication guides and theoretical materials

Without these examples, the system cannot learn:
- Which word choices work in the Finnish context
- What rhythm and structure appeal to the target audience
- Which arguments are truly convincing

**The more quality examples, the better the system works.**

Based on source materials and user feedback, Claude creates new .md files that serve as additional guides and rules.

### 2. Seven different styles
Different situations require different communication:
- **Oratory style** - Emotional, imperative, mobilizing
- **Analytical** - Strategic, educational, legitimizing
- **Conceptual** - Introduces new ideas and frameworks
- **Argumentative** - Logical, refutes opposing claims
- **Critical-political** - Criticizes opponents, scandals
- **Philosophical-religious** - Values, meaning, traditions
- **Populist** - Simple solutions, economic appeals

### 3. Step-by-step refinement
Messages are created in stages:
1. First version
2. Feedback and improvements
3. Polished result

## Practical example

**Goal:** You want to criticize energy policy

**Process:**
1. Choose a style (e.g., populist)
2. System creates first version
3. You give feedback ("add more specifics")
4. You get a refined version

**Result:** A message that effectively speaks to your target audience

## Repository structure

```
postaukset/        # Finished messages by topic
tyyliesimerkit/    # Proven effective examples  
resurssit/         # Support materials (phrases, narratives, framing)
  oppaat/          # PDF guides and theoretical materials
nyanssit/          # Materials for learning subtle nuances
puolueohjelmat/    # Official party programs
CLAUDE_*.md        # Detailed system instructions
```

## Getting started

1. **Define your goal** - What do you want to achieve?
2. **Choose a style** - Which fits the situation?
3. **Create first version** - The system helps
4. **Refine step by step** - Improve based on feedback

## System strengths

✅ **Works well:**
- Creating individual messages
- Managing different styles
- Optimizing word choices
- Building arguments

❌ **Limitations:**
- Long campaigns require human guidance
- Consistency across multiple messages is challenging

## Why is this important?

Political communication is no longer just intuition. By understanding how language affects thinking, we can:
- Create more effective messages
- Reach people better
- Advance political goals

## Technical implementation

The system uses Claude AI to help create messages.

Key instructions:
- **CLAUDE.md** - System overview and workflow
- **CLAUDE_TYYLI.md** - 7 different writing styles
- **CLAUDE_POSTAUS.md** - Guide for writing individual posts
- **CLAUDE_TAVOITE.md** - Guide for choosing the right style
- **CLAUDE_SYNTAKSI.md**, **CLAUDE_RETORIIKKA.md**, **CLAUDE_SANASTO.md** - Fine-grained constraints

**Note:** Using this system requires Claude Code.

---

*This tool combines human creativity and machine efficiency to create impactful political communication.*