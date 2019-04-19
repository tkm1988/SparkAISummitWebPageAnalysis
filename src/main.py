import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml

CHROME_DRIVER_PATH = "/Users/tkm/GitHub/SparkAISummitWebPageAnalysis/modules/ChromeDriver_73.0.3683.68/chromedriver"

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH,  options=options)

target_URL = 'https://databricks.com/sparkaisummit/north-america/schedule'

try :
    driver.get(target_URL)
    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    for h4 in soup.find_all('h4'):
        print(h4.string)
except:
    traceback.print_exc()
finally:
    driver.quit()
