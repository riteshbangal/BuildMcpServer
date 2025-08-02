import requests
from mcp.server.fastmcp import FastMCP

# Create a FastMCP instance for BuildMCPServer
mcp  = FastMCP("Build MCP Server", host="0.0.0.0", port=3000, log_level="DEBUG")

# Define a simple health tool
@mcp.tool()
def health() -> str:
    """Check the health of the MCP server."""
    return {"status": "ok", "message": "MCP Server is running smoothly."}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

    print("Starting BuildMCPServer ...")
