#API HTTP Request User Credentials
#Rehaan Lachporia - 101594859
import urllib.request

target = "https://api.0x10.cloud/"
path = "users?id="
try:

    for count in range(1,101):
        response = urllib.request.urlopen(f"{target}{path}{count}")
        print(response.read().decode())
except Exception as e:
    print(e)