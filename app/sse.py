from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Mount, Route

mcp = Server("example")
transport = SseServerTransport("/messages/")


# Define handler functions
async def handle_sse(request):
    async with transport.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        await mcp.run(streams[0], streams[1], mcp.create_initialization_options())


# Create Starlette routes for SSE and message handling
routes = [
    Route("/sse/", endpoint=handle_sse),
    Mount("/messages/", app=transport.handle_post_message),
]

# Create a Starlette app
sse = Starlette(routes=routes, debug=True)
