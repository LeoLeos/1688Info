#coding:utf-8
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import re
import time
import os

# header
cookies = ''
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookies,
}

#获取搜索商品的ID
def getproductid(search):
    # 搜索商品首页链接
    url = 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?spm=a2609.11209760.j661dm7m.234.44292de1JhLZNK&cosite=&keywords=' + search + '&trackid=&location='
    # %E7%94%B7%E8%A3%85

    search_product_info = requests.get(url=url, headers=header)
    context_search_product_info = search_product_info.content.decode('utf-8')
    # print(context_search_product_info)
    # 正则查找listOffer
    pattern = re.compile('"infoId":"(.*?)","loginId"', re.S)
    # 获取商品ID详情
    Allshopid = re.findall(pattern, context_search_product_info)
    # print(Allshopid)

    search_etree = etree.HTML(context_search_product_info)
    search_etreetext = search_etree.xpath('/html/head/text()')
    # print(search_etreetext)
    return Allshopid


def getContact(shopid):
    # 商品详情链接
    url_product_info = 'https://detail.1688.com/offer/'+ shopid +'.html?spm=a312h.2018_new_sem.dh_002.1.603d607eCstWOJ&tracelog=p4p&clickid=cb8ccfd0bf3642fdb3340752d7aa5d23&sessionid=4dee4799abff737fd63b301e551a5264'
    # 获取实时观看人数
    Request_Work_info = requests.get(url=url_product_info, headers=header)
    # AllInfo = json.loads(Request_Work_info)
    # print(AllInfo)
    context = Request_Work_info.content.decode('gbk')
    # print(context)

    con = etree.HTML(context)
    # 商品url
    shopurl = con.xpath('//*[@id="ali-masthead-v6"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/a/@href')
    if shopurl != []:
        print('商铺链接：',end='')
        print(shopurl)
        # 商铺名称
        shopname = con.xpath('//*[@id="ali-masthead-v6"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/a/div/text()')
        print('商铺名',end='')
        print(shopname)
    else:
        shopurl = con.xpath('//*[@id="ali-masthead-v6"]/div/div[2]/div[1]/div[1]/div[1]/a/@href')
        shopname = con.xpath('//*[@id="ali-masthead-v6"]/div/div[2]/div[1]/div[1]/div[1]/a/div/text()')
        print('商铺链接：',end='')
        print(shopurl)
        print('商铺名',end='')
        print(shopname)

    # 进入商铺联系页面
    contactHtmlRespone = requests.get(url=shopurl[0]+'/page/contactinfo.htm', headers=header)
    contactHtmlcontext = contactHtmlRespone.content.decode('gbk',errors='ignore')
    contextetree = etree.HTML(contactHtmlcontext)
    contactnumber = contextetree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/dl[1]/dd/text()')
    print('商家电话号码',end='')
    print(contactnumber)

    #进入商品首页
    shopinfo = requests.get(url=shopurl[0], headers=header)
    shopinfo_context = shopinfo.content.decode('gbk', errors='ignore')
    shopinfo_etree = etree.HTML(shopinfo_context)
    shop_contact = shopinfo_etree.xpath('//*[@id="site_content"]/div[2]/div[5]/div/div[2]/dl[1]/dd/text()')
    shop_people = shopinfo_etree.xpath('//*[@id="site_content"]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/span/a/text()')
    print('联系电话：'+str(shop_contact))
    print('联系人：'+str(shop_people))
    if not os.path.exists('1688商家信息.csv'):
        with open('1688商家信息.csv','a') as f:
            f.write('%s,%s,%s,%s,%s' % ('商家链接', '商家名称', '商家联系方式', '联系人','联系电话'))
            f.write('\n')
            f.close()
    with open('1688商家信息.csv','a') as f:
        f.write('%s,%s,%s,%s,%s' % (shopurl, shopname, shop_contact, shop_people,contactnumber))
        f.write('\n')
        f.close()

count = 0
keyword = '电脑'
# 获取商品id
Allshopid = getproductid(keyword)
# print(Allshopid)

for i in Allshopid:
    count += 1
    print('第'+ str(count) + '次')
    getContact(i)
    time.sleep(1)
