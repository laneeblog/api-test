import os
import requests
import json


'''
1. 타이핑 할 때마다 주소 및 키워드로 나오는 결과를 리스트로 받아서 선택 옵션으로 제시
2. 옵션 중 하나를 선택하면 해당 id로 영업점 정보 가져와서 필요한 정보 추출

'''

# 설정
keyword_api = "https://dapi.kakao.com/v2/local/search/keyword.json"
address_api = "https://dapi.kakao.com/v2/local/search/address.json"
detailed_url = "https://place.map.kakao.com/main/v/"
rest_api_key = os.environ["KAKAO_REST_API_KEY"]
headers = {"Authorization": f"KakaoAK {rest_api_key}"}

def get_query_result(code, input_text):
    data = {"query": input_text}
    api = keyword_api if code == 0 else address_api # 0 - keyword, 1 - address
    return json.loads(requests.get(api, headers=headers, data=data).text)['documents']


# 사용자가 키워드 또는 주소를 입력하면 
input_text = "청담 스타벅스" # "전북 삼성동 100"
keyword_result = get_query_result(0, input_text)
address_result = get_query_result(1, input_text)
total_result = keyword_result + address_result

# 입력한 내용으로 검색된 결과를 선택할 수 있게 제공
list_for_selection = []
for i, r in enumerate(total_result):
    id = r['id'] if 'id' in r else get_query_result(0, address)[0]['id']
    address = r['address_name']
    x = r['x']
    y = r['y']
    list_for_selection.append((id, address, x, y))
    if i == 5:
        break
set_temp = set(list_for_selection) 
list_for_selection = list(set_temp)

# 사용자가 그 중에 하나를 선택하면 id 를 받아서 상세 정보 가져온 후
info_selected = list_for_selection[0]
id_selected = info_selected[0]
detailed_data = json.loads(requests.get(detailed_url + id_selected, headers=headers).text)
basicInfo = detailed_data['basicInfo'] # placenamefull, mainphotourl, phonenum, address조합, homepage, tags, wpointx-y
blogReview =detailed_data['blogReview'] # list
comment = detailed_data['comment'] # list
menuInfo = detailed_data['menuInfo'] # menuList
photo = detailed_data['photo'] # photoList[0]['list']

# 카페 정보 입력 시 필요한 정보 추출




