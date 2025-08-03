# CLAUDE.md

The purpose of this repo is to provide a comprehensive system for creating effective political 
communication in the Finnish context, particularly for the Perussuomalaiset (PS) party. It includes 
insights from various experts in political communication, psychology, and cultural studies.

## Main Goal
To iteratively produce textual social media content that resonates with Finnish voters.

## Content Creation Process

The system creates effective single posts for social media:

**Organization:**
- All posts are created in the `posts` folder
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

### Naming Convention

**All lowercase throughout:**
- Post folders: `p###-topic-name/`
- Files inside: `p###-##-a-description.md` and `p###-##-b-description.md`
  - `p###` = Post number (e.g., p001, p002)
  - `##` = Iteration number (01, 02, 03...)
  - `a` = User-created content (requests, feedback)
  - `b` = Claude-generated content (responses)
  - `description` = Brief description of content
- Topics: lowercase with hyphens (e.g., `burkakielto-jatko`)

VERY IMPORTANT:
- Always maintain consistent lowercase naming
- Never modify existing files - create new iterations
- **Current Version Rule**: The latest generated file (highest number) is the active version
  - E.g., if both p001-01-b and p001-02-b exist, use p001-02-b
  - User will explicitly mention any exceptions to this rule

### Content Generation Guidelines

1. **When Creating a New Post**
   - Automatically create the first request template: `p###-01-a-request.md`
   - Use the standard template with sections for Goal, Style, Length, Key Points, etc.
   - This saves the user time and ensures consistent structure

2. **When User Says "käsittele"**
   - Process the request file to generate response
   - **IMPORTANT**: Automatically create the next feedback template after generating response
   - This ensures smooth iteration workflow

3. **When User Provides Other Instructions**
   - If constraints are unclear, ask for clarification
   - If multiple valid interpretations exist, provide multiple options
   - Reference background materials when instructed (party programs, framing techniques, style examples)

4. **Response Format**
   - For multiple options: Create all variations in a single B file, clearly separated
   - Use descriptive headers for each version
   - Keep Finnish text separate from English instructions/comments

5. **Feedback Processing**
   - **CRITICAL**: When user provides feedback on any part, apply it globally
   - If user corrects a spelling (e.g., "burkkaa" → "burkaa"), fix it everywhere
   - If user suggests a tone change in one post, consider if it applies to others
   - If user mentions missing context, add context to ALL posts, not just the commented one
   - Always think: "Does this feedback apply elsewhere?"

### Workflow Example

**Step 1: User creates request file**
```
posts/p002-tuulivoimakritiikin/p002-01-a-request.md:

# Request: Wind Power Criticism Post

Goal: Expose the hidden costs of wind power subsidies
Style: Analyyttinen (Analytical) - I want to build credibility with facts
Length: MEDIUM (5-6 paragraphs)
Key points:
- Taxpayer burden
- Unreliability of wind power
- Impact on electricity prices

Please include credible sources (remember: no Wikipedia)
```

**Step 2: Claude generates response**
```
posts/p002-tuulivoimakritiikin/p002-01-b-tuulivoiman-todelliset-kustannukset.md:

# Tuulivoiman todelliset kustannukset paljastuvat

[Analytical style post with 5-6 paragraphs, facts, sources...]

Lähteet:
1. Energiavirasto (2023): https://energiavirasto.fi/...
2. VTT:n tutkimus (2024): https://www.vtt.fi/...
```

**Step 3: User provides feedback**
```
posts/p002-tuulivoimakritiikin/p002-02-a-feedback.md:

Good start, but:
- Add more emotional hook in opening
- Include comparison to nuclear power costs
- Tone is too academic, make it more accessible
```

**Step 4: Claude creates refined version**
```
posts/p002-tuulivoimakritiikin/p002-02-b-tuulivoiman-piilotetut-kulut.md:

[Refined version incorporating all feedback]
```

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

### Style Selection Guides
Two guides for choosing the right style for your posts:
- **CLAUDE_GOAL_FI.md** - Finnish guide for style selection
- **CLAUDE_GOAL_EN.md** - English guide for style selection

These guides help you choose the most effective style for your communication goal.

### Fine-Grained Constraint Documents
Three levels of detailed constraints for optimizing content generation:

#### Syntactic Constraints
- **CLAUDE_SYNTAX_FI.md** - Grammatical constraints per style (sentence types, lengths, structures)
- **CLAUDE_SYNTAX_EN.md** - English version of syntactic constraints

#### Rhetorical Constraints
- **CLAUDE_RHETORIC_FI.md** - Argumentation structures and rhetorical devices per style
- **CLAUDE_RHETORIC_EN.md** - English version of rhetorical constraints

#### Lexical Constraints
- **CLAUDE_LEXICON_FI.md** - Vocabulary, registers, and phraseology per style
- **CLAUDE_LEXICON_EN.md** - English version of lexical constraints

### Post Writing Guides
Detailed instructions for individual post creation:
- **CLAUDE_POST_FI.md** - Finnish guide for writing individual posts
- **CLAUDE_POST_EN.md** - English guide for writing individual posts

### How to Use the Guides
1. User describes their communication goal
2. Claude identifies the most appropriate style(s)
3. Content is created following style characteristics
4. Example files (e###) serve as concrete references

### The 7 Political Communication Styles
1. **Paasaustyyli/Oratory** - Emotional, commanding, mobilizing
2. **Analyyttinen/Analytical** - Strategic, educational, legitimizing
3. **Konseptuaalinen/Conceptual** - Introduces new ideas and frameworks
4. **Argumentoiva/Argumentative** - Logical, refutes opposition
5. **Kriittis-poliittinen/Critical-Political** - Criticizes opponents, scandals
6. **Filosofis-uskonnollinen/Philosophical-Religious** - Values, meaning, tradition
7. **Populistinen/Populist** - Simple solutions, economic appeals


## Language Guidelines
- The language of the posts is **Finnish**, so you must write the posts in Finnish
- If you need help with Finnish, ask the user
- English is used for prompts and other instructions
- NEVER use hashtags in posts
- For post length guidance, refer to style-examples for typical lengths

## Source and Reference Guidelines
- **ALL references must be URLs**: Never use vague citations like "Study shows" or "Report says"
- **Language requirement**: Sources must be in Finnish or English only
- **Credibility requirement**: 
  - Never use Wikipedia as a source
  - Only use generally credible sources like:
    - Government websites (.gov, .fi ministries)
    - Established news organizations (YLE, HS, BBC, Reuters)
    - Academic institutions and research institutes
    - Official NGO and international organization websites
    - Peer-reviewed journals and official reports
- **Format**: EACH POST must have its own source list
  - Place all references at the END of EACH individual post
  - Use brackets [1] or parentheses (1) in text to mark citations
  - Never use superscript or subscript numbers
  - List full URLs at the bottom under "Lähteet:" or "Viitteet:"
  - Never share source lists between posts - each post is self-contained
- **IMPORTANT**: When generating content with URLs, use WebFetch to verify links work
  - If URL doesn't work, find alternative sources
  - Never include broken or fictional URLs
- **Example format**:
  ```
  Ranskan sisäministeriön mukaan [1] burkakielto on vähentänyt turvallisuusongelmia.
  
  Lähteet:
  1. Ranskan sisäministeriön raportti (2019): https://www.interieur.gouv.fr/...
  ```

## Key Reminders
- Follow the iterative process carefully
- Use version numbering consistently
- Keep the posts folder organized
- Leverage background materials effectively
- Ensure messages resonate with the Finnish audience

## Technical details
- Max line length: 120 characters
- **Markdown formatting**: Always use proper markdown syntax
  - Lists must use `-` or `*` at the beginning of each item
  - Bold text with `**text**`
  - Headers with appropriate `#` levels
  - Proper line breaks between sections
