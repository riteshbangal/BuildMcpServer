import requests
from mcp.server.fastmcp import FastMCP
from typing import Optional, Dict, Any
from datetime import datetime
from zoneinfo import ZoneInfo
import os
from functools import wraps

# API Key for authentication
API_KEY = "12345-abcde-67890-fghij"  # In production, this should be in environment variables

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print("[DEBUG] Incoming kwargs:", kwargs)
        headers = kwargs.get('headers', {})
        # Handle nested 'kwargs' as sent by MCP tool calls
        if not headers and 'kwargs' in kwargs:
            headers = kwargs['kwargs'].get('headers', {})
        print("[DEBUG] Headers:", headers)
        auth_header = headers.get('Authorization')
        print("[DEBUG] Authorization header:", auth_header)
        if not auth_header or auth_header != f"Bearer {API_KEY}":
            print(f"[DEBUG] Provided auth header does not match expected: Bearer {API_KEY}")
            return {"error": "Unauthorized", "message": "Invalid or missing API key"}, 401
        return f(*args, **kwargs)
    return decorated

# Create a FastMCP instance for BuildMCPServer
mcp  = FastMCP("Build MCP Server", host="0.0.0.0", port=3000, log_level="DEBUG")

# Define a simple health tool
@mcp.tool()
@require_auth
def health(**kwargs) -> dict:
    """
    Check the health of the MCP server.

    Parameters:
        headers (dict, optional): HTTP headers for authentication. Must include the Authorization header as follows:
            
            { "headers": {"Authorization": "Bearer 12345-abcde-67890-fghij"} }

        When calling this tool from an LLM or client, always provide the 'headers' parameter with the correct Authorization value as shown above.

    If the user does not provide the 'headers' parameter, the tool will attempt to use a default or prompt for the required authentication information.
    """
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
