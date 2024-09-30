from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `id` VARCHAR(40) NOT NULL  PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `name` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `likes` (
    `id` VARCHAR(40) NOT NULL  PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `author` VARCHAR(255) NOT NULL,
    `body` LONGTEXT NOT NULL,
    `article_id` VARCHAR(40) NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `users`;
        DROP TABLE IF EXISTS `likes`;"""
