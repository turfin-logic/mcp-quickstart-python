import pytest

try:
    from mcp.server import MCPServer  # noqa: F401
except ImportError:
    pytest.skip("local environment has the pre-v2 MCP SDK", allow_module_level=True)
from server import hello_world


def test_hello_world():
    assert hello_world("Ada") == "Hello, Ada! This is running via MCP."

