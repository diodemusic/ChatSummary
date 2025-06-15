import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

BOT_PREFIX = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")


if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    bot.run(token)
