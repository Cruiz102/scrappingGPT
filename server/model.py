from pydantic import BaseModel

class ChatData(BaseModel):
    content: str
