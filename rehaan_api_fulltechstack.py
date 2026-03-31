import urllib.request

try:
    response = urllib.request.urlopen("https://api.0x10.cloud/")
    headers = dict(response.info().items())

    if response is not None:
        print("\n  [!] VULNERABILITY FOUND")
        print("  Full Tech Stack API disclosed: ")
        for key, value in headers.items():
            print(f"    {key}: {value}")
    else:
        print("\n  [OK] NO VULNERABILITY FOUND")

except Exception as e:
    print(e)
