import requests
import time
import random
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def send_message(data):
    bottoken = "5599692359:AAEn8-k3t2kFoTLvGEPrqiMumB77VcrNGOI"
    url = "https://api.telegram.org/bot" + bottoken + "/sendMessage"
    res = requests.post(url=url, headers={}, files=data)
    

def send():
    if datetime.datetime.now().minute == 0:    
        data = {
            'text': (None, f'SendPostNotification'),
            'chat_id': (None, -1001773405336),
            'parse_mode': (None, 'Markdown')}
        send_message(data)


scheduler = BlockingScheduler()
scheduler.add_job(send, 'interval', minutes=1)
scheduler.start()
