from fastapi import FastAPI
import socketio
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Initialize Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")

# Mount the Socket.IO server to the FastAPI app
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)

@app.get("/hello")
async def hello_world():
    return {"message": "Hello from FastAPI REST!"}

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

# To run the app using uvicorn, we will use socket_app
# This ensures both FastAPI and Socket.IO are served correctly.
if __name__ == "__main__":
    uvicorn.run(socket_app, host="0.0.0.0", port=7777)