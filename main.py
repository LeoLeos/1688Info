import requests
import json

url = 'https://detail.1688.com/offer/560269650740.html?spm=a26239.11617082.jhyjeg61.1.4db65782WkdurY&sk=consign'
cookies = 'cna=lVToF93nVx0CARsvqYKBdW/d; cookie2=15931d685fc67e1e85e13a1cb951505d; hng=CN%7Czh-CN%7CCNY%7C156; t=b1f7bcb1973d961cd9be0a34a986423f; _tb_token_=ee5eeb73a06e5; __cn_logon__=false; xlly_s=1; alicnweb=touch_tb_at%3D1604651917594; UM_distinctid=1759cbffa8c5f9-0ccf92b0b3dcc8-230346d-1fa400-1759cbffa8dafd; _csrf_token=1604652629717; taklid=b51ce7ad429c45aba5f6c5a1b6f5ef25; ali_ab=27.47.171.92.1604652630595.8; CNZZDATA1253659577=1355996455-1604647295-https%253A%252F%252Fp4psearch.1688.com%252F%7C1604651610; JSESSIONID=CD25A741DC8C2D1EE3C6003D8BE47819; tfstk=cc0fB2ThCtXXXrxNujOzg9Z35nzNZk5Q1nwmGmnJ48p98RhfiXQUd75mjOQ8v71..; l=eBLMJ2kgO-zskx7MBOfwnurza77tQIRAguPzaNbMiOCP_y1H5nIfWZS5jyYMCnGVh6r6R3Rj0APzBeYBqIcidj4pTs4cCOHmn; isg=BAQE8VSYB1KUw7OexR-C5-wA1YL2HSiHVqJF_h6lhk-SSaQTRi_gFrvvieGR0WDf'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookies,
}
# 获取实时观看人数
Request_Work_info = requests.get(url=url, headers=header)
# AllInfo = json.loads(Request_Work_info)
# print(AllInfo)
context = Request_Work_info.content.decode('gbk')
with open('ddd.txt','a') as f:
    f.write(context)
