import requests
import json
import os
from datetime import datetime

def update():
    # 현재 날짜 기준 회차 계산 (대략적인 계산)
    first_date = datetime(2002, 12, 7)
    now = datetime.now()
    round_no = (now - first_date).days // 7 + 1
    
    # 질문자님이 찾으신 상세 URL
    url = f"https://www.dhlottery.co.kr/lt645/selectPstLt645Info.do?srchLtEpsd=1206&_=1700000000000"
    headers = {"User-Agent": "Mozilla/5.0"}


    res = requests.get(url, headers=headers)
    res_json = res.json()
    
    file_path = "lotto_data.json"

    print("!!res_json")
    print(res_json)
    
    # 기존 데이터 읽기
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                all_data = json.load(f)
            except:
                all_data = {}
    else:
        all_data = {}

    print("!!all_data")
    print(all_data)


    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    print(f"✅ 업데이트 성공!")



if __name__ == "__main__":
    update()
