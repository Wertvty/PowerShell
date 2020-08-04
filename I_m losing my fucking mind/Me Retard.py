import urllib.request
import requests
import os
from bs4 import BeautifulSoup
file_name = 1
url = requests.get('https://www.cutesypooh.com/when-cats-put-their-best-derp-face-forward/')
html = BeautifulSoup(url.text)
images = html.findAll('img')
for k in images:
    full_name = os.path.join('C:/Users/vahva/Exercism/I_m losing my fucking mind/Всратые Коты', str(file_name)+'.png')
    urllib.request.urlretrieve(k['src'], full_name)
    if file_name == 26:
        break
    file_name+=1
os.system('cls')
print ('''                      Я - долбоёб и читал документацию модулей 5 часов, 
                            чтоб заставить это говно работать,
                    хотя легче и быстрее было бы сохранить все вручную
                                            ;^)''')




