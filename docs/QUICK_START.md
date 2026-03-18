# Quick Start Guide

Get up and running with **json-to-markdown-tools** in minutes.

## Installation

1. **Clone or download the tools**
   ```bash
   git clone https://github.com/geo-x/json-to-markdown-tools.git
   cd json-to-markdown-tools
   ```

2. **Make executable (optional but recommended)**
   ```bash
   chmod +x bin/chat-trim-tool.py
   chmod +x bin/chat-trim-gui.py
   ```

3. **Export your VS Code Copilot chat**
   - In VS Code, right-click on a chat session
   - Select "Export Chat"
   - Save as JSON

## First Run: CLI

```bash
# Basic usage: Split chat into daily markdown files
python3 bin/chat-trim-tool.py /path/to/chat.json --start "2026-03-12" --split-by-day

# Output appears in: same directory as chat.json
# Structure: 2026-03/12.md, 2026-03/13.md, etc.
```

## First Run: GUI

```bash
# macOS (system Python)
python3 bin/chat-trim-gui.py

# macOS (Homebrew Python - recommended)
python3.11 bin/chat-trim-gui.py

# Linux/Windows
python3 bin/chat-trim-gui.py
```

Then click through:
1. **Select JSON File** → Choose your exported chat
2. **Set Dates** → Pick start and end dates
3. **Split by Day?** → Check if you want daily organization
4. **Process Chat** → Wait for completion
5. **View Results** → Check output directory

## Common Tasks

### Task 1: Filter to Last Week and Save as Markdown

```bash
python3 bin/chat-trim-tool.py "chat.json" \
  --start "2026-03-11" \
  --end "2026-03-18" \
  --format markdown
```

### Task 2: Archive Entire Chat into Daily Files

```bash
python3 bin/chat-trim-tool.py "chat.json" --split-by-day
```

Your output: `YYYY-MM/DD.md` structure ready for searching

### Task 3: Preserve Original JSON with Date Filter

```bash
python3 bin/chat-trim-tool.py "chat.json" \
  --start "2026-01-01" \
  --end "2026-03-18" \
  --format json
```

### Task 4: Both Formats (JSON + Markdown)

```bash
python3 bin/chat-trim-tool.py "chat.json" \
  --start "2026-03-01" \
  --format both \
  --split-by-day
```

Creates daily files for both formats:
```
2026-03/01.json
2026-03/01.md
2026-03/02.json
2026-03/02.md
...
```

## What You Get

Each markdown file includes:
- ✅ User questions with timestamps
- ✅ Assistant responses with complete content
- ✅ All thinking/reasoning blocks (labeled)
- ✅ Code snippets with syntax highlighting
- ✅ Filenames and programming languages
- ✅ Full conversation context

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Command not found | Make sure you're in the repo directory or prefix with `python3` |
| GUI won't open | Try: `python3.11 bin/chat-trim-gui.py` (Homebrew Python on macOS) |
| Files not found after running | Check output directory; defaults to input file's directory |
| Date format error | Use YYYY-MM-DD format exactly (e.g., 2026-03-12) |

## Next Steps

- Read [USAGE.md](USAGE.md) for advanced options
- Check [USE_CASES.md](USE_CASES.md) for real-world examples
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed help
- Visit [INSTALLATION.md](INSTALLATION.md) for platform-specific setup

---

Ready to split some chats? Run your first command above! 🚀
