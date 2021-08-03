import sys
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://github.com/login')

def create():
    print(str(sys.argv[1]))
    py_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    py_button.send_keys('YOUR_GITHUB_USERNAME')
    pass_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    pass_button.send_keys('YOUR_GITHUB_PASSWORD')
    sign_button = browser.find_elements_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")[0]
    sign_button.click()
    browser.get('https://github.com/new')
    repo_txt = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    repo_txt.send_keys(str(sys.argv[1]))
    time.sleep(2)
    create_button = browser.find_elements_by_xpath("//*[@id='new_repository']/div[4]/button")[0]
    create_button.click()
    link = 'https://github.com/Rishabh3112002/'+str(sys.argv[1])
    browser.get(link)
    browser.quit()

if __name__ == "__main__":
    create()
