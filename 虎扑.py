import requests
from bs4 import BeautifulSoup as BS
import json
from requests.exceptions import RequestException
import time


def test_url(url):
    """
    测试连接是否为有效链接，如果是则返回链接，不是则返回None
    :param url:
    :return: r
    """
    try:
        headers = {
            "Cookie": "_HUPUSSOID=d3c5306a-42e2-4b1a-b671-b0d23f458f23; _dacevid3=f5ff9448.92a5.d92f.e68f.5e0dc14fac06; __gads=ID=5dc9da19a54287d4:T=1591515149:S=ALNI_MbVFjWdyb_On-7pfFaW-8gvwOSnqA; _CLT=918ebe7bb324d8673460f7af1d701a5c; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1593177762,1593177887,1593823283,1594561566; u=43985531|5pyA54ix5ZCr5oGp6Z2Z|0039|f5460e856bf236a634cb3a46ca4b8034|6bf236a634cb3a46|aHVwdV9kOGJmNzEzOGYxMzFmYjZk; us=d09c2ada5f50aae6cd9d5368463add73cbc1b73d32ab63431008770a39f3e39a7fb106d7902ec08cd4fb3344f0c0ccda6c98ff923aa277d1c7064e8dba001c4a; ipfrom=9611ab1289d5e565096778ecb74f0904%09Unknown; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221703f2e6373693-0565cb04ee8593-3a65420e-2073600-1703f2e63741f3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221703f2e6373693-0565cb04ee8593-3a65420e-2073600-1703f2e63741f3%22%7D; Hm_lvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1599360272,1599432719,1599487352,1599584358; ua=49987011; acw_tc=76b20f4815995843752241322e7fa97e8b0e6eae5405d72675147e7e4ebe1f; PHPSESSID=3a73054d1f64573fa3310a42ef18ea01; _cnzz_CV30020080=buzi_cookie%7Cf5ff9448.92a5.d92f.e68f.5e0dc14fac06%7C-1; Hm_lvt_4fac77ceccb0cd4ad5ef1be46d740615=1599360280,1599432736,1599487376,1599584378; Hm_lvt_c324100ace03a4c61826ef5494c44048=1599432856,1599487376,1599489160,1599584378; Hm_lpvt_4fac77ceccb0cd4ad5ef1be46d740615=1599584502; Hm_lpvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1599584502; Hm_lpvt_c324100ace03a4c61826ef5494c44048=1599584502; _fmdata=UIMGLCN9vW6mfXgYn3wl8X4wntlykeTeSzFvGFMyr1kv9f3C4G403C31IsBOQ9WL%2BBzpI0x3z%2BMs6qKvCg52BmgNDjPCgeyue8bS2wNjzEA%3D; lastvisit=1431%091599584602%09%2Fajax%2Flights.ajax.php%3F; __dacevst=6911a535.d7f986e1|1599586594718",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        s = requests.Session()
        r = s.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            return r
        else:
            return None
    except RequestException:
        return None


def parse_url(r):
    """
    该函数时一个生成器，解析链接，拿到想要的字符串（即帖子标题），
    :param r:
    :return:
    """
    soup = BS(r.text, "lxml")
    ts = (soup.find_all(name="a", attrs={"class": "truetit", "target": "_blank"}))
    for t in ts:
        content = t.string
        print(content)
        yield content


def write_to_file(content):
    """
    把帖子标题写入文档中，
    :param content:
    :return:
    """
    with open("hupu.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")


def main(page):
    url = "https://bbs.hupu.com/vote-" + str(page)
    valid_url = test_url(url)
    for d in parse_url(valid_url):
        write_to_file(d)


if __name__ == "__main__":
    for i in range(1, 5):
        print(f"--------这是第{i}页----------")
        main(i)
        time.sleep(2)
