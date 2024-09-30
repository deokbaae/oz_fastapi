from app.models.like import Like


async def do_like(article_id: str, user_id: str) -> Like:
    return await Like.create_one(article_id, user_id)



