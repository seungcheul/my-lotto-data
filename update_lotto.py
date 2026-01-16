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
    url = f"https://www.dhlottery.co.kr/lt645/selectPstLt645Info.do?srchLtEpsd={round_no}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        res = requests.get(url, headers=headers)
        data = res.json()
        
        if data.get("drwNo"):
            # 기존 데이터 읽기
            file_path = "lotto_data.json"
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    all_data = json.load(f)
            else:
                all_data = {}

            all_data[str(round_no)] = data
            
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(all_data, f, ensure_ascii=False, indent=4)
            print(f"Success: {round_no}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update()
