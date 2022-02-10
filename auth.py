import time
import requests
from dhooks import Webhook, Embed
webhook = 'https://discord.com/api/webhooks/941192613321654292/I_h8uR1g7oOakwtKaC7spUl0gawQ1gE8kZIxF4P4TxRAB5nZGvgnL2B7-QoSfVNZiZ82'
#token = '6eb26e56-1a02-41ec-891e-d3d2d1c87b3d'
link = 'https://pastebin.com/raw/pxdyiiD9'
auth = requests.get(link).text
hook = Webhook(webhook)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
token = input('enter token >')
try:
    if token in auth:
        print('authed')
        embed=Embed(title='Successful User Login', description=f'{current_time}')
        hook.send(embed=embed)
        time.sleep(1)
    else:
        print('invalid token')
        embed=Embed(title='Invalid User Login', description=f'Token Used: {token}')
        hook.send(embed=embed)
        time.sleep(1)
    
except:
    print("ERROR: CAN'T CONNECT")
    time.sleep(1)