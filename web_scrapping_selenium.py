#web Scrapping using Selenium

#pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


#set up the web driver with web driver manager
service  = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.bbc.com/news")

time.sleep(3) 


#find all the headlines on the page
headlines = driver.find_elements(By.TAG_NAME,'h2')

#print out the headlines
for index, headline in enumerate(headlines):
    print(f"{index + 1}: {headline.text}")

try:
    headlines = driver.find_elements(By.TAG_NAME, 'h2')

#save the headlines 
    with open("/Users/aizaz/Desktop/Desktop/headlines.txt", 'w', encoding='utf-8') as file:
        for headline in headlines:
            file.write(headline.text + "\n")
except Exception as e:
    print(f"An error occured: {e}")
finally:
    driver.quit()


