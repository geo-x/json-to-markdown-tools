# Installation Guide

Get **json-to-markdown-tools** set up and ready to use.

## System Requirements

- **Python**: 3.7 or higher
- **OS**: macOS, Linux, or Windows
- **Disk Space**: ~50 MB free for tools
- **Libraries**: None required (uses Python standard library only)

## Check Python Version

```bash
python3 --version
```

You should see `Python 3.7.x` or newer. If not:

- **macOS**: `brew install python-tk@3.11`
- **Linux**: `sudo apt-get install python3`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

## Installation Methods

### Method 1: Clone from GitHub (Recommended)

```bash
git clone https://github.com/geo-x/json-to-markdown-tools.git
cd json-to-markdown-tools

# Make scripts executable
chmod +x bin/chat-trim-tool.py
chmod +x bin/chat-trim-gui.py

# Test installation
python3 bin/chat-trim-tool.py --help
```

### Method 2: Download ZIP

1. Visit [github.com/geo-x/json-to-markdown-tools](https://github.com/geo-x/json-to-markdown-tools)
2. Click **Code** → **Download ZIP**
3. Extract to desired location
4. Make executable:
   ```bash
   chmod +x bin/chat-trim-tool.py bin/chat-trim-gui.py
   ```

---

## Platform-Specific Setup

### macOS

#### CLI (Works out of the box)
```bash
python3 bin/chat-trim-tool.py /path/to/chat.json --split-by-day
```

#### GUI with Homebrew Python (Recommended)
```bash
# Install Python with modern Tkinter
brew install python-tk@3.11

# Run GUI with Homebrew Python
python3.11 bin/chat-trim-gui.py
```

---

### Linux (Ubuntu/Debian)

```bash
# Install Python and Tkinter
sudo apt-get update
sudo apt-get install python3 python3-tk

# Clone repo
git clone https://github.com/geo-x/json-to-markdown-tools.git
cd json-to-markdown-tools

# Make executable
chmod +x bin/chat-trim-tool.py bin/chat-trim-gui.py

# Run CLI
python3 bin/chat-trim-tool.py --help

# Run GUI
python3 bin/chat-trim-gui.py
```

---

### Windows

#### Using PowerShell

```powershell
# Install Python (if not already installed)
# Download from python.org or use Windows Store

# Clone repo
git clone https://github.com/geo-x/json-to-markdown-tools.git
cd json-to-markdown-tools

# Run CLI
python bin\chat-trim-tool.py --help

# Run GUI
python bin\chat-trim-gui.py
```

---

## Verify Installation

```bash
# Test CLI
python3 bin/chat-trim-tool.py --help

# Should display usage information

# Test GUI (if applicable)
python3 bin/chat-trim-gui.py
# Should open window with buttons and fields
```

---

## Troubleshooting Installation

### "Python3 Not Found"

**macOS**:
```bash
brew install python3
```

**Linux (Ubuntu)**:
```bash
sudo apt-get install python3
```

**Windows**:
- Download from https://www.python.org/downloads/
- During install, check "Add Python to PATH"

### "No Module Named Tkinter"

**macOS (use Homebrew Python)**:
```bash
brew install python-tk@3.11
python3.11 bin/chat-trim-gui.py
```

**Linux (Ubuntu)**:
```bash
sudo apt-get install python3-tk
```

**Windows**:
- Re-run Python installer
- Select "tcl/tk and IDLE"

---

## Next Steps

1. **Get Started**: Read [QUICK_START.md](../docs/QUICK_START.md)
2. **Learn Commands**: Check [USAGE.md](../docs/USAGE.md)
3. **See Examples**: Browse [USE_CASES.md](../docs/USE_CASES.md)
4. **Troubleshoot**: Visit [TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md)

---

**Ready? Run your first command:**

```bash
python3 bin/chat-trim-tool.py ~/Downloads/chat.json --split-by-day
```

🚀
