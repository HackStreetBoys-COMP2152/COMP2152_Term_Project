import urllib.request

target = "http://webhook.0x10.cloud/?url=https://webhook.site/fba40850-56bd-4fe0-8929-e348cdf168ed"

try:
    with urllib.request.urlopen(target) as response:
        print(response.read().decode())

except Exception as e:
    print(f"An error occurred: {e}")