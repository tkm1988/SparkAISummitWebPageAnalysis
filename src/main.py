#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
import pandas as pd

CHROME_DRIVER_PATH = "/Users/tkm/GitHub/SparkAISummitWebPageAnalysis/modules/ChromeDriver_73.0.3683.68/chromedriver"

def get_summit_schedule_titles(target_URL) :
    schedule_title_list = []

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH,  options=options)

    try :
        driver.get(target_URL)
        time.sleep(5)
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        for h4 in soup.find_all('h4'):
            schedule_title_list.append(h4.string)
    except:
        traceback.print_exc()
    finally:
        driver.quit()
        return schedule_title_list

def main() :
    target_URL = 'https://databricks.com/sparkaisummit/north-america/schedule'

    title_list = get_summit_schedule_titles(target_URL)
    title_dataframe = pd.DataFrame(title_list, columns = ['title'])

    title_dataframe.to_csv('../contents/2019titlelist.csv')
    
if __name__ == '__main__' :
    main()


