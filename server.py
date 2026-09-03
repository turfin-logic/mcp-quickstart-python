"""A minimal protocol-correct MCP server using the official Python SDK."""
try:
    from mcp.server import MCPServer
except ImportError:  # compatibility with the older locally installed SDK only
    from mcp.server.fastmcp import (
        FastMCP as MCPServer,  # type: ignore[attr-defined,no-redef]
    )

mcp = MCPServer("QuickstartMCP")

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """Return a greeting from the quickstart server."""
    return f"Hello, {name}! This is running via MCP."

if __name__ == "__main__":
    # FastMCP uses stdio by default. stdout is reserved for protocol messages.
    mcp.run()

