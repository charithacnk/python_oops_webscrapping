import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.nike.com/w/jordan-1-shoes-4fokyzy7ok")
print(response)

soup=BeautifulSoup(response.content,'html.parser')

#print(soup)

names=soup.find_all('div', class_='product-card__info disable-animations for--product') 
#print(names)
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)



prices=soup.find_all('div', class_='product-card__animation_wrapper') 
#print(names)
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
print(price)

images=soup.find_all('img', class_='product-card__link-overlay') 
#print(names)
image=[]
for i in images[0:10]:
    d=i['src']#i.div.img['src']
    image.append(d)
print(image)

#product-card__link-overlay

links=soup.find_all('a', class_='product-card__link-overlay') 
#print(names)
link=[]
for i in links[0:10]:
    d="https://www.nike.com"+i['href'] # href=link
    link.append(d)
print(link)


data={"Names":name,#name.pandas.series
      "Prices":price,
      "links":link,
    #   "images":image
    }

print(data)

df= pandas.DataFrame(data)

df.to_csv("Nike_data.csv")

