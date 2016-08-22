# pttsalescrawler
抓PTT網頁版各大買賣版關鍵字標題，藉由MQTT Broker傳遞資訊。<br />
我用來傳到手機的MQTT Client，就可馬上登入PTT回覆信箱<br />
預設抓取網頁版前五頁資訊

#使用說明
##bsPTT.py說明<br />
```python
#MQTT Broker
MQTT_BROKER = ""
#在Broker上同Topic都會收到同一訊息  
MQTT_TOPIC = ""
#要抓取的PTT網頁版URL
PTTBOARD_URL = "https://www.ptt.cc/bbs/HardwareSale/index.html"
```

##items.json說明<br />
check_str為要搜尋的品項，此例為i3 I3<br />
type為買賣類別<br />

	"check_str": ["i3", "I3"]
	"type": "賣"



