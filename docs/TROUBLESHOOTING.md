# Troubleshooting Guide

Solutions for common issues with **json-to-markdown-tools**.

## macOS GUI Issues

### Issue: Blank Window on macOS

**Symptoms**:
- GUI starts but shows empty window
- Warning about deprecated Tkinter
- Window appears in dock but nothing visible

**Root Cause**: System Python has outdated Tkinter.

**Solution (Recommended)**:

```bash
# Install Python with working Tkinter using Homebrew
brew install python-tk@3.11

# Run GUI with Homebrew Python
python3.11 bin/chat-trim-gui.py
```

---

## Date Format Errors

### Issue: Invalid Date Error

**Error Message**:
```
Error: Invalid date format. Please use YYYY-MM-DD (e.g., 2026-03-18)
```

**Common Mistakes**:
- ❌ `03-18-2026` (wrong order)
- ❌ `18/03/2026` (different separator)
- ❌ `March 18, 2026` (spelled out)
- ❌ `2026-3-18` (missing leading zero)

**Solution**: Use exactly **YYYY-MM-DD** format:
- ✅ `2026-03-18`
- ✅ `2026-12-31`
- ✅ `2026-01-01`

---

## File Not Found Errors

### Issue: "Cannot Find File" or "File Not Found"

**Causes**:
1. File path typo
2. File doesn't exist at specified location
3. File permissions issue
4. Path has spaces (not wrapped in quotes)

**Solutions**:

```bash
# Verify file exists
ls -la "/path/to/chat.json"

# Use quotes for paths with spaces
python3 bin/chat-trim-tool.py "/path/to/Big Chat Export.json"

# Use absolute paths if possible
python3 bin/chat-trim-tool.py "$HOME/Downloads/chat.json"
```

---

## Output Directory Issues

### Issue: Files Not Found After Processing

**Problem**: Script runs but you can't find the output.

**Explanation**: By default, output goes in the **same directory as the input file**.

**Solution**:

```bash
# Files saved to input file's directory
python3 bin/chat-trim-tool.py ~/Downloads/chat.json

# Output: ~/Downloads/2026-03/ (for split-by-day)

# Override with --output flag if needed
python3 bin/chat-trim-tool.py ~/Downloads/chat.json --output ~/Desktop/
```

---

## Processing Issues

### Issue: "Permission Denied" When Writing Files

**Error**:
```
Permission denied: Cannot write to output directory
```

**Solutions**:

```bash
# Check directory permissions
ls -ld ~/output-dir/

# Make directory writable
chmod u+w ~/output-dir/

# Or use a different directory
python3 bin/chat-trim-tool.py chat.json --output ~/Desktop/
```

---

### Issue: "End Date Before Start Date"

**Error**:
```
Error: Start date must be before end date
```

**Example of wrong**:
```bash
python3 bin/chat-trim-tool.py chat.json \
  --start "2026-03-15" \
  --end "2026-03-10"  # This is before start!
```

**Fix**:
```bash
python3 bin/chat-trim-tool.py chat.json \
  --start "2026-03-10" \
  --end "2026-03-15"  # End after start
```

---

## Large File Issues

### Issue: Script Takes Too Long / Hangs

**Causes**:
- Very large files (1GB+)
- System running out of memory
- Slow disk I/O

**Solutions**:

```bash
# Try with smaller date range
python3 bin/chat-trim-tool.py huge-chat.json \
  --start "2026-03-01" \
  --end "2026-03-07"  # Smaller slice
```

---

## Windows-Specific Issues

### Issue: "Python Command Not Found"

**Solutions**:

```cmd
# Try with python instead of python3
python bin\chat-trim-tool.py chat.json --split-by-day

# Or use full path
"C:\Program Files\Python311\python.exe" bin\chat-trim-tool.py
```

---

## Getting Help

**If your issue isn't listed here**:

1. **Check basics**:
   - Python 3.7+? → `python3 --version`
   - Valid JSON? → Try opening in VS Code
   - Correct date format? → YYYY-MM-DD only

2. **Collect debug info**:
   ```bash
   python3 bin/chat-trim-tool.py --help
   python3 --version
   ```

3. **Open an issue on GitHub**:
   - Include the exact command you ran
   - Share the error message
   - Include `python3 --version` output

---

**Stuck? Check [QUICK_START.md](../docs/QUICK_START.md) or [USAGE.md](../docs/USAGE.md)!**
