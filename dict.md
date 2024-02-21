

# 基本樣板
## 單檔案架構
`main.py`
```py
import discord
from discord.ext import commands
import asyncio

token="把你的bot token放在這"

#  設定bot權限
intents=discord.Intents.all()#  設定權限：所有權限
DCbot=commands.Bot(command_prefix="/",intents=intents)
#  command_prefix：指令前綴，例如：/help（這和discord的/ command 不一樣）
#  intents：權限，例如：發送訊息、管理訊息、管理伺服器、管理使用者等等，視需要而定

@DCbot.event
async def on_ready():#  當DCbot啟動
	slash=await DCbot.tree.sync()#  將 / 指令同步到DC，否則無法使用斜線指令

async def load_file():#  cogs檔案架構
	for fname in os.listdir("./cogs"):
		try:
			if fname.endswith(".py"):
				await DCbot.load_extension(f"cogs.{fname[:-3]}")#  載入cogs
			pass
		except:
			print(f"載入./cogs{fname}時發生錯誤")
			pass

async def main():
	async with DCbot:
		await load_file()
		await DCbot.start(token)

asyncio.run(main())#  執行bot
```

## cogs檔案架構
p.s. cogs檔案不能單獨存在，必須使用main.py來驅動（範例中的main.py有驅動cogs檔案的程式碼，可以直接使用）
p.s. 僅管是不同的cog檔，class名稱也不能重複
`cogs/filename.py`
```py
enable=False#  debug用，設定為True時，會載入這個cogs
cogname="cogname"#  debug用，可用來檢測是哪個cogs出錯ㄡ

import discord
from discord.ext import commands
from discord import app_commands#  增加DC / 指令支援

class classname(commands.Cog):
	bot:commands.Bot
	def __init__(self,bot:commands.Bot):
		self.bot=bot

	#  write your code here
	@commands.Cog.listener()
	async def on_ready(self):#  當DCbot啟動
		pass

async def setup(bot:commands.Bot):#  cogs被載入時，會執行這個函式
	if(not enable):
		return	
	await bot.add_cog(classname(bot))
```

# event 事件
## on_ready 當DCbot啟動成功
`main.py`
```py
@DCbot.event
async def on_ready():#  當DCbot啟動
	#  command here
	pass
```
`cogs/filename.py`
```py
@commands.Cog.listener()
async def on_ready(self):#  當DCbot啟動
	#  command here
	pass
```
## on_message 當有人傳送訊息
`main.py`
```py
@DCbot.event
async def on_message(message):#  當有人傳送訊息
	#  command here
	pass
```
`cogs/filename.py`
```py
@commands.Cog.listener()
async def on_message(self,message):#  當有人傳送訊息
	#  command here
	pass
```
## slash command 斜線指令
`main.py`
```py
@DCbot.tree.command(name="指令名稱",description="指令說明")
@DCbot.tree.describe(參數名="參數說明",參數名2="參數說明",......)
async def 函數名稱可任意(interaction:discord.Interaction,參數名:參數類型=參數初始值,參數名2......)
	pass

@DCbot.tree.command(name="command",description="這是一個指令")
@DCbot.tree.describe(a="只是一個參數")
async def command(interaction:discord.Interaction,a:int=0):
	await interaction.response.send_message(f"你輸入了一個指令，參數a={a}")
```
`cogs/filename.py`
```py
@app_commands.command(name="指令名稱",description="指令說明")
@app_commands.describe(參數名="參數說明",參數名2="參數說明",......)
async def 函數名稱可任意(interaction:discord.Interaction,參數名:參數類型=參數初始值,參數名2......)
	pass

@app_commands.command(name="command",description="這是一個指令")
@app_commands.describe(a="只是一個參數")
async def command(interaction:discord.Interaction,a:int=0):
	await interaction.response.send_message(f"你輸入了一個指令，參數a={a}")
```

# Class 類別整理

## `discord` `module`
最基本的discord模組，用來連接discord伺服器


## `discord.Interaction` `class`
使用者輸入斜線指令時，會產生一個interaction物件

## `discord.Message` `class`
代表一個訊息
- `tts` : `bool` = 是否為TTS朗讀訊息
- `content` : `str` = 訊息內容
- `author` : `discord.Member` = 訊息作者
- `channel` : `(Union)` = 訊息所在的頻道，類型可能是下表其一
	- `discord.TextChannel`
	- `discord.StageChannel`
	- `discord.VoiceChannel`
	- `discord.Thread`
	- `discord.DMChannel`
	- `discord.GroupChannel`
	- `discord.PartialMessageable`
- `guild` : `discord.Guild` = 訊息所在的伺服器
- `id` : `int` = 訊息ID
- `embeds` : `List[discord.Embed]` = 訊息中的嵌入
- `mentions` : `list[discord.user]` = 訊息中提及的使用者
- `mention_everyone` : `bool` = 是否提及了所有人
- `channel_mentions` : `list[discord.TextChannel]` = 訊息中提及的頻道
- `role_mentions` : `list[discord.Role]` = 訊息中提及的身分組
- `reference` : `Optional[discord.MessageReference]` = 回復的訊息
- `webhook_id` : `Optional[int]` = 訊息的webhook ID



## `discord.TextChannel` `class`
代表一個文字頻道
- `name` : `str` = 頻道名稱
- `guild` : `discord.Guild` = 頻道所在的伺服器
- `id` : `int` = 頻道ID
- `category` : `discord.CategoryChannel` = 頻道所在的分類
- `position` : `int` = 頻道在分類中的位置（從0開始）
- `last_message` : `discord.Message` = 最後一則訊息的ID
- `slowmode_delay` : `int` = 頻道的慢速模式CD時間（秒）
- `nsfw` : `bool` = 是否為年齡限制頻道

- `async for ... in history()`: 歷史訊息
	- `limit` : `int` = 訊息數量上限
	- `before` : `Union[discord.Message, datetime.datetime]` = 訊息ID或時間，取得該訊息之前的訊息
	- `after` : `Union[discord.Message, datetime.datetime]` = 訊息ID或時間，取得該訊息之後的訊息
	- `around` : `Union[discord.Message, datetime.datetime]` = 訊息ID或時間，取得該訊息附近的訊息
	- `oldest_first` : `bool` = 是否從舊到新
		```py
		async for message in channel.history(limit=200):
			print(message.content)
		```

## `discord.User` `class`
代表一個使用者、帳號
- `name` : `str` = 使用者名稱（可以拿來加好友的那個）
- `id` : `int` = 使用者ID
- `discriminator` : `str` = 使用者的識別碼（已棄用）
- `global_name` : `Optional[str]` = 使用者的全域暱稱，優先於使用者名稱顯示（顯示名稱，不能用來加好友）
- `bot` : `bool` = 是否為機器人帳號（ `True` = 是機器人）
- `system` : `bool` = 是否為系統帳號（ `True` = 是系統帳號）

## `discord.Asset` `class`
代表一個CDN資產
- `url` : `str` = 資產的URL
- `key` : `str` = 資產的key
- `is_animated()` : `fn` : `bool` = 是否為動態圖片 ex. gif
- `await to_file(...)` : `fn` : `discord.File` = 將資產轉換為可以用來傳送的檔案，例如 `Channel.send(file=asset.to_file())`。參數如下：
	- `filename` : `Optional[str]` = 檔案名稱
	- `description` : `Optional[str]` = 檔案描述
	- `spoiler` : `bool` = 是否為隱藏檔案（ `True` = 隱藏，點一下才能看到）
	



[`channel`]: #channel
[`user`]: #user
