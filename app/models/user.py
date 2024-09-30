from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class User(BaseModel, Model):
    name = fields.CharField(max_length=255)

    class Meta:
        table = "users"
