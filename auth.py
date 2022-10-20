import time
import requests
from dhooks import Webhook, Embed
webhook = ''
link = ''
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
