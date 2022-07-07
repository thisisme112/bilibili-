import requests
from bs4 import BeautifulSoup
import re

url = "https://www.bilibili.com/v/popular/rank/all"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}
resp = requests.get(url, headers=header)
resp.close()
obj = re.compile(r'<a class="title" href="//(?P<url>.*?)" target="_blank">(?P<title>.*?)'
                 r'</a>.*?<a href="//(?P<space>.*?)".*?'
                 r'/>(?P<name>.*?)</span></a>', re.S)
rank = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 从bs对象查找数据
# find(标签, 属性=值)
# find_all
# result = rank.find("ul", attrs={"class": "rank-list"})
item = rank.find_all("div", attrs={"class": "info"})

i = 0
while i < (len(item)):
    video = obj.finditer(str(item[i]))
    i += 1
    for it in video:
        print("排名为"+str(i)+"的视频")
        print("up主:", it.group("name").strip())
        print("标题:", it.group("title"))
        print("视频地址:", it.group("url"))
        print("up空间:", it.group("space"))
        print("========================")
