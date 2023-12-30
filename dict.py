import discord#  DC套件

intents=discord.Intents.all()#  設定DCbot的權限
DCbot_client=discord.Client(intents=intents)#  創建DCbot





@DCbot_client.event
async def on_message(message):#  當有訊息傳來
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

@DCbot_client.event
async def on_ready():#  當機基人成功啟動
	print("雞雞人已啟動，身分為：",DCbot_client.user)
	print("雞雞人ID為：",DCbot_client.application_id)

	game=discord.Game("小ㄌㄌ")#  設定現在在玩甚麼
	#discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
	await DCbot_client.change_presence(status=discord.Status.dnd,activity=game)#  設定狀態

	channel=DCbot_client.get_channel(int(cid))#  以id取得頻道
	await channel.send(msg)#  發送訊息msg到頻道channel







DCbot_client.run(token)#	啟動DCbot
