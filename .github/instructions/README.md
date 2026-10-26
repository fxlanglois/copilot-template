# File-specific instructions

Add `*.instructions.md` files here for guidance that applies only to matching files. Use `applyTo` frontmatter to scope each instruction instead of placing unrelated rules in the workspace-wide instructions.

Example:

```markdown
---
name: Python tests
description: Testing conventions for Python files
applyTo: "**/*test*.py"
---

Add project-specific testing guidance here.
```
