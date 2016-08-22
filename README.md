# pttsalescrawler
抓PTT網頁版各大買賣版關鍵字標題，藉由MQTT Broker傳遞資訊。
我用來傳到手機的MQTT Client，就可馬上登入PTT回覆信箱

#使用說明
##bsPTT.py說明<br />
```python
#MQTT Broker<br />
MQTT_BROKER = ""<br />
#在Broker上同Topic都會收到同一訊息  <br />
MQTT_TOPIC = ""<br />   
#要抓取的PTT網頁版URL<br />
PTTBOARD_URL = "https://www.ptt.cc/bbs/HardwareSale/index.html"<br />
#以下5為代表PTT網頁版前五頁
GetURL(PTTBOARD_URL, 5, itemList, matchItems)  
```

##items.json說明<br />
check_str為要搜尋的品項<br />
type為買賣類別<br />
    "check_str": ["i3", "I3"]<br />
    "type": "賣"<br />
    


