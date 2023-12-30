# 建立bot
先到<https://discord.com/developers>  
先建立一個應用程式  
![Alt text](image/image.png)  
![Alt text](image/image-1.png)  
建立bot  
![Alt text](image/image-2.png)  
打開 `cfg.json`，把Token貼上去，避免忘記  
![Alt text](image/image-4.png)  
把這三個勾起來  
![Alt text](image/image-5.png)  
p.s. 第12部是設定bot的權限，可視需要自行調整
![Alt text](image/image-6.png)  
p.s. 第15部是設定bot的權限，可視需要自行調整
![Alt text](image/image-7.png)  
他會產生bot邀請連結，你可以把它加入至你有管理權限的伺服器
![Alt text](image/image-8.png)  
連到該網址，把ㄐㄐ人加到你要的server  
![Alt text](image/image-10.png)  


# 連線bot
1. 修改 `cfg.json` 內的token
2. 將 `cfg.json` 移動到 `../cfg.json`
3. 執行 `python3 main.py`  
4. `main.py` 會隨時輸出誰在哪裡傳了什麼訊息  
	![Alt text](image/image-9.png)