# Git Commit Convention

Use **Conventional Commits** to keep the Git history clean, consistent, and easy to understand.

| Commit Type | When to Use | Example |
|---|---|---|
| `feat` | New capability or functionality | `feat: add document upload API` |
| `fix` | Something was broken and has been fixed | `fix: resolve document retrieval issue` |
| `refactor` | Improving existing code structure without changing behavior | `refactor: simplify RAG service logic` |
| `perf` | Improving performance or reducing latency | `perf: optimize embedding generation` |
| `test` | Adding or modifying tests | `test: add retrieval service tests` |
| `docs` | Updating README, comments, or documentation | `docs: update project setup guide` |
| `chore` | Dependencies, configuration, maintenance, or other non-feature changes | `chore: update project dependencies` |

### Quick Guide

- **New capability → `feat`**
- **Something was broken → `fix`**
- **Improving existing code structure → `refactor`**
- **Making it faster → `perf`**
- **Adding or updating tests → `test`**
- **README/comments/docs → `docs`**
- **Dependencies/config/maintenance → `chore`**

### Commit Format

```text
<type>(<scope>): <short description>