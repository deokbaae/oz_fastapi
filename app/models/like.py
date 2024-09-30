from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.article import Article
from app.models.base_model import BaseModel
from app.models.user import User


class Like(BaseModel, Model):
    article: fields.ForeignKeyRelation[Article] = fields.ForeignKeyField(
        "models.Article", related_name="likes", db_constraint=False
    )
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="likes", db_constraint=False
    )

    class Meta:
        table = "likes"
        unique_together = (("article", "user"),)

    @classmethod
    async def create_one(cls, article_id: str, user_id: str) -> Like:
        return await cls.create(article_id=article_id, user_id=user_id)

    @classmethod
    async def get_all_by_article_id(cls, article_id: str) -> list[Like]:
        return await cls.filter(article_id=article_id).all()
