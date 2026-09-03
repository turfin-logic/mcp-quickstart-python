"""A minimal protocol-correct MCP server using the official Python SDK."""
from mcp.server.fastmcp import FastMCP  # type: ignore[attr-defined]

mcp = FastMCP("QuickstartMCP")

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """Return a greeting from the quickstart server."""
    return f"Hello, {name}! This is running via MCP."

if __name__ == "__main__":
    # FastMCP uses stdio by default. stdout is reserved for protocol messages.
    mcp.run()

