# Output Styling Guide

**json-to-markdown-tools** offers flexible styling options to customize how your chat export looks. Choose the style that best matches your documentation needs.

## Overview

The tool supports multiple output styles for both user messages and assistant responses:

| Style | Description | Best For |
|-------|-------------|----------|
| `none` | Simple bold formatting (default) | Clean, minimal output |
| `emoji` | Emoji icons with bold labels | Friendly, visual documentation |
| `block` | Blockquote style indentation | Citation-like formatting |
| `box` | Unicode box border formatting | Eye-catching highlights |
| `color` | HTML color spans | Web-based documentation |

## CLI Usage

### Basic Syntax with Styles

```bash
python3 chat-trim-tool.py input.json --user-style STYLE [--style-color COLOR]
```

### Available Styles

#### 1. None (Default)

Simplest formatting with just bold labels.

```bash
python3 chat-trim-tool.py chat.json --format markdown
```

**Output Example:**
```
**User:**
How do I create a class in Python?

**Assistant:**
You can create a class using the class keyword...
```

#### 2. Emoji Style

Adds relevant emoji icons for visual distinction.

```bash
python3 chat-trim-tool.py chat.json --user-style emoji --format markdown
```

**Output Example:**
```
👤 **User:**
How do I create a class in Python?

🤖 **Assistant:**
You can create a class using the class keyword...
```

#### 3. Block Style

Formats messages as blockquotes, perfect for citation-style documentation.

```bash
python3 chat-trim-tool.py chat.json --user-style block --format markdown
```

**Output Example:**
```
> **👤 User:**
> How do I create a class in Python?

> **🤖 Assistant:**
> You can create a class using the class keyword...
```

#### 4. Box Style

Wraps messages in Unicode box borders for prominent visual display.

```bash
python3 chat-trim-tool.py chat.json --user-style box --format markdown
```

**Output Example:**
```
╔═════════════════════════════════════════════════════════════════╗
║ 👤 User                                                      ║
║ How do I create a class in Python?                           ║
╚═════════════════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════════════════╗
║ 🤖 Assistant                                                  ║
║ You can create a class using the class keyword...            ║
╚═════════════════════════════════════════════════════════════════╝
```

#### 5. Color Style (HTML)

Outputs HTML `<span>` tags with CSS color styling. Ideal for web-based documentation and systems that support inline HTML.

```bash
python3 chat-trim-tool.py chat.json --user-style color --style-color blue --format markdown
```

**Output:**
```html
<span style="color:blue">**👤 User:**</span>
How do I create a class in Python?

<span style="color:blue">**🤖 Assistant:**</span>
You can create a class using the class keyword...
```

## Color Customization

When using the `color` or `emoji` styles, customize the color with the `--style-color` option:

```bash
# Blue colored labels
python3 chat-trim-tool.py chat.json --user-style color --style-color blue

# Red colored labels
python3 chat-trim-tool.py chat.json --user-style color --style-color "#FF0000"

# Named CSS colors
python3 chat-trim-tool.py chat.json --user-style color --style-color darkgreen
```

### Supported Color Values

- **Named colors**: `red`, `blue`, `green`, `purple`, `orange`, `gray`, `darkgreen`, `darkblue`, etc.
- **Hex colors**: `#FF0000`, `#00FF00`, `#0000FF`, etc.
- **RGB colors**: Can be used in HTML contexts: `rgb(255, 0, 0)`

## Real-World Examples

### Example 1: Professional Documentation

```bash
python3 chat-trim-tool.py chat.json \
  --user-style block \
  --format markdown \
  --split-by-day
```

Perfect for creating professional-looking chat archives with clear blockquote formatting.

### Example 2: Friendly Tutorial

```bash
python3 chat-trim-tool.py chat.json \
  --user-style emoji \
  --format markdown
```

Great for tutorials or educational content where friendly visual indicators help readability.

### Example 3: Web Documentation

```bash
python3 chat-trim-tool.py chat.json \
  --user-style color \
  --style-color "#2E86AB" \
  --format markdown
```

Ideal for exporting to web platforms like Notion, Confluence, or GitHub Pages with custom brand colors.

### Example 4: Highlighted Conversations

```bash
python3 chat-trim-tool.py chat.json \
  --user-style box \
  --format markdown \
  --start "2026-03-15"
```

Creates eye-catching boxed output perfect for highlighting important conversations.

## Styling Best Practices

### Choose Based on Output Platform

- **GitHub/GitLab**: Use `emoji` or `block` (best markdown support)
- **Notion/Confluent**: Use `color` with custom brand colors
- **Slack/Discord**: Use `emoji` for best compatibility
- **Static Documentation**: Use `block` for clean, professional look
- **Print/PDF**: Use `box` for clear visual separation

### Combining Styles with Filters

```bash
# Last week's important conversations with visual style
python3 chat-trim-tool.py chat.json \
  --start "2026-03-10" \
  --end "2026-03-17" \
  --user-style emoji \
  --split-by-day \
  --format markdown
```

### Color Accessibility

When using `color` style, ensure sufficient contrast:
- Light backgrounds: Use dark colors (`darkblue`, `darkgreen`, `#1a1a1a`)
- Dark backgrounds: Use bright colors (`cyan`, `yellow`, `#00FFFF`)

## HTML Processing Note

The `color` style generates HTML that's designed to work with markdown processors that support inline HTML (like GitHub's markdown renderer). The output maintains markdown formatting while adding HTML color spans.

For maximum compatibility across platforms, test your exported markdown in your target environment before sharing widely.

---

**Pro Tip**: Experiment with different styles on a small date range first to find the look that works best for your documentation needs!
