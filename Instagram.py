import requests
import random
import os
os.system('pip install pyfiglet')
os.system('pip install requests')
os.system('pip install webbrowser')
os.system('pip install user_agent')
os.system('pip install getuseragent')
os.system('clear')
import requests
import random
import pyfiglet
import webbrowser
import sys
import time
from random import randint
from user_agent import generate_user_agent as ua
from getuseragent import UserAgent

def to(s):
    for char in s + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0625)
        return None
        
#------------logo ------------#
logo = (f"""
\033[1;32m╔══════════════════════════════════════════════════════════╗\033[1;93m
\033[1;32m║	         \033[1;93m ─━<🌺𝐀𝐒𝐒𝐀𝐋𝐀𝐌𝐔 𝐖𝐀𝐋𝐀𝐈𝐊𝐔𝐌🌺>━─\033[1;32m	           ║
\033[1;32m╔══════════════════════════════════════════════════════════╗
\033[1;32m║\033[0;92m:     ██ ██████      ███████ ██ ██████  ██████  ██ ██   ██ 
\033[1;32m║\033[0;97m:     ██ ██   ██     ██      ██ ██   ██ ██   ██ ██ ██  ██  
\033[1;32m║\033[0;91m:     ██ ██████      ███████ ██ ██   ██ ██   ██ ██ █████   
\033[1;38m║\033[0;94m:██   ██ ██               ██ ██ ██   ██ ██   ██ ██ ██  ██  
\033[1;32m║\033[0;93m: █████  ██          ███████ ██ ██████  ██████  ██ ██   ██ 
\033[1;32m╚══════════════════════════════════════════════════════════╝
\033[1;32m╔══════════════════════════════════╗╔══════════════════════╗
\033[1;32m║𝐍𝐎𝐓𝐄 :\033[37;41m𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐈𝐒 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌-𝐋𝐈𝐊𝐄\033[0;m\033[1;32m║║        \x1b[1;91m___T_\033[1;32m         ║
\033[1;33m║══════════════════════════════════║║       \x1b[1;91m| o o |\033[1;32m        ║
\033[1;36m║𝐀𝐔𝐓𝐇𝐎𝐑    : 𝐉𝐏-𝐒𝐈𝐃𝐃𝐈𝐊-𝐊𝐇𝐀𝐍        ║║       \x1b[1;91m|__-__|\033[1;32m        ║
\033[1;35m║══════════════════════════════════║║       \x1b[1;91m/| []|'\033[1;32m        ║
\033[1;33m║𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  : 𝟎𝟏𝟖𝟑𝟏𝟕𝟕𝟑𝟔𝟖𝟖           ║║     \x1b[1;91m()/|___|\()\033[1;32m      ║
\033[1;37m║══════════════════════════════════║║        \x1b[1;91m|_|_|\033[1;32m         ║
\033[1;38m║𝐆𝐈𝐓𝐇𝐔𝐁    : 𝐉𝐏-𝐒𝐈𝐃𝐃𝐈𝐊-𝟏𝟒𝟑         ║║       \x1b[1;91m|_| |_|\033[1;32m        ║
\033[1;36m║══════════════════════════════════║║                      ║
\033[1;31m║𝐒𝐄𝐑𝐕𝐄𝐑    : 𝐃𝐀𝐓𝐀 : 𝐖𝐈𝐅𝐈 :𝐖𝐎𝐑𝐊𝐈𝐍𝐆  ║╚══════════════════════╝
\033[1;32m║══════════════════════════════════════════════════════════╗
\033[0;97m║𝐔𝐏𝐃𝐀𝐓𝐄 : 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 𝟏.𝟏\033[1;32m                                    ║
\033[1;34m║══════════════════════════════════════════════════════════║
\033[1;35m║𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐋𝐈𝐍𝐊 : \x1b[1;91\https://www.facebook.com/rxsiddik1\033[1;32m        ║
\033[1;36m╚══════════════════════════════════════════════════════════╝\033[1;37m""") 
def linex():
    print(f'{ran}-----------------------------------{w}')
   
ua = UserAgent('ios').Random()
print (logo)
user = input('[+] InstaGram UserName : ')
link = input('[+] Post Link : ')
print('')
res = requests.post('https://api.likesjet.com/freeboost/7', json = {
    'instagram_username': user,
    'link': link,
    'email': f'''srk{random.randint(100000, 999999)}@gmail.com''' }, headers = {
    'Host': 'api.likesjet.com',
    'content-length': '137',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?1',
    'user-agent': ua,
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://likesjet.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://likesjet.com/',
    'accept-language': 'en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5' }).json()
print(res['message'])
print(f"\x1b[38;5;82m: \033[31;1m[√] Successfully 50 Like send")
