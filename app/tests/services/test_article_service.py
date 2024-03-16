from tortoise.contrib.test import TestCase

from app.models.article import Article
from app.services.article_service import service_get_article_and_comments


class TestArticleRouter(TestCase):
    async def test_get_article_and_comment(self) -> None:
        # given
        article_id = "test_article"
        article = await Article.create(
            id=article_id, author="author", title="title", body="body"
        )

        # when
        article_and_comment = await service_get_article_and_comments(article_id)

        # then
        self.assertEqual(article_and_comment.id, article_id)
        self.assertEqual(article_and_comment.author, "author")
        self.assertEqual(article_and_comment.title, "title")
        self.assertEqual(article_and_comment.body, "body")
