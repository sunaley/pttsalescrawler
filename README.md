# pttsalescrawler
抓PTT網頁版各大買賣版關鍵字標題，藉由MQTT Broker傳遞資訊。
我用來傳到手機的MQTT Client，並馬上

#使用說明
bsPTT.py說明
        //MQTT Broker
        MQTT_BROKER = ""
        //在Broker上同Topic都會收到同一訊息  
        MQTT_TOPIC = ""   
        //要抓取的PTT網頁版URL
        PTTBOARD_URL = "https://www.ptt.cc/bbs/HardwareSale/index.html"

以下5為代表PTT網頁版前五頁
```pytonh
GetURL(PTTBOARD_URL, 5, itemList, matchItems)  
```
items.json說明
        //輸入要收尋的品名
        "check_str": ["i3", "I3"]
        //買賣類別
        "type": "賣"

