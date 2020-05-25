from bs4 import BeautifulSoup
from pprint import pprint
import requests
from urllib.request import urlopen, Request
import urllib
import bs4
html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class': 'weather_box'})

find_address = data1.find('span', {'class':'btn_select'}).text
print('현재 위치: '+find_address)

find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
print('현재 온도: '+find_currenttemp+'℃')

data2 = data1.findAll('dd')
find_dust = data2[0].find('span', {'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span', {'class':'num'}).text
print('현재 미세먼지: '+find_dust)
print('현재 초미세먼지: '+find_ultra_dust)
print('현재 오존지수: '+find_ozone)
location = input("원하시는 지역을 찾아보고싶으면 검색하세요 : ")
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html5lib')
print('현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')