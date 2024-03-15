from tortoise.contrib.test import TestCase

from app.models.article import Article


class TestArticleRouter(TestCase):

    async def test_글과_댓글이_함께_리턴된다(self):
        article_id = "test_article"
        article = Article.create(id=article_id, author="author", title="title", body="body")
