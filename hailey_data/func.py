import random, discord
def TheColoursOfTheRainbow(): #to choose a random RGB value
    colours = []
    for i in range(0,3):
        colours.append(random.randint(0,255))
    return colours
def SetEmbed(title, description, url=False, colour=False, img=False, footer=False):
    """
    params are self explanatory.
    returns the embed.
    """
    if not colour:
        colour = TheColoursOfTheRainbow()
        colour = discord.Color.from_rgb(*colour)
    if not url: mountEmbed = discord.Embed(title=title, description=description, color=colour)
    else: mountEmbed = discord.Embed(title=title, description=description, color=colour, url=url)
    if not img: pass
    else:  mountEmbed.set_image(url=img)
    if not footer: pass
    else: mountEmbed.set_footer(text=footer)
    return mountEmbed
