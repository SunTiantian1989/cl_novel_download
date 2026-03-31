import time
import requests
import re
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def obtain_title(url):
    time.sleep(2)
    res = requests.get(url, headers=headers)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    tag_title = soup.find('title')
    title = tag_title.text
    title = re.findall('(.*?) - 成人', title)[0]
    return title

def obtain_page_content(url):
    time.sleep(2)
    res = requests.get(url, headers=headers)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    content_list = soup.find_all('div', class_="tpc_content")
    return content_list    

if __name__ == '__main__':
    # obtain title
    url_base='https://t66y.com/read.php?tid=7187084&toread=2'
    max_page=12+1
    title=obtain_title(url_base+'&page='+str(1))
    # title = re.sub('(：|\xa0)', ' ', title)
    print('题目：'+title) 
    try:
        with open(title+'.txt', 'w', encoding='utf-8')as file:
            for iPage in range(1,max_page):
                print('获取第'+str(iPage)+'页...')
                content_list=obtain_page_content(url_base+'&page='+str(iPage))
                for i in range(len(content_list)):
                    content=content_list[i].text
                    # recon = re.sub('<.*?>', '', content)
                    file.write(content)
        print('保存成功')
    except:
        print('保存失败')
    
    
