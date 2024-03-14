from tortoise.models import Model
from tortoise import fields
from app.models.base_model import BaseModel


class Article(BaseModel, Model):

    author = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)
    body = fields.TextField()

    class Meta:
        table = "articles"
