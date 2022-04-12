from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
import local_settings

# Sends an email alert once the product reaches the desired price
def alert_me(url,name, priceWanted):
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(local_settings.MAIL,local_settings.MAIL_PASSWORD)
    
    subject = 'Price fell down for '+name   
    body = 'Buy it now here: '+url   
    msg = f"Subject:{subject}\n\n{body}".encode('utf-8').strip()
    
    server.sendmail(local_settings.MAIL,local_settings.RECIPIENT,msg)
    print('Email alert sent')    
    server.quit()

# parses the html page
# compares the price with the desired price
def trackPrice(url,priceWanted):
    driver = webdriver.Chrome('/home/aouataf/Documents/chromedriver')
    
    driver.get(url)
    try:
        name = driver.find_element_by_id('title').text
        
        price = float(driver.find_element(By.XPATH, '//*[@class="a-price a-text-price a-size-medium apexPriceToPay"]').text[1:].replace(",",""))
        
        if price<=priceWanted:
            alert_me(url,name, priceWanted)
    except:
        print("no details found on this product")
    return 1

# Testing the code  
url="https://www.amazon.com/Acer-Predator-PH315-54-760S-i7-11800H-Keyboard/dp/B092YHJLS6/ref=sr_1_6?crid=F1JXNBNMFGGU&keywords=gamer+laptop&qid=1649613915&s=computers-intl-ship&sprefix=gamer+laptop+%2Ccomputers-intl-ship%2C176&sr=1-6"
print(trackPrice(url, 12999.0))

# to do :Run the program on AWS cloud
# cron(08**?*) every day at 8 am 


