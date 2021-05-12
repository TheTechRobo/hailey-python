import discord, random
from discord.ext import commands
from discord.utils import get
class NothingSpecified(Exception):
    pass
class modCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.has_permissions(ban_members=True)
    @commands.command(name="ban") #https://stackoverflow.com/a/62996702/9654083
    async def ban(self, ctx, member="NO", reason="(No reason specified.)", delete_message_days=1):
        if member == "NO":
            await ctx.send("Please specify a user.")
            raise NothingSpecified(f"ctx.author: {ctx.author}, command: ban")
        mod = ctx.author
        reason = f"{reason}\nBanned by {mod}"
        member = await self.bot.fetch_user(int(member.strip("<!@>")))
        try:
            await ctx.guild.ban(member, reason=reason, delete_message_days=delete_message_days)
        except Exception:
            await ctx.send("**Oops!**\nFailed to ban user. Please move the role of Hailey the Snake higher than all roles you want to be able to ban and lower than roles you don't want to be able to ban.")
            return
        await ctx.send("Success! :white_check_mark: ")
def setup(bot):
    bot.add_cog(modCog(bot))
