import asyncio
import json
import sys
from typing import Dict, Any, Callable

class MCPServer:
    """A lightweight, zero-dependency MCP (Model Context Protocol) Server Boilerplate."""
    
    def __init__(self, name: str):
        self.name = name
        self.tools: Dict[str, Callable] = {}
        self.running = False

    def tool(self, name: str, description: str):
        """Decorator to register an MCP tool."""
        def decorator(func):
            self.tools[name] = {
                "func": func,
                "description": description,
                "name": name
            }
            return func
        return decorator

    async def _handle_request(self, req: str):
        try:
            data = json.loads(req)
            action = data.get("action")
            
            if action == "list_tools":
                return {"tools": [{"name": k, "description": v["description"]} for k, v in self.tools.items()]}
            
            if action == "call_tool":
                tool_name = data.get("tool")
                kwargs = data.get("args", {})
                if tool_name in self.tools:
                    result = await self.tools[tool_name]["func"](**kwargs)
                    return {"status": "success", "result": result}
                return {"status": "error", "message": f"Tool '{tool_name}' not found."}
                
        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def serve(self):
        """Starts the stdio JSON-RPC loop."""
        self.running = True
        print(f"[{self.name}] MCP Server started.", file=sys.stderr)
        
        while self.running:
            line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
            if not line:
                break
                
            response = await self._handle_request(line.strip())
            print(json.dumps(response), flush=True)

# === Usage Example ===
if __name__ == "__main__":
    app = MCPServer("QuickstartMCP")

    @app.tool(name="hello_world", description="Returns a simple greeting.")
    async def hello_world(name: str = "World"):
        return f"Hello, {name}! This is running via MCP."

    asyncio.run(app.serve())
