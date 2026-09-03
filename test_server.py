import pytest

pytest.importorskip("mcp")
from server import hello_world


def test_hello_world():
    assert hello_world("Ada") == "Hello, Ada! This is running via MCP."
