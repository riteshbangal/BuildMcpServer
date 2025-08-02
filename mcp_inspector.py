# mcp_inspector.py
"""
"MCP Inspector Tool Router"
This script uses the MCP framework to route user queries to appropriate tools.
It defines several tools and routes queries based on their content.

Author: Ritesh Bangal
Version: 1.0
"""
from mcp.server.fastmcp import FastMCP

# Create an instance of FastMCP
mcp = FastMCP("MCP Inspector", log_level="DEBUG")

@mcp.tool()
def load_mcp_inspector() -> str:
    return "🤖 MCP Inspector has been loaded successfully! You can now ask questions."


if __name__ == "__main__":
    mcp.run()
    print("MCP Inspector is running...")

