import smtplib 
import requests #pip istall requests
from bs4 import BeautifulSoup #pip istall bs4

#This programe is create by Sujit Mandal

URL = ('https://www.amazon.in/Canon-EOS-1300D-Digital-18-55mm/dp/B01D4EYNUG/ref=pd_sbs_23_2/257-8946760-0981711?_encoding=UTF8&pd_rd_i=B01D4EYNUG&pd_rd_r=40b6b35d-a0e9-11e9-8027-cd598beea6df&pd_rd_w=AMDvp&pd_rd_wg=39fvn&pf_rd_p=87667aae-831c-4952-ab47-0ae2a4d747da&pf_rd_r=ZA235CP7YC1DHSWVRDGP&psc=1&refRID=ZA235CP7YC1DHSWVRDGP')
#search on google "my user agent"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price_1 = (price[2:4])
    converted_price_2 = (price[5:8])
    converted_price = converted_price_1 + converted_price_2

    print(title.strip())

    print(float(converted_price))
    #print(price)

    if(converted_price >= "15000"):
        send_email()
    else:
        print("HEY THE PRICE HAS NOT FELL DOWN!")
   
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("abcd@gmail.com", "password") #g-mail longing 

    subject = ("Price is fell down!")
    body = ("Check the amazonw link https://www.amazon.in/Canon-EOS-1300D-Digital-18-55mm/dp/B01D4EYNUG/ref=pd_sbs_23_2/257-8946760-0981711?_encoding=UTF8&pd_rd_i=B01D4EYNUG&pd_rd_r=40b6b35d-a0e9-11e9-8027-cd598beea6df&pd_rd_w=AMDvp&pd_rd_wg=39fvn&pf_rd_p=87667aae-831c-4952-ab47-0ae2a4d747da&pf_rd_r=ZA235CP7YC1DHSWVRDGP&psc=1&refRID=ZA235CP7YC1DHSWVRDGP")

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        "abcd@gmail.com@gmail.com", #sender e-mail
        "abcd@gmail.com@gmail.com", #reciver e-mail
        msg
    )
    print("HEY E-mail HAS BEEN SENT!")
    server.quit()

check_price()
