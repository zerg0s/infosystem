import re
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://24smi.org/celebrity/3555-petr-i.html")
res = driver.find_elements(
    By.XPATH,
    "//p")
years = list()
for abc in res:
    l = abc.text
    years += re.findall(r'[1-9][0-9]{,3} год(?:|а|у|ом|е|ы|ов|ам|ами|ах)\b', l)
print(years)
driver.close()
