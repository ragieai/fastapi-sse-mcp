# FastAPI SSE MCP

A FastAPI application that demonstrates Server-Sent Events (SSE) integration with the Model Context Protocol

## Overview

This project showcases how to use Server-Sent Events (SSE) as a transport layer for MCP in a FastAPI application. It provides a simple echo service that can:

- Handle FastAPI HTTP requests
- Implement MCP tools, resources and prompts using the MCP python-sdk

## Requirements

- Python 3.12+
- FastAPI 0.115.11+
- MCP 1.4.1+

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ragieai/fastapi-sse-mcp.git
   cd fastapi-sse-mcp
   ```

2. Install dependencies:
   ```bash
   uv sync --dev
   ```

## Running the Application

Start the FastAPI server:

```bash
uv run uvicorn app.main:app --reload
```

The server will be available at http://127.0.0.1:8000.

## API Endpoints

- `GET /` - Returns a simple JSON greeting
- `GET /sse/` - SSE endpoint for establishing connections
- `POST /messages/` - Endpoint for sending messages over SSE

## Examples

The application provides three example MCP functions:

1. **Tool Function**: Echoes messages
   ```python
   @mcp.tool()
   def echo_tool(message: str) -> str:
       """Echo a message as a tool"""
       return f"Tool echo: {message}"
   ```

2. **Prompt Function**: Creates echo prompts
   ```python
   @mcp.prompt()
   def echo_prompt(message: str) -> str:
       """Create an echo prompt"""
       return f"Please process this message: {message}"
   ```

3. **Resource Function**: Handles resource requests
   ```python
   @mcp.resource("echo://{message}")
   def echo_resource(message: str) -> str:
       """Echo a message as a resource"""
       return f"Resource echo: {message}"
   ```

## License

MIT License

Copyright (c) 2024 Ragie Corp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

