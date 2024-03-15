from pydantic import BaseModel


class CommentResponse(BaseModel):
    author: str
    body: str


class ArticleAndCommentsResponse(BaseModel):
    author: str
    title: str
    body: str
    comments: tuple[CommentResponse, ...]
