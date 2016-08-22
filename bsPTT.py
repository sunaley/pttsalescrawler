# -*- coding: utf-8 -*-
import sys, time, requests, json, os
import paho.mqtt.client as mqtt
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def readItems():
    with open('items.json', 'r', encoding='utf-8') as fin:
        data = json.loads(fin.read())
    data = data['items']
    return data

def checkItems(content, data):
    for item in data:
        if item['type'] in content:
            for x in item['check_str']:
                if x in content:
                    return True

def GetURL(URL, i, itemList, data):
    URL_parser_result = urlparse(URL)
    if 'http' in URL_parser_result.scheme: 
        leftURL = '%s://%s/' %(URL_parser_result.scheme, URL_parser_result.netloc)
    if i > 0:
        try:
            f = requests.get(URL)
        except:
            mqttc.publish(MQTT_TOPIC, 'connection error')
    
        soup = BeautifulSoup(f.text, 'lxml')
        #get all a href tag
        for text in soup.find_all('a'): 
            if checkItems(text.contents[0], data):
                #send new item info to broker
                if text.contents[0] not in itemList: 
                    mqttc.publish(MQTT_TOPIC, text.contents[0])
                    itemList.append(text.contents[0])
            if "‹ 上頁" in text.contents[0]:
                #get pre page URL
                URL = leftURL + text.get('href') 
    else:
        return
    i = i - 1
    time.sleep(1)
    GetURL(URL,i,itemList,data)

MQTT_BROKER = "54.85.158.111"
MQTT_TOPIC = "ptt/hardwaresale"

if __name__ == '__main__':
    

    cnt = 0
    itemList = []
    mqttc = mqtt.Client("python_pub")
    mqttc.connect(MQTT_BROKER, 1883, keepalive=60)

    matchItems = readItems()

    while True:
        #get item
        GetURL("https://www.ptt.cc/bbs/HardwareSale/index.html", 5, itemList, matchItems)  
        cnt = cnt + 1
        i = 0
        sys.stdout.write("Done: #" + str(cnt) + " " + str(i) + " seconds\r")
        while i <= 120:
            sys.stdout.write("Done: #" + str(cnt) + " " + str(i) + " seconds\n")
            for x in itemList:
                sys.stdout.write(x + '\n')
            sys.stdout.flush()
            time.sleep(1)
            os.system('clear')
            i = i + 1   

        mqttc.reconnect()
         