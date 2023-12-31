
# 名詞定義
`list`
```py
[1,2,3,4,5]
```
`dict`
```py
{"a":1,"b":2,"c":3}
```
`fn`
```py
def fn(a,b):
	return a+b
```
`str`
```py
"hello world"
```
`int`
```py
1
```


# 初始設定、ㄐㄐ人權限
```py
discord.Intents.all()#  設定ㄐㄐ人權限
DCbot_client=discord.Client(intents=intents)
DCbot_client.run(token)# 連線
```

# 請注意，每個fn好像都需要加await，且必須在機器人啟動時才能使用，例如
```py
@DCbot_client.event
async def on_ready():
	await DCbot_client.get_user(userid).send("hello world")

DCbot_client.start(token)

#  以下為錯誤示範
DCbot_client.get_user(userid).send("hello world")#  runtime error
```

使用方法：  
假如我要用的東西，結構如下：  
> `DCbot_client`
> - `user`
> 	- 內部物件為 [`user`]
> 
> `user`
> 	- `id`

那我可以用下方程式碼獲取我想要的東西    
```py
DCbot_client.user.id
```

## `DCbot_client`
- `user` bot的使用者名稱
	- 內部物件為 [`user`]
- `guilds` `list` 伺服器列表
	- `id` `int` 伺服器id
	- `name` `int` 伺服器名稱
	- `owner` `str` 伺服器擁有者
	- `channels` `list` 伺服器列表
		- 內部物件為 [`channel`]
	- `categories` `list` 頻道類別
		- 內部物件為 [`channel`]
	- `members` `list` 成員列表
		- 內部物件為 [`user`]


## `channel`
- `category` `int` 頻道類別id
- `id` `int` 頻道id
- `name` `str` 頻道名稱
- `send(msg)` `fn` 傳送訊息

## `user` 使用者名稱（可用這個名稱加別人好友）
- `id` `int` 使用者id
- `global_name` `str` 顯示名稱
- `name` `str` 使用者名稱，同[`user`]
- `nick` `str` 暱稱
- `bot` `bool` 是否為機器人（`True` 是機器人）
- `send(msg)` `fn` 傳送訊息

[`channel`]: #channel
[`user`]: #user
