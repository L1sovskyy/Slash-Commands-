import disnake
from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[1048312899975774299])
    async def clear(self, interaction, amount: int):
        embed = disnake.Embed(title = "Очистка", description = f"Удалено {amount} сообщений", color = 0x2C2D31)
        await interaction.response.send_message(embed = embed, ephemeral = True)
        await interaction.channel.purge(limit = amount + 1)


def setup(bot):
    bot.add_cog(Clear(bot))