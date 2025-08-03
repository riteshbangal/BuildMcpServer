# Authentication Options for MCP Server

## 1. Device Authorization Flow (Recommended)

- Endpoint: `POST /oauth/device`
- This flow is suitable for agent/device authentication.
- See the diagram below for the device authorization process:

![Device Authorization Flow](utilities/assets/Device_Authorization_Flow.png)

## 2. Pre-Authorized Tokens (Alternative)

If device flow is not possible, use pre-authorized tokens:

1. User logs into your Identity Provider (IdP) via browser (SSO) and copies a token manually.
2. User pastes the token into Copilot's settings or the `mcp.json` config file.
3. Copilot sends this token with every MCP request.

### Manual Token Entry
- Document and instruct users to paste their token into the config file as shown:

```jsonc
{
  "kwargs": {
    "headers": {
        "Authorization": "Bearer <paste-your-token-here>"
    }
  }
}
```

---

> Place this section at the end of your documentation for clear guidance on authentication options.
