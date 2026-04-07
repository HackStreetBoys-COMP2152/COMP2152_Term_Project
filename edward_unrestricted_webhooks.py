import urllib.request

target = "http://webhook.0x10.cloud/?url=https://webhook.site/e880f46f-049e-4cf3-b7da-073821af9f8e"

try:
    with urllib.request.urlopen(target) as response:
        print(response.read().decode())

except Exception as e:
    print(f"An error occurred: {e}")