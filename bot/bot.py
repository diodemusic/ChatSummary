# bot.py
import asyncio
import logging

import discord
from discord.ext import commands

import config

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s:%(name)s: %(message)s"
)


async def load_cogs(bot, cogs):
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            logger.info(f"Loaded extension {cog}")
        except Exception as e:
            logger.exception(f"Failed to load extension {cog}: {e}")


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        cogs = ["cogs.ping"]
        await load_cogs(self, cogs)

    async def on_ready(self):
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")

        guild = discord.Object(id=config.TEST_GUILD_ID)
        await self.tree.sync(guild=guild)
        logger.info(
            f"Synchronized application commands to guild {config.TEST_GUILD_ID}"
        )


async def main():
    bot = MyBot()
    try:
        await bot.start(config.DISCORD_TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot shutting down...")


if __name__ == "__main__":
    asyncio.run(main())
