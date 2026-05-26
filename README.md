# MCP Quickstart Python 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The absolute fastest way to build a **Model Context Protocol (MCP)** server in Python. Zero bloated dependencies, async-first, and ready to connect with Claude, Gemini, or any MCP-compatible agent.

## Why this boilerplate?
The internet is full of complex MCP SDKs that take hours to understand. This repository provides a single-file, lightweight `MCPServer` class that you can drop into any project. It handles stdio communication, JSON parsing, and asynchronous tool routing perfectly.

## Quickstart

1. **Clone the repo**
   ```bash
   git clone https://github.com/turfin-logic/mcp-quickstart-python.git
   cd mcp-quickstart-python
   ```

2. **Add your tools in `server.py`**
   ```python
   @app.tool(name="calculate_revenue", description="Calculates startup revenue.")
   async def calculate_revenue(users: int, price: float):
       return {"revenue": users * price}
   ```

3. **Run your MCP server**
   ```bash
   python server.py
   ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Created by [turfin-logic](https://github.com/turfin-logic) - Building the future of agentic AI.
