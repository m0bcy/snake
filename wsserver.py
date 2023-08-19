#!/usr/bin/env python
import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print('received a message from the client: ' + message)
        await websocket.send("hello from websocket")

async def main():
    async with serve(echo, "127.0.0.1", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
