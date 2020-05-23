'''
    有道翻译
'''
import requests
import time,random
from hashlib import md5

class YdSpider:
    def __init__(self):
        self.url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "251",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": "OUTFOX_SEARCH_USER_ID=-369496913@10.108.160.19; JSESSIONID=aaaRTXUlLGvgLh9cCe8dx; OUTFOX_SEARCH_USER_ID_NCOO=1151966975.930748; ___rl__test__cookies=1584783177268",
                "Host": "fanyi.youdao.com",
                "Origin": "http://fanyi.youdao.com",
                "Referer":"http://fanyi.youdao.com/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
}


    def get_ts_salt_sign(self,word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        s = md5()
        s.update(string.encode())

        sign = s.hexdigest()

        return ts,salt,sign

    def attack_yd(self,word):
        ts,salt,sign = self.get_ts_salt_sign(word)
        data = {
                "i": word,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": salt,
                "sign": sign,
                "ts": ts,
                "bv": "94ef9c063d6b2a801fab916722d70203",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME"
}
        html = requests.post(url=self.url,data=data,headers=self.headers).text
        print(html)

    def run(self):
        word = input('请输入要翻译的单词:')
        self.attack_yd(word)


if __name__ == '__main__':
    spider = YdSpider()
    spider.run()




