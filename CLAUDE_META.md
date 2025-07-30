# CLAUDE_META.md

This file contains meta-instructions for Claude to generate and maintain the CLAUDE.md file.

## Instructions for Generating CLAUDE.md

When asked to create or update CLAUDE.md, use the following information:

### Purpose Statement
The repo provides a comprehensive system for creating effective political communication in the Finnish context, particularly for the Perussuomalaiset (PS) party. It includes insights from various experts in political communication, psychology, and cultural studies.

### Main Goal
The system should iteratively produce textual social media content that resonates with Finnish voters.

### Process Description
The CLAUDE.md should describe this workflow:

1. User writes the start of the text in a file. At the end of the text, the user asks for ideas how to continue and/or describes the idea of the post. Claude should consider the idea description as constraints within which to generate how the text should continue. 
   - If constraints are not specific enough, Claude should ask for clarification. 
   - If constraints are specific enough but allow multiple interpretations, Claude should provide multiple options for how to continue the text.

2. Once Claude has figured out what to generate, it writes the continuation of the text to a new file with a running version number in the filename, e.g., 01-..., 02-..., etc. Two numbers are enough.

3. All work happens in workspace folder. Iterating each text is done in subfolders named with the post idea. The user decides the subfolder name. Subfolder names start with a number 001-, 002-, etc. to keep the order. Use three digits.

### Background Resources
The CLAUDE.md should reference these folders:
- party_programs - contains official programs for various political parties
- framing - contains information about framing techniques
- resources - contains examples and other materials

### Language Requirements
- The language of the posts is Finnish, so Claude must write the posts in Finnish
- If Claude needs help with Finnish, it should ask the user
- English is used for prompts and other instructions

## Meta-Notes
- This file (CLAUDE_META.md) should NOT be referenced in CLAUDE.md
- CLAUDE.md should be written as a clear, standalone document for the project
- Keep CLAUDE.md concise and practical


## Technical details
Max line length: 120 characters
