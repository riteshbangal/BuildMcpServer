# MCP Server Setup Guide

This guide explains how to set up and run a basic MCP server using `uv` and MCP.

---

## Setup Commands

1. Install `uv`:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.local/bin/env
   uv
````

2. Install Python 3.13 using `uv`:

   ```bash
   uv python install 3.13
   ```

3. Configure Python and pip aliases (add these to your `~/.zshrc` or shell config):

   ```bash
   alias python="/Users/riteshbangal/.local/share/uv/python/cpython-3.13.5-macos-x86_64-none/bin/python3.13"
   alias python3="/Users/riteshbangal/.local/share/uv/python/cpython-3.13.5-macos-x86_64-none/bin/python3.13"
   alias pip="/Users/riteshbangal/.local/share/uv/python/cpython-3.13.5-macos-x86_64-none/bin/pip3.13"
   alias pip3="/Users/riteshbangal/.local/share/uv/python/cpython-3.13.5-macos-x86_64-none/bin/pip3.13"

   . "$HOME/.local/bin/env"
   ```

   Then reload your shell config:

   ```bash
   source ~/.zshrc
   ```

4. Verify Python installation:

   ```bash
   uv python --version
   python3.13 --version
   ```

5. Initialize your project with `uv`:

   ```bash
   uv init
   ```

6. Create and activate a virtual environment:

   ```bash
   uv venv
   source .venv/bin/activate
   ```

7. Add required packages (`fastmcp` and `mcp` with CLI extras):

   ```bash
   uv add fastmcp
   uv add mcp
   uv add 'mcp[cli]'
   ```

8. Run your MCP server script:

   ```bash
   mcp run main.py
   ```

---

This sequence sets up Python, pip aliases, virtual environment, MCP packages, and runs your MCP server.
