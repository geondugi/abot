import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("GEONDUGI Bot:",client.user.name,"GEONDUGI Bot:",client.user.id,"1.0:",discord.__version__)


client.run(os.environ['MTAwMjA0MTY2MjM4NzgwMjE4Mg.G-vuhq.nhb3H_D1m8OpLzGG1CBmR6OCQts2eMNGzXJsyA'])