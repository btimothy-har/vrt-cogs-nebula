import logging

import discord
from discord import app_commands
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.data_manager import cog_data_path

from .abc import CompositeMetaClass
from .commands import Utils

log = logging.getLogger("red.vrt.vrtutils")


class VrtUtils(Utils, commands.Cog, metaclass=CompositeMetaClass):
    """
    A collection of utility commands for getting info about various things.
    """

    __author__ = "vertyco"
    __version__ = "2.4.0"

    def format_help_for_context(self, ctx: commands.Context):
        helpcmd = super().format_help_for_context(ctx)
        return f"{helpcmd}\nCog Version: {self.__version__}\nAuthor: {self.__author__}"

    async def red_delete_data_for_user(self, *, requester, user_id: int):
        """No data to delete"""

    def __init__(self, bot: Red):
        super().__init__()
        self.bot: Red = bot
        self.path = cog_data_path(self)

    @app_commands.command(name="ping", description="Return the bot's latency.")
    async def ping(self, interaction: discord.Interaction):
        """
        Return the bot's latency.
        """
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! `{latency}ms`", ephemeral=True)
