import requests 
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
import os
import datetime
# make request and parse data
def get_req():
    req = requests.get("https://www.coingecko.com")
    soup = bs(req.text,"lxml")
# scrape the html to get what you want

    a = [i.text.strip() for i in soup.find_all(class_="tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between")]
    
    c = [x.text.strip() for x in soup.find_all(class_="td-price price text-right pl-0")]
    
    result = [(i,x) for i,x in zip(a,c) ]
    
    return result
# insert data to csv file
result2 = get_req()
row = ["name","balance"]
csv_name = input("enter the csv file name with .csv")
with open(csv_name,"w") as f:
    writter = csv.writer(f)
    writter.writerow(row)
    writter.writerows(result2)
print("file was created")

# Get the price of each coin

def get_price():
    dataset = pd.read_csv(csv_name)
    check = False
    while check == False :
        coin = input("enter a coin name: ")
        print(f"at {datetime.datetime.now()} {coin} is : \n{dataset['balance'][dataset['name'] == coin]}")
        ask = input("another q ! yes or no")
        if ask == "yes":
            continue
        elif ask == "no":
            check = True
        else:
            print("yes or no")
            check = True
    
            
get_price()
