from pydantic import BaseModel


class LinkedInPost(BaseModel):
    content: str