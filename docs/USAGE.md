# Usage Guide

Comprehensive reference for **json-to-markdown-tools**.

## Command Line Interface

### Basic Syntax

```bash
python3 chat-trim-tool.py FILE [OPTIONS]
```

### Arguments

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `FILE` | path | Yes | — | Path to VS Code Copilot chat JSON export |
| `--start` | date | No | Earliest message | Start date in YYYY-MM-DD format |
| `--end` | date | No | Latest message | End date in YYYY-MM-DD format |
| `--format` | text | No | markdown | Output format: `json`, `markdown`, or `both` |
| `--split-by-day` | flag | No | False | Split output into daily files (YYYY-MM/DD.format) |
| `--output` | path | No | Input directory | Where to save processed files |
| `--user-style` | text | No | none | Styling option: `none`, `emoji`, `block`, `box`, or `color` |
| `--style-color` | text | No | green | CSS color for styled output (e.g., `blue`, `#FF0000`) |
| `--help` | flag | No | — | Show help message |

### Output Format Details

#### Format: `markdown`
Creates human-readable markdown files with:
- Timestamps for each message pair
- User query formatted as **User:**
- Assistant response with all content
- Thinking blocks as **Reasoning:**
- Code blocks with syntax highlighting
- Metadata and context

**File extension**: `.md`

#### Format: `json`
Preserves original VS Code Copilot JSON structure with filtered date range.
- Maintains all metadata
- Includes full response array
- Original message structure intact

**File extension**: `.json`

#### Format: `both`
Generates both markdown AND json for the same date range.

**File extensions**: `.md` and `.json`

### Split by Day

When `--split-by-day` flag is used:
- Files organized into folders: `YYYY-MM/`
- Individual files named: `DD.{format}`
- One day per file, chronologically ordered

**Example structure**:
```
output/
├── 2026-03/
│   ├── 12.md
│   ├── 13.md
│   └── 14.md
└── 2026-04/
    └── 01.md
```

### Output Directory

- **Default**: Same directory as input JSON file
- **Custom**: Use `--output /path/to/directory`

The directory is created if it doesn't exist.

### Output Styling

Customize how user and assistant messages appear in your markdown output:

#### Style Options

- **`none`** (default): Simple bold formatting
- **`emoji`**: Adds 👤 and 🤖 emoji icons  
- **`block`**: Blockquote-style indentation with `>`
- **`box`**: Unicode box borders around messages
- **`color`**: HTML span tags with CSS colors

#### Color Options

Any CSS color value is supported:
- Named colors: `blue`, `red`, `green`, `purple`, `darkgreen`, etc.
- Hex colors: `#FF0000`, `#00FF00`, etc.
- RGB format: `rgb(255, 0, 0)` (for HTML contexts)

See the [Styling Guide](STYLING.md) for detailed examples of each style.

## Examples

### Example 1: Filter Last Month, Split by Day

```bash
python3 chat-trim-tool.py "2026-copilot-export.json" \
  --start "2026-02-18" \
  --end "2026-03-18" \
  --split-by-day \
  --format markdown
```

**Result**:
```
2026-02/18.md
2026-02/19.md
...
2026-03/18.md
```

### Example 2: Extract Single Day

```bash
python3 chat-trim-tool.py "chat.json" \
  --start "2026-03-15" \
  --end "2026-03-15" \
  --format markdown
```

**Result**: One markdown file with all messages from March 15

### Example 3: Preserve Complete JSON, No Date Filter

```bash
python3 chat-trim-tool.py "chat.json" --format json
```

**Result**: Entire chat as filtered JSON (same if no dates specified)

### Example 4: Archive with Both Formats

```bash
python3 chat-trim-tool.py "big-chat.json" \
  --start "2026-01-01" \
  --format both \
  --split-by-day \
  --output ~/Chat-Archive/
```

**Result**:
```
~/Chat-Archive/
├── 2026-01/
│   ├── 01.md
│   ├── 01.json
│   └── ...
└── 2026-12/
    └── 25.md
```

### Example 5: Export with Emoji Styling

```bash
python3 chat-trim-tool.py "chat.json" \
  --start "2026-03-10" \
  --user-style emoji \
  --format markdown
```

**Output includes**: 👤 User and 🤖 Assistant labels with emoji icons

### Example 6: Professional Documentation with Block Style

```bash
python3 chat-trim-tool.py "project-chat.json" \
  --user-style block \
  --format markdown \
  --split-by-day
```

**Output**: Conversation formatted as blockquotes, ideal for documentation

### Example 7: Colored Web Export

```bash
python3 chat-trim-tool.py "chat.json" \
  --user-style color \
  --style-color "#2E86AB" \
  --format markdown \
  --output ~/Web-Docs/
```

**Output**: HTML-styled color spans compatible with GitHub Pages, Notion, etc.
~/Chat-Archive/
├── 2026-01/
│   ├── 01.json
│   ├── 01.md
│   ├── 02.json
│   └── 02.md
└── ...
```

### Example 5: Prepare for Sharing (Specific Date Range)

```bash
python3 chat-trim-tool.py "project-chat.json" \
  --start "2026-03-10" \
  --end "2026-03-15" \
  --format markdown \
  --output ~/Share/
```

**Result**: Clean markdown file containing only March 10-15 discussion

## Date Format

Dates must be in **YYYY-MM-DD** format:
- ✅ `2026-03-12`
- ✅ `2026-01-01`
- ❌ `03-12-2026`
- ❌ `12/03/2026`
- ❌ `March 12, 2026`

## Content Preserved

### Always Included
- ✅ User messages (questions, context)
- ✅ Assistant responses (complete text)
- ✅ Thinking/reasoning blocks (internal reasoning)
- ✅ Code snippets (with language and filename)
- ✅ Timestamps (for each message pair)
- ✅ Message count and metadata

### Complete Preservation
- No content trimmed or simplified
- All metadata maintained
- Code blocks extracted with full formatting

## Advanced Tips

### Batch Processing

Create a script to process multiple chats:
```bash
#!/bin/bash
for chat in ~/chats/*.json; do
  python3 chat-trim-tool.py "$chat" --split-by-day
done
```

### Search Generated Files

```bash
# Find all markdown files mentioning "player"
grep -r "player" output/ --include="*.md"

# Count code blocks by language
grep -r "^\`\`\`" output/ --include="*.md" | cut -d: -f2 | sort | uniq -c
```

---

For more examples, see [USE_CASES.md](USE_CASES.md).
