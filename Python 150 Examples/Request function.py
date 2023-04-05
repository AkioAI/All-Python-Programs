import requests
r=requests.get("https://xkcd.com/1732/")
print(r.text)