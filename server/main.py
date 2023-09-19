from fastapi import FastAPI
from models import ChatData

app = FastAPI()

@app.post("/api/chat")
def receive_chat_data(data: ChatData):
    # Store or process chat data
    # For now, just return it as is
    return {"received": data.content}
