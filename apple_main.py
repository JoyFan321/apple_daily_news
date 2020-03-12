import requests, bs4
import re
import lxml

# get html
url = 'https://tw.appledaily.com/hot/daily'
apple_html = requests.get(url)
soup_obj = bs4.BeautifulSoup(apple_html.text, 'lxml')

# sort top 10
items = soup_obj.find('ul', 'all').find_all('li')
for item in items:
	if item.find('div', 'aht_title_num atopred'):
		num = item.find('div', 'aht_title_num atopred').text
	else:
		num = item.find('div', 'aht_title_num').text
	title = item.find('div', 'aht_title').text
	link = item.find('a').get('href') 

	print(f'新聞編號：{num}')
	print(f'新聞標題：{title}')
	print(f'新聞鏈結：{link}')
	
		