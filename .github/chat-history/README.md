# Chat History - Development Records

This folder preserves the development conversations and decisions for the json-to-markdown-tools project.

## Purpose

Documenting development chats ensures:
- Development decisions are preserved with full context
- Future developers can understand the "why" behind features
- Features can be refined based on original discussions
- Development can be resumed from a known checkpoint

## Files

### user-message-styling-dev.json
- **Format**: VS Code Copilot chat export (JSON)
- **Size**: Compressed format, full metadata preserved
- **Usage**: Original source for all development discussions
- **Export Command**:
  ```bash
  python3 ../bin/chat-trim-tool.py user-message-styling-dev.json --format markdown
  ```

### user-message-styling-dev.md
- **Format**: Readable markdown
- **Generated**: From JSON export using the tool itself
- **Best For**: Quick reference, reading in VS Code, sharing
- **Style**: Divider-style for clear message separation

## How to Use

### 1. Export New Development Chat

When a development session ends:
```bash
# In VS Code:
1. Right-click chat session
2. Select "Export Chat"
3. Save to .github/chat-history/[name].json
4. Name format: [feature]-dev-[date].json
```

### 2. Convert to Markdown

```bash
cd ../../
python3 bin/chat-trim-tool.py .github/chat-history/[filename].json \
  --user-style divider \
  --format markdown \
  --output .github/chat-history/
```

### 3. Commit to Repository

```bash
git add .github/chat-history/
git commit -m "Add development chat: [feature description]"
git push
```

## Naming Convention

- **JSON**: `[feature-name]-dev-[phase].json`
  - Example: `user-message-styling-dev-phase1.json`
  
- **Markdown**: Same name, `.md` extension
  - Example: `user-message-styling-dev-phase1.md`

## Reading Development History

1. **Start with DEVELOPMENT.md** (project root) for overview
2. **Read markdown versions** for quick scanning (better formatting)
3. **Check JSON** for complete metadata if needed
4. **Review relevant commit messages** for context

## Tips

- Use `--split-by-day` when exporting long chats to keep files manageable
- Add a header comment in the markdown explaining the chat's purpose
- Link to related commits in any documentation
- Update DEVELOPMENT.md when making significant decisions

## Privacy Note

These are development records. Before sharing the repository publicly, review chat exports for:
- Sensitive information
- File paths revealing system structure
- Personal details

---

**Folder Created**: March 19, 2026
**Purpose**: Preserve json-to-markdown-tools development history
