import requests
from bs4 import BeautifulSoup
url = "http://198.15.119.148/thread-6502899-1-1.html"
headers = {"Cookie":"Ovo6_2132_nofavfid=1; Ovo6_2132_smile=1D1; Ovo6_2132_home_readfeed=1596302039; Ovo6_2132_saltkey=uWwVoOf7; Ovo6_2132_lastvisit=1597237109; Ovo6_2132_auth=e58dyOBCslNtdm%2FJ0fitRrebi%2Fm7IHyCgOeKHxKUDKy%2BB6t4uHfOgO2AbbN1uXJRYfVRDYYE5WpY1XHT03NyOIn9JD1k; Ovo6_2132_lastcheckfeed=3859335%7C1597240723; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_forum_lastvisit=D_2_1599402652D_454_1599404354; PHPSESSID=qqt06cc74d1p6ko8tvkdt2of20; Ovo6_2132_home_diymode=1; Ovo6_2132_ulastactivity=1599486113%7C0; Ovo6_2132_sendmail=1; Ovo6_2132_visitedfid=50D454D123D2D30D142D193D212D776D758; Ovo6_2132_viewid=tid_6502899; Ovo6_2132_lastact=1599486352%09home.php%09spacecp; Ovo6_2132_checkpm=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
s = requests.Session()
r = s.get(url,headers=headers)
print(r.text)