from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser =webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/Солнечная_система")

assert "Солнечная система" in browser.title
paragraphs = browser.find_elements(By.TAG_NAME, "p")
for paragraph in paragraphs:
    print(paragraph.text)
    input()

