import requests

res = requests.get("http://www.pythonhow.com/data/universe.txt")
res_txt = res.text.strip()
print(res_txt.count('a'))