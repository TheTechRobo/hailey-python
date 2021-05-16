import discord, random
from discord.ext import commands
from discord.utils import get
from .INFO import appeal
from .func import SetEmbed
class NothingSpecified(Exception):
    pass
class modCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.has_permissions(ban_members=True)
    @commands.command(name="ban") #https://stackoverflow.com/a/62996702/9654083
    async def ban(self, ctx, member: discord.Member, reason="(No reason specified.)", delete_message_days=1):
        """
        TIP: Entries such as TheTechRobo#5291 do not work. You need to @-mention them.
        """
        mod = ctx.author
        reason = f"{reason}\nBanned by {mod}"
        delete_message_days = int(delete_message_days)
        if delete_message_days not in (0, 1, 7):
            await ctx.send("Invalid number of days! Must be 0, 1, or 7.")
        try:
            await member.send(f"**Looks like you've been banned from the {ctx.guild.name} server!**\nYour ban reason was: {reason}.")
            if appeal is not None:
                await member.send(f"_{appeal}_")
        except Exception as ename:
            await ctx.send("(WARNING: Could not send a message to the user.)")
        try:
            await ctx.guild.ban(member, reason=reason, delete_message_days=delete_message_days)
        except Exception:
            await ctx.send("**Oops!**\nFailed to ban user. Please move the role of Hailey the Snake higher than all roles you want to be able to ban and lower than roles you don't want to be able to ban.")
            raise #awareness
        await ctx.send("Success! :white_check_mark: ")
    @commands.has_permissions(ban_members=True)
    @commands.command(name="unban")
    async def unban(self, ctx, member="NO", reason="(No reason specified.)"):
        if member == "NO":
            await ctx.send("Please specify a user.")
            raise NothingSpecified(f"ctx.author: {ctx.author}, command: unban")
        banned_users = await ctx.guild.bans()
        try:
            member_name, member_discriminator = member.split('#')
        except Exception:
            await ctx.send("Invalid user! You need to use Username#XXXX format.")
            raise
        member = None
        similar = []
        for ban_entry in banned_users: #https://www.codegrepper.com/code-examples/python/discord.py+unban+command
            if (ban_entry.user.name, ban_entry.user.discriminator) == (member_name, member_discriminator):
                member = ban_entry.user
            elif ban_entry.user.name == member_name:
                similar.append(f"{ban_entry.user.name}#{ban_entry.user.discriminator}")
        if similar == []:
            similar = "(No users found.)"
        if member is None:
            await ctx.send(embed=SetEmbed("Could not find user in ban list!", "If you're sure you typed it corretly, they may already be unbanned.", footer=f"However, the following users were similar:\n{similar}"))
            #await ctx.send("Could not find user in ban list! If you're sure you typed it correctly, they may be already unbanned.")
            #await ctx.send(f"However, the following users were similar:\n{similar}")
            raise Exception("user not found")
        mod = ctx.author
        reason = f"{reason}\nUnBanned by {mod}"
        try:
            await ctx.guild.unban(member, reason=reason)
        except Exception:
            await ctx.send("**Oops!**\nWe did an oopsie and we can't seem to unban that user. Please try again, and make sure the user exists.")
            raise
        await ctx.send("Success! :white_check_mark:")
    @commands.has_permissions(kick_members=True)
    @commands.command(name="kick")
    async def kick(self, ctx, member: discord.Member, reason: str):
        mod = ctx.author
        reason = f"{reason}\nKicked by {mod}"
        await ctx.send(f"Not working yet - Potentially used member: {member.mention} - Ban Reason: \n```\n{reason}\n```")
def setup(bot):
    bot.add_cog(modCog(bot))
