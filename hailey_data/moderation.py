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
            raise
        await ctx.send("Success! :white_check_mark: ")
    @commands.has_permissions(ban_members=True)
    @commands.command(name="unban")
    async def unban(self, ctx, member="NO", reason="(No reason specified.)"):
        if member == "NO":
            await ctx.send("Please specify a user.")
            raise NothingSpecified(f"ctx.author: {ctx.author}, command: unban")
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users: #https://www.codegrepper.com/code-examples/python/discord.py+unban+command
            if (ban_entry.user.name, ban_entry.user.discriminator) == (member_name, member_discriminator):
                member = ban_entry.user
        mod = ctx.author
        reason = f"{reason}\nUnBanned by {mod}"
        try:
            await ctx.guild.unban(member, reason=reason)
        except Exception:
            await ctx.send("**Oops!**\nWe did an oopsie and we can't seem to ban that user. Please try again, and make sure the user exists.")
            raise
        await ctx.send("Success! :white_check_mark:")
def setup(bot):
    bot.add_cog(modCog(bot))
