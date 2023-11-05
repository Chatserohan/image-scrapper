import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os 


save_dir='images/'

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

query=input('enter object name to scrap')
response=requests.get(f'https://www.google.com/search?q={query}&sca_esv=579625040&tbm=isch&source=hp&biw=1024&bih=588&ei=bKxHZcapO6bn2roPzvutyAc&iflsig=AO6bgOgAAAAAZUe6fQtT2TjyoqHotHqea5OPpeo7kChZ&ved=0ahUKEwjGj4e2jq2CAxWms1YBHc59C3kQ4dUDCAY&uact=5&oq=elon+musk&gs_lp=EgNpbWciCWVsb24gbXVzazIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQNI5B9QkgtYtRtwAHgAkAEAmAHKAaABgg2qAQUwLjguMbgBA8gBAPgBAYoCC2d3cy13aXotaW1nqAIAwgIFEAAYgATCAggQABixAxiDAcICCxAAGIAEGLEDGIMBwgIEEAAYAw&sclient=img')

soup=BeautifulSoup(response.content,'html.parser')

image_tags=soup.find_all('img')

del image_tags[0]

for i in image_tags:
    image_url=i['src']
    image_data=requests.get(image_url).content
    with open(os.path.join(save_dir,f'{query}_{image_tags.index(i)}.jpg'),'wb') as f:
        f.write(image_data)
    


