# MCP Quickstart (Python)

A minimal Model Context Protocol server built with the official Python SDK. It
uses the standard stdio transport and exposes one typed tool.

## Setup
1. Ensure Python 3.10+ is installed.
2. Install dependencies: `python -m pip install -r requirements.txt`.
3. Run `python client.py`; it starts the server over stdio, performs the MCP
   handshake, lists the tool and calls `hello_world`.

The server writes protocol traffic to stdout through the SDK. Do not print
diagnostics there; use stderr for diagnostics. This example has no network
service, authentication or persistent state. Run `python -m pip install
-r requirements-dev.txt` for lint, type and test checks.
