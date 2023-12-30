import discord#  DC套件
from discord import app_commands#  DC / command
from discord.ext import commands
import json


cfg=json.load(open("../cfg.json","r"))

token=cfg["DCbot"]["token"]

intents=discord.Intents.all()
intents.members=True
intents.message_content = True
DCbot_client=discord.Client(intents=intents)


#  當DCbot_client啟動
@DCbot_client.event
async def on_ready():
	print("雞雞人已啟動，身分為：",DCbot_client.user)
	print("雞雞人ID為：",DCbot_client.application_id)
	game=discord.Game("小ㄌㄌ")#  設定現在ㄐㄐ人在玩甚麼
	#discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
	await DCbot_client.change_presence(status=discord.Status.dnd,activity=game)
	print("以下是你能瀏覽的channel")
	allc=DCbot_client.get_all_channels()#  獲取所有有權限瀏覽的頻道
	for i in allc:
		print("名稱:",i.name,"\t\tid:",i.id)
	# while True:
	# 	print("DCbot > ",end="")
	# 	msg=input()
	# 	if msg=="exit":
	# 		break
	# 	elif msg=="send":
	# 		cid=input("channel id:")
	# 		channel=DCbot_client.get_channel(int(cid))
	# 		msg=""
	# 		print("enter the command \"end\" to end the message")
	# 		while True:
	# 			tmp=input()
	# 			if tmp=="end":
	# 				break
	# 			msg+=tmp+"\n"
	# 		await channel.send(msg)
	# 	elif msg=="help":
	# 		print("""
	# 		help: 顯示此訊息
	# 		send: 發送訊息
	# 		exit: 離開
	# 		""")



#  當有人傳送訊息
run_on_message=True
@DCbot_client.event
async def on_message(message):
	if(run_on_message==False):
		return
	if message.author == DCbot_client.user:
		print("雞雞人訊息發送成功")
	else:
		print("雞雞人收到訊息：")
		print("\t頻道訊息：")
		print("\t\t頻道名：",message.channel.name)
		print("\t\t頻道id：",message.channel.id)
		print("\t\t位於類別id：",message.channel.category_id)
		print("\t使用者：")
		print("\t\t使用者名稱：",message.author.name)
		print("\t\t使用者全域名稱：",message.author.global_name)
		print("\t\t使用者伺服器內名稱：",message.author.nick)
		print("\t\t雞雞人：",message.author.bot)
		print("\t訊息為：\n===訊息開始===\n",message.content,"\n===訊息結束===\n")

		#  print(message)


DCbot_client.run(token)



