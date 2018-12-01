import requests
import json
login_url = 'http://192.168.255.19/0.htm'

requst_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Language=zh_CN; JSESSIONID=LKBj0xsbtxtfgbXlW8S9sOErvvp3akfFHD6_BkcHs59CMxkaHncM!-345465670; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    'Host': '192.168.255.19',
    'Origin': 'http://192.168.255.19',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
    'Referer': 'http://192.168.255.19/0.htm'
}

form_data = {
    'DDDDD': 'zc1',
    'upass': '741963',
    '0MKKey': '(unable to decode value)'
}

sessions = requests.Session()
response = sessions.post(login_url,data=form_data,headers=requst_header)

print(response.text)