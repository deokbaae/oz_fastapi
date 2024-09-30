from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.article import Article
from app.models.base_model import BaseModel


class Like(BaseModel, Model):
    article: fields.ForeignKeyRelation[Article] = fields.ForeignKeyField(
        "models.Article", related_name="likes", db_constraint=False
    )
    author = fields.CharField(max_length=255)
    body = fields.TextField()

    class Meta:
        table = "likes"

    @classmethod
    async def get_all_by_article_id(cls, article_id: str) -> list[Like]:
        return await cls.filter(article_id=article_id).all()
