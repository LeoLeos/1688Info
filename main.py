import requests
import json

url = 'https://detail.1688.com/offer/560269650740.html?spm=a26239.11617082.jhyjeg61.1.4db65782WkdurY&sk=consign'
cookies = ''
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
