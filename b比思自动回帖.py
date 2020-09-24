import requests
import time
from requests.exceptions import RequestException
# from lxml import etree
import random
url = "http://198.15.119.148/thread-6502899-1-1.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'cookie': 'Ovo6_2132_nofavfid=1; Ovo6_2132_smile=1D1; Ovo6_2132_home_readfeed=1596302039; Ovo6_2132_saltkey=uWwVoOf7; Ovo6_2132_lastvisit=1597237109; PHPSESSID=03l3ou025j6vk75uchcfm59755; Ovo6_2132_auth=e58dyOBCslNtdm%2FJ0fitRrebi%2Fm7IHyCgOeKHxKUDKy%2BB6t4uHfOgO2AbbN1uXJRYfVRDYYE5WpY1XHT03NyOIn9JD1k; Ovo6_2132_lastcheckfeed=3859335%7C1597240723; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_forum_lastvisit=D_918_1595694935D_837_1596301999D_50_1596308652D_397_1596983506D_454_1596984449D_776_1596985173D_2_1597240986; Ovo6_2132_home_diymode=1; Ovo6_2132_ulastactivity=1597241449%7C0; Ovo6_2132_sendmail=1; Ovo6_2132_visitedfid=50D2D776D454D30D212D758D123D110D142; Ovo6_2132_viewid=tid_6502899; Ovo6_2132_lastact=1597241485%09home.php%09spacecp; Ovo6_2132_check'}
ss = requests.Session()
r = requests.get(url)
print(r.status_code)
print(r.text)



