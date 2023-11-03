import requests

res = requests.get("https://pythonhow.com/media/data/universe.txt")

print(res.text)
