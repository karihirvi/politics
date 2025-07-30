# CLAUDE.md

The purpose of this repo is to provide a comprehensive system for creating effective political 
communication in the Finnish context, particularly for the Perussuomalaiset (PS) party. It includes 
insights from various experts in political communication, psychology, and cultural studies.

## Main Goal
To iteratively produce textual social media content that resonates with Finnish voters.

## Post Writing Process

### File Structure and Naming Convention

1. **Workspace Organization**
   - All work happens in the `workspace` folder
   - Each post topic gets its own subfolder named: `W-XXX-topic-name`
     - W = Workspace
     - XXX = Three-digit number (001, 002, etc.)
     - topic-name = User-chosen descriptive name

2. **A-B File Pairing System**
   - Each iteration consists of an A-B file pair:
     - **A files**: Written by user, containing instructions/prompts
     - **B files**: Written by Claude, containing the response/generated text
   - File naming pattern: `W-XXX-YY-[A/B]-description.md`
     - XXX = Workspace number (matches folder)
     - YY = Two-digit iteration number (01, 02, etc.)
     - A/B = File type (A for user, B for Claude)
     - description = Brief descriptor of content

3. **Iteration Process**
   - User creates `W-001-01-A-instructions.md` with initial text and instructions
   - Claude creates `W-001-01-B-response.md` with generated content
   - User creates `W-001-02-A-refinement.md` referencing the previous B file
   - Claude creates `W-001-02-B-refined.md` with updated content
   - Process continues until desired result is achieved

VERY IMPORTANT: When processing A files, follow this exact pattern:
   - When you process a W-XXX-YY-A file, you must create a corresponding W-XXX-YY-B file (same iteration number)
   - Example: If processing `W-001-02-A-instructions.md`, create `W-001-02-B-response.md`
   - NEVER modify existing files in the workspace folder
   - NEVER increment the iteration number yourself - that's the user's job
   - The A-B pairing means: A file (user) → B file (Claude) with the SAME iteration number

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
- **party_programs** - contains official programs for various political parties
- **framing** - contains information about framing techniques
- **resources** - contains examples and other materials
- **style_examples** - contains selected examples of earlier posts, which you can use as inspiration or reference.
  The examples are selected due to their estimated effectiveness in Finnish political communication. They are numbered 
  for easy reference, e.g., E-001-..., E-002-..., etc. The prefix "E-" stands for "example" for Claude to recognize 
  them easily. Posts from workspace folders may be lifted to this folder if they are considered particularly effective.

## Language Guidelines
- The language of the posts is **Finnish**, so you must write the posts in Finnish
- If you need help with Finnish, ask the user
- English is used for prompts and other instructions

## Key Reminders
- Follow the iterative process carefully
- Use version numbering consistently
- Keep the workspace folder organized
- Leverage background materials effectively
- Ensure messages resonate with the Finnish audience

## Technical details
Max line length: 120 characters
