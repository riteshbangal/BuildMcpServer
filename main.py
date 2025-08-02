import requests
from mcp.server.fastmcp import FastMCP
from typing import Optional, Dict, Any
from datetime import datetime
from zoneinfo import ZoneInfo
import os

# Create a FastMCP instance for BuildMCPServer
mcp  = FastMCP("Build MCP Server", host="0.0.0.0", port=3000, log_level="DEBUG")

# Define a simple health tool
@mcp.tool()
def health() -> dict:
    """Check the health of the MCP server."""
    return {"status": "ok", "message": "MCP Server is running smoothly."}

# Define a tool to get current time and time zone information
@mcp.tool()
def get_current_time_info() -> dict:
    """Returns the current local time, time zone, and UTC offset."""
    # Get the system's local timezone (uses TZ env variable or OS setting)
    tz_name = os.environ.get("TZ", "Europe/Amsterdam")  # fallback if TZ not set
    tz = ZoneInfo(tz_name)

    now = datetime.now(tz)
    return {
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": tz.key,
        "utc_offset": now.strftime("%z")
    }

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    print("Starting BuildMCPServer ...")
