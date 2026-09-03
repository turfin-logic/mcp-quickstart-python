"""Small stdio client for manually exercising server.py."""
from __future__ import annotations

import asyncio
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent


async def main() -> None:
    server = StdioServerParameters(command="python", args=[str(Path(__file__).with_name("server.py"))])
    async with stdio_client(server) as (read, write), ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool("hello_world", {"name": "Ada"})
        first = result.content[0]
        if not isinstance(first, TextContent):
            raise TypeError("hello_world returned a non-text MCP content block")
        print(first.text)

if __name__ == "__main__": asyncio.run(main())

