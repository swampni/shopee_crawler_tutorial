import requests  # 引入requests函式庫
import json  # 引入json函式庫
from selenium import webdriver  # 從selenium引入webdriver這個class


# 因為複製下來的內容是json格式，需要先轉成dict(字典)才能用requests送出去
paylaod = json.loads('{"item_shop_ids":[{"itemid":10440560,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10442845,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10436586,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10437820,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":19090283,"adsid":0,"shopid":4520975,"campaignid":0},{"itemid":10468654,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":1249190,"adsid":0,"shopid":176116,"campaignid":0},{"itemid":10438059,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10468560,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10442463,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10442585,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10440384,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":28564665,"adsid":0,"shopid":5528567,"campaignid":0},{"itemid":10438294,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":6602131,"adsid":0,"shopid":1757297,"campaignid":0},{"itemid":10456562,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10437636,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":4770520,"adsid":0,"shopid":2208647,"campaignid":0},{"itemid":10442286,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":7647297,"adsid":0,"shopid":2781071,"campaignid":0},{"itemid":1249021,"adsid":0,"shopid":176116,"campaignid":0},{"itemid":18874011,"adsid":0,"shopid":1975307,"campaignid":0},{"itemid":16967679,"adsid":0,"shopid":746024,"campaignid":0},{"itemid":4103747,"adsid":0,"shopid":810776,"campaignid":0},{"itemid":17198338,"adsid":0,"shopid":4914505,"campaignid":0},{"itemid":8806725,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":5804309,"adsid":0,"shopid":2521617,"campaignid":0},{"itemid":5790921,"adsid":0,"shopid":176116,"campaignid":0},{"itemid":18414307,"adsid":0,"shopid":4824242,"campaignid":0},{"itemid":10508589,"adsid":0,"shopid":2478934,"campaignid":0},{"itemid":8808156,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":9502811,"adsid":0,"shopid":276448,"campaignid":0},{"itemid":8806125,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":8901279,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":30229022,"adsid":0,"shopid":185310,"campaignid":0},{"itemid":20780804,"adsid":0,"shopid":5117703,"campaignid":0},{"itemid":8806381,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":18259683,"adsid":0,"shopid":1154659,"campaignid":0},{"itemid":13343084,"adsid":0,"shopid":3618853,"campaignid":0},{"itemid":6755666,"adsid":0,"shopid":2685888,"campaignid":0},{"itemid":16225470,"adsid":0,"shopid":4520975,"campaignid":0},{"itemid":23646420,"adsid":0,"shopid":3070693,"campaignid":0},{"itemid":24014109,"adsid":0,"shopid":4526230,"campaignid":0},{"itemid":13581824,"adsid":0,"shopid":3070693,"campaignid":0},{"itemid":22561844,"adsid":0,"shopid":759803,"campaignid":0},{"itemid":16432285,"adsid":0,"shopid":1293928,"campaignid":0},{"itemid":8803569,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":22765509,"adsid":0,"shopid":746024,"campaignid":0},{"itemid":8807062,"adsid":0,"shopid":3343348,"campaignid":0},{"itemid":26010591,"adsid":0,"shopid":1468591,"campaignid":0}]}')

driver = webdriver.Chrome(
    'D:\code\ceiba\driver\chromedriver.exe')  # initiate chrome
driver.get(
    'https://shopee.tw/%E9%9B%BB%E8%85%A6%E5%91%A8%E9%82%8A%E8%80%97%E6%9D%90-cat.69')  # 瀏覽我們要的網頁
cookie = ';'.join(['{}={}'.format(item['name'], item['value'])  # 抓cookie
                   for item in driver.get_cookies()])
# token = [item['value']  #抓csrf token  影片裡的方法
#              for item in driver.get_cookies() if item['name'] == 'csrftoken'][0]
token = driver.get_cookie('csrftoken')['value']  #抓csrf token 我個人覺得更好的方法
driver.quit()
# 把headers用字典形式表示，簡單明瞭



content = {  # 設定get參數
    'by': 'pop',
    'order': 'desc',
    'categoryids': 69,
    'newest': 0,
    'limit': 50,
    'skip_price_adjust': False,
}
# https://shopee.tw/api/v1/search_items/?by=pop&order=desc&categoryids=69&newest=0&limit=50&skip_price_adjust=false
get_item = requests.get(
    'https://shopee.tw/api/v1/search_items/', params=content)
payload = str({"item_shop_ids": get_item.json()['items']})
payload = json.loads(payload.replace("'", '"'))  # json要求用""不能用''






headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'x-csrftoken': token,
    'Referer': 'https://shopee.tw/3C%E7%9B%B8%E9%97%9C-cat.69',
    'Cookie': cookie,
}


# 用requests做post requests，附帶的就是我們剛剛複製下來的東西還有我們剛剛的headers
response = requests.post(
    'https://shopee.tw/api/v1/items/', json=paylaod, headers=headers)

# 印出字典形式
for r in response.json():
    print('******************************************************')
    print(r['name'])
