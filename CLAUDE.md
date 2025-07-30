# CLAUDE.md

The purpose of this repo is to provide a comprehensive system for creating effective political 
communication in the Finnish context, particularly for the Perussuomalaiset (PS) party. It includes 
insights from various experts in political communication, psychology, and cultural studies.

## Main Goal
To iteratively produce textual social media content that resonates with Finnish voters.

## Post Writing Process

1. **User writes the start of the text in a file.** At the end of the text, the user asks for ideas 
   on how to continue and/or describes the idea of the post. Claude should consider the idea 
   description as constraints within which to generate how the text should continue.
   - If constraints are not specific enough, Claude should ask for clarification.
   - If constraints are specific enough but allow multiple interpretations, Claude should provide 
     multiple options for how to continue the text.
   - Instructions may refer to background information, such as party programs, framing techniques, 
     or examples from previous posts.

2. **Once Claude has figured out what to generate,** it writes the continuation of the text to a new 
   file with a running version number in the filename, e.g., 01-..., 02-..., etc. Two numbers are 
   enough.

3. **All work happens in the workspace folder.** Iterating each text is done in subfolders named 
   with the post idea. The user decides the subfolder name. Subfolder names start with a number 
   001-, 002-, etc. to keep the order. Use three digits.

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
