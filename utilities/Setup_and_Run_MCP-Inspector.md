# MCP Inspector Setup Guide

This guide explains how to set up and run the MCP Inspector server using FastMCP.

---

## Prerequisites

- **Python 3.13+** installed (managed via `uv` or system Python)
- **Node.js** installed (v16+ recommended) for UI frontend support
- MCP Python package installed with CLI extras:  
  ```bash
  uv pip install --upgrade "mcp[cli]"
````

* Basic familiarity with terminal commands

---

## Step: Run the MCP Inspector with UI

Start the development server with UI:

```bash
mcp dev mcp_inspector.py
```

You should see output with a URL (e.g., `http://127.0.0.1:8000`) — open it in your browser.

The UI allows you to interactively test your registered tools and see responses.

---
