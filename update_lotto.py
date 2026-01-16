import requests
import json

def update():
    url = f"https://www.dhlottery.co.kr/lt645/selectPstLt645Info.do?srchLtEpsd=all&_=1700000000000"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    
    res = requests.get(url, headers=headers)
    res_json = res.json()
    with open("lotto_data.json", "w", encoding="utf-8") as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    update()
