import logging

import discord
from discord import app_commands
from discord.ext import commands

logger = logging.getLogger(__name__)


class PingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="ping", description="Replies with Pong! And Shows latency."
    )
    async def ping(self, interaction: discord.Interaction):
        ws_latency = self.bot.latency

        await interaction.response.send_message(
            f"Pong! WebSocket latency: {ws_latency * 1000:.1f} ms"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(PingCog(bot))
