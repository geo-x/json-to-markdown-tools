# JSON to Markdown Tools

Convert VS Code Copilot chat JSON exports to markdown and filter by date range. Perfect for organizing, archiving, and sharing your AI conversation history.

## Features

✨ **Smart Content Extraction**
- Preserves thinking/reasoning blocks from Claude
- Extracts code snippets with filename and language info
- Handles both `text` and `parts` message formats
- Complete fidelity—no content left behind

📅 **Flexible Date Filtering**
- Filter by date range (start/end dates)
- Optional start date (defaults to earliest message)
- Precise YYYY-MM-DD format validation

🎨 **Customizable Output Styling**
- **5 style options**: None, Emoji, Block, Box, Color
- **Color customization**: Use any CSS color or hex value
- **HTML support**: Compatible with web-based documentation platforms
- See [Styling Guide](docs/STYLING.md) for examples

📂 **Multiple Export Options**
- **JSON**: Filtered original structure
- **Markdown**: Professional formatting with timestamps and metadata
- **Split by Day**: Organize into daily files (YYYY-MM/DD.format)
- **Combined**: Single file with all messages

🖥️ **Dual Interface**
- **CLI**: `chat-trim-tool.py` — Command-line for automation and scripting
- **GUI**: `chat-trim-gui.py` — Visual interface for non-technical users

## Quick Start

### CLI (Command Line)

```bash
# Split chat into daily markdown files, starting March 12
python3 chat-trim-tool.py "chat.json" --start "2026-03-12" --format markdown --split-by-day

# Filter and save as JSON
python3 chat-trim-tool.py "chat.json" --start "2026-03-01" --end "2026-03-18" --format json

# Export with emoji styling
python3 chat-trim-tool.py "chat.json" --user-style emoji --format markdown

# Export with colored HTML styling
python3 chat-trim-tool.py "chat.json" --user-style color --style-color blue --format markdown
```

### GUI (Graphical Interface)

```bash
# On macOS, use Homebrew Python for best results
python3 chat-trim-gui.py
```

Then:
1. Click "Select JSON File" and choose your chat export
2. Set start and end dates
3. Choose export format (JSON, Markdown, or Both)
4. Check "Split by day" to organize into daily files
5. Click "Process Chat" and watch the magic happen

## Installation

No external dependencies required—uses only Python standard library.

```bash
# Make scripts executable
chmod +x chat-trim-tool.py chat-trim-gui.py

# Optional: Add to your PATH
cp chat-trim-tool.py /usr/local/bin/
cp chat-trim-gui.py /usr/local/bin/
```

### macOS GUI Note

System Python's Tkinter is outdated. For best GUI experience, install Homebrew Python:

```bash
brew install python-tk@3.11
python3.11 chat-trim-gui.py
```

## Output Structure

### Split by Day

```
output/
├── 2026-03/
│   ├── 01.md
│   ├── 02.md
│   └── 03.md
└── 2026-04/
    └── 01.md
```

### Combined Export

```
output.md          # All messages in single file
output.json        # Filtered JSON structure
```

## What Gets Preserved

✅ All thinking/reasoning blocks (marked as **Reasoning:**)
✅ Code snippets with syntax highlighting (includes filename and language)
✅ Message timestamps and metadata
✅ Complete response content and context
✅ User queries and full conversation flow

## Examples

### Use Case: Archive Important Chat Sessions

Filter and organize years of chats into daily markdown files for easy searching:

```bash
python3 chat-trim-tool.py "2024-copilot.json" --split-by-day --format markdown
# Creates: 2024-01/01.md, 2024-01/02.md, ... 2024-12/31.md
```

### Use Case: Share Chat History

Extract a specific date range to share with teammates:

```bash
python3 chat-trim-tool.py "project-chat.json" \
  --start "2026-03-01" \
  --end "2026-03-15" \
  --format markdown \
  --output "march-discussion.md"
```

### Use Case: Code Extraction

All code blocks are preserved with full context—perfect for learning or documentation:

```bash
# Code and reasoning blocks both included
python3 chat-trim-tool.py "solutions.json" --format markdown
```

## Troubleshooting

**Blank GUI window on macOS?**
- Install Homebrew Python: `brew install python-tk@3.11`
- Run with: `python3.11 chat-trim-gui.py`

**Large file size discrepancy?**
- That's normal! Original JSON is typically much larger
- Markdown is more human-readable but more compact for text-only content
- Use `--format json --split-by-day` to preserve original structure

**Files not where expected?**
- Default output: same directory as input file
- Customize with `--output /path/to/directory`

## Command Reference

```
chat-trim-tool.py FILE [OPTIONS]

OPTIONS:
  --start DATE           Start date (YYYY-MM-DD), optional, defaults to earliest
  --end DATE             End date (YYYY-MM-DD), optional
  --format FORMAT        Output format: json, markdown, or both (default: markdown)
  --split-by-day         Organize output into daily files (YYYY-MM/DD.format)
  --output DIR           Output directory (default: same as input)
  --help                 Show this help message
```

## License

MIT License — Use freely in personal and commercial projects.

## Contributing

Found a bug or have a feature request? Feel free to improve this tool!

---

**Made with ❤️ by [geo-x](https://github.com/geo-x)**
