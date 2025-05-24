from fastapi import FastAPI
import socketio
import uvicorn

app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)


@app.get("/")
async def heartbeat():
    return {"message": "FastAPI is alive!"}


@sio.on("connect")
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    await sio.emit("message", f"Welcome, {sid}!", room=sid)

@sio.on("disconnect")
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.on("chat_message")
async def handle_chat_message(sid, data):
    print(f"Received message from {sid}: {data}")
    await sio.emit("message", f"Server received: {data}", room=sid)
    # You can broadcast to all connected clients
    # await sio.emit("message", f"Broadcast from {sid}: {data}")


if __name__ == "__main__":
    uvicorn.run(socket_app, host="0.0.0.0", port=3101)