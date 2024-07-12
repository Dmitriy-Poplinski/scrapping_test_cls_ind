# from bs4 import BeautifulSoup
# import requests
import re


pattern = re.compile(r'listingcontainer\[\d+]')

#
# print("pattern", pattern)
#
# rockauto_html = requests.get("https://www.rockauto.com/en/catalog/").text
# rockauto_soup = BeautifulSoup(rockauto_html, "html.parser")
# brands = rockauto_soup.find_all("a", class_="navlabellink nvoffset nnormal")
#
# print(rockauto_soup)
#
# models = rockauto_soup.find_all("tbody", class_="listing-inner altrow-a-1")
#
# print("models", models)
#
# for model in models:
#     print("value", model)

# print(brands)

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.rockauto.com/en/catalog/")

try:
    tbodies = driver.find_elements(By.CSS_SELECTOR, "[id^='listingcontainer']")
    for tbody in tbodies:
        print(tbody.get_attribute("outerHTML"))
except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()
