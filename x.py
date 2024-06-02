
import random
from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
print("enter username")
username = "testytest2003"
 
print("enter password")
password = "testytest2003"
 
print("enter the url")
url = "https://x.com/i/flow/login"


def path():  
    global chrome
    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu') 




# ...
 
    # starts a new chrome session
    chrome = webdriver.Chrome() 
    chrome.implicitly_wait(6)


def url_name(url):  
    # the web page opens up
    chrome.get(url) 
    
    # webdriver will wait for 4 sec before throwing a  
    # NoSuchElement exception so that the element 
    # is detected and not skipped.
    time.sleep(10) 

def login(username, your_password):
	

	# finds the username box


    usern = chrome.find_element(By.NAME,"text")
    usern.send_keys(username)  
    
    time.sleep(10)
    btn = chrome.find_element(By.XPATH, "//span[text()='Next']")
    chrome.execute_script("arguments[0].click();", btn)
    time.sleep(5)

	# sends the entered username


	# finds the password box
    passw = chrome.find_element(By.NAME, "password") 

	# sends the entered password
    passw.send_keys(your_password)	 
    passw.send_keys(Keys.RETURN)
    time.sleep(15)
    
    div_element = chrome.find_element(By.XPATH, f"//div[@aria-label='Timeline: Trending now']")
    span_elements = div_element.find_elements(By.TAG_NAME, "span")
    texts = []
    for element in span_elements:
        texts.append(element.text)

    return analysis(texts)




def analysis(text):
    i=0
    data=[]

    while i < len(text):
        if 'Trending' in text[i]:
            row =[]
            row.append(text[i])
            i+=1
            row.append(text[i])
            i+=1
            while 'posts' not in text[i] and i < len(text) :
                i+=1
            if 'posts' in text[i]:
                row.append(text[i])
                data.append(row)

        i+=1

    return data


def main():
    path()
    time.sleep(1)

    url_name(url)

    data = login(username, password)

    return data

#like_pic()

#continue_liking()
#chrome.close()
