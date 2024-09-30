from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `likes` ADD `user_id` VARCHAR(40) NOT NULL;
        ALTER TABLE `likes` DROP COLUMN `body`;
        ALTER TABLE `likes` DROP COLUMN `author`;
        ALTER TABLE `likes` ADD UNIQUE INDEX `uid_likes_article_1dbfb1` (`article_id`, `user_id`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `likes` DROP INDEX `uid_likes_article_1dbfb1`;
        ALTER TABLE `likes` ADD `body` LONGTEXT NOT NULL;
        ALTER TABLE `likes` ADD `author` VARCHAR(255) NOT NULL;
        ALTER TABLE `likes` DROP COLUMN `user_id`;"""
