from fastapi import FastAPI
from app.sse import create_sse_server
from mcp.server.fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("example")

# Mount the Starlette SSE server onto the FastAPI app
app.mount("/", create_sse_server(mcp))


@app.get("/")
def read_root():
    return {"Hello": "World"}
