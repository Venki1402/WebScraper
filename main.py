import requests
import tldextract
from bs4 import BeautifulSoup
import cv2
from prettytable import PrettyTable




# Amazon
def amazon(soup,url):

    # Getting the name of the product
    product_name = soup.find("span", {"id": "productTitle"})

    # Getting the price of the product
    rupee_symbol = soup.find("span", {"class": "a-price-symbol"})
    product_price = soup.find("span", {"class": "a-price-whole"})

    # Adding the details in the table
    table.add_row([tldextract.extract(url).domain.strip(), product_name.text.strip(), rupee_symbol.text+''+product_price.text])


# Snapdeal
def snapdeal(soup,url):

    # Getting the name of the product
    product_name = soup.find("h1", {"class": "pdp-e-i-head"})

    # Getting the price of the product
    rupee_symbol = soup.find("span", {"class": "pdp-final-price"})
    product_price = soup.find("span", {"class": "payBlkBig"})

    # Adding the details in the table
    table.add_row([tldextract.extract(url).domain.strip(), product_name.text.strip(), rupee_symbol.text])


# Flipkart
def flipkart(soup,url):

    # Getting the name of the product
    product_name = soup.find('span', class_='B_NuCI')

    # Getting the price of the product
    product_price = soup.find('div', class_='_30jeq3 _16Jk6d')

    # Adding the details in the table
    table.add_row([tldextract.extract(url).domain.strip(), product_name.text.strip(), product_price.text.strip()])


# Myntra
def myntra(soup,url):
    product_brand = soup.find("h1",{"class" : "pdp-title"})
    product_name = soup.find("h1",{"class" : "pdp-name"})
    # rupee_symbol = soup.find("span", {"class": "a-price-symbol"})
    product_price = soup.find("span", {"class": "pdp-price"})
    # print(product_name.get_text().strip())
    # print(rupee_symbol.text + " " + product_price.text)
    # print("Available at Amazon.in")
    table.add_row([tldextract.extract(url).domain.strip(), product_name.text.strip(), product_price.text.strip()])



def gostor(soup,url):
    product_name = soup.find("h1")

    # Here there is span inside another span so see what should be done

    product_price = soup.find("span",class_='text-22 font-semibold')

    table.add_row([tldextract.extract(url).domain.strip(), product_name.text.strip(), product_price.text.strip()])


# Take Input

url1 = input("Enter URL: ")
url2 = input("Enter URL: ")

print('Calculating results...')

# Extract information from URL
extracted_info1 = tldextract.extract(url1)
extracted_info2 = tldextract.extract(url2)

# Headers

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# Session

session = requests.Session()

req1 = session.get(url1, headers=headers)
req2 = session.get(url2, headers=headers)


soup1 = BeautifulSoup(req1.content, "html.parser")
soup2 = BeautifulSoup(req2.content, "html.parser")

captcha = soup1.find("form", {"name": "captchaForm"})
if captcha is None:
    print("Lucky! No Captcha")

    table = PrettyTable()
    table.field_names = ['Domain Name', 'Product Name', 'Product Price']

    if extracted_info1.domain.strip()=='amazon':
        amazon(soup1,url1)
    elif extracted_info1.domain.strip()=='snapdeal':
        snapdeal(soup1,url1)
    elif extracted_info1.domain.strip()=='flipkart':
        flipkart(soup1,url1)
    # elif extracted_info1.domain.strip()=='myntra':
    #     myntra(soup1,url1)
    # elif extracted_info1.domain.strip()=='gostor':
    #     gostor(soup1,url1)
    else:
        print("oh oh! First Site is not supported yet. Our Apologies.")


    if extracted_info2.domain.strip()=='amazon':
        amazon(soup2,url2)
    elif extracted_info2.domain.strip()=='snapdeal':
        snapdeal(soup2,url2)
    elif extracted_info2.domain.strip()=='flipkart':
        flipkart(soup2,url2)
    # elif extracted_info2.domain.strip()=='myntra':
    #     myntra(soup2,url2)
    # elif extracted_info2.domain.strip()=='gostor':
    #     gostor(soup2,url2)
    else:
        print("oh oh! Second Site is not supported yet. Our Apologies.")


    # Print the Output
    print(table)



else:
   print(".......... YOU'VE HIT A CAPTCHA")
   capatchaImage = soup1.find("img",{"id":"captchaTag"}).get("src")
   cv2.imshow("captcha", captchaImage)
   cv2.waitKey()
   captchaInput = input("Please enter captcha: ")





