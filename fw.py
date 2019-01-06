from requests import get

url = "https://www.jleague.jp/en/match/search/j1/all/"

response = get(url)
print(response.status_code)
