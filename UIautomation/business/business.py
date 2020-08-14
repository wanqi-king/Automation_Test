from selenium import webdriver
from time import sleep


# 所使用浏览器
browser = webdriver.Chrome()
handles = browser.current_window_handle
print(handles)
browser.get('http://10.102.1.3/index')
browser.maximize_window()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/button').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/input').send_keys('TM17721869646')
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input').send_keys('Aa123456')
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/button').click()



def switch_new_ck():
    handles_new = browser.window_handles
    sleep(1)
    for i in browser.window_handles:
        if i != handles_new:
            browser.switch_to.window(i)
    # browser.switch_to.window(handles[1])

def switch_hold_ck():
    # handles = browser.current_window_handle
    browser.switch_to.window(handles)


if __name__ == '__main__':
    switch_new_ck()
    switch_hold_ck()