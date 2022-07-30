'''
MongoDB shell version v5.0.9
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("0e264885-7b61-408a-a735-447709cac856") }
MongoDB server version: 5.0.9
================
Warning: the "mongo" shell has been superseded by "mongosh",
which delivers improved usability and compatibility.The "mongo" shell has been deprecated and will be removed in
an upcoming release.
For installation instructions, see
https://docs.mongodb.com/mongodb-shell/install/
================
---
The server generated these startup warnings when booting: 
        2022-07-10T21:36:49.279+09:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
        2022-07-10T21:36:50.708+09:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
        2022-07-10T21:36:50.708+09:00: /sys/kernel/mm/transparent_hugepage/enabled is 'always'. We suggest setting it to 'never'
---
---
        Enable MongoDB's free cloud-based monitoring service, which will then receive and display
        metrics about your deployment (disk utilization, CPU, operation statistics, etc).

        The monitoring data will be available on a MongoDB website with a unique URL accessible to you
        and anyone you share the URL with. MongoDB may use this information to make product
        improvements and to suggest MongoDB products and deployment options to you.

        To enable free monitoring, run the following command: db.enableFreeMonitoring()
        To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---

# 기본 개념
https://www.youtube.com/watch?v=81JnYGT2HVQ

# 키워드
인덱스는 적절히, master-slave 가능, 샤딩

# 사용법 - https://velopert.com/457
- db 생성 > use {명}
- 현재 db 확인 > db
- db 보기 > show dbs
- db에 document 추가 > db.{collection명}.insert({"":""})
- 현재 접속 중인 db 제거 > db.dropDatabase()
- 현재 접속 중인 db에 collection 생성 > db.createCollection({collection명}, [options])
- 현재 접속 중인 db에 특정 collection 제거 > db.{collection명}.drop()
... 등
database > collection > document > field
>>> use {database명} >  db.{collection명}.insert(다양한 field로 구성된 json 형태의 document)

# crud
db.person.save({"":""})
db.person.find()
db.person.update()
db.person.remove({"":""})

'''

from pymongo import MongoClient, GEO2D
import pprint


# 전체 저장한다면
db_client = MongoClient(host='localhost', port=27017)
col_cafenow = db_client['cafenow']

cafe_insert = col_cafenow.cafe
# cafe_id = cafe_insert.insert_one({
#     "detailed": detailed_data,
#     "location": {
#         'type': "Point",
#         "coordinates": [float(info_selected[2]), float(info_selected[3])]
#     }
# })
location_insert = col_cafenow.location
# location_insert.create_index([("loc", GEO2D)])
# location_id = location_insert.insert_one({
#     "cafe_id": id_selected,
#     "loc":  [float(info_selected[2]), float(info_selected[3])]
# })


for doc in location_insert.find({"loc": {"$near": [3, 6]}}).limit(3):
    pprint.pprint(doc)


# document -----------------------------------------------------------------------------------
cafeInfo = {
    "_id": "-",              # document 내장    
    "idApi": "-",          # api에 등록된 카페 id - 중복 제거
    "placeName": "-",      # 카페 이름    
    "loc": [float("lat"), float("lon")],    # 위도, 경도
    "likes": "-",       # 좋아요 - 좋아요 액션에 자동 조정
    "Score": 5,       # 평점 - 평점 입력 시 자동 조정
    "01": 5,
    "02": 5,
    "03": 5,
    "04": 5,
    "timeCreated": "-",
    "timeUpdated": "-",
} # unique
# db.cafeInfo.create_index({ "idApi": 1 }, { unique: true })
# db.cafeInfo.create_index([("loc", GEO2D)])    # 위치 정보

cafeLikes = {
    "_id": "-",              
    "cafeId": "-",          # api에 등록된 카페 id
    "userId": "-",          # user document의 ObjectId 
    "timeCreated": "-",
    "timeCanceled": "-",
}
# db.cafeLikes.create_index({ "idApi": 1 }, { unique: true })
# cafeId & userId 중복 방지 

cafeScores = {
    "_id": "-",
    "cafeId": "-",          # cafeIfo의 ObjectId
    "userId": "-",          # user document의 ObjectId 
    "timeCreated": "-",
    "01": 5,
    "02": 5,
    "03": 5,
    "04": 5,
}
# cafeId & userId 중복 방지 

comments = {
    "_id": "-",
    "cafeId": "-",          # cafeIfo의 ObjectId
    "userId": "-",          # user document의 ObjectId 
    "comment": "-",
    "timeCreated": "-",
    "timeDeleted": "-",
}

users = { # 도경님 껄로 대체
    "_id": "-",
    "user_name": "-",    
    "socialLogin": False,    
    "age": 30,
    "sex": 0,   # male 0, female 1
    "timeSignedIn": "-",
    "timeDeactivated": "-",
}