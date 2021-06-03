from selenium import webdriver

chromeDriverPath = "C:\Program Files (x86)\chromedriver.exe"

browser=webdriver.Chrome(chromeDriverPath)
browser.get("https://www.google.com")
#browser.maximize_window()
loginIDElem= browser.find_element_by_name("q")
loginIDElem.send_keys("Anime")
loginIDElem.submit()

# mystring = "open chrome and search anime"
# mylist = list(mystring.split())
# print(str(mylist[1]))