import bs4
import requests 
from bs4 import BeautifulSoup



def priceparse():
    req = requests.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")

    soup = bs4.BeautifulSoup(req.text, "html") #need to figure out wha the site uses to store the value

    price =  soup.find('div id "nsecp"', {'class' :  ' inprice1 nsecp '}).find('rel')
   # return price
    print(price)

while True :
    print("Current value is " + str(priceparse()))