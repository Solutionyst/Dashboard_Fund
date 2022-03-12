# Imports
import openpyxl
import pandas as pd
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import regex as re
import os
from datetime import date
from .models import position

def test():
    position_data = position.objects.all()

    start_url = 'https://www.londonstockexchange.com/stock/'
    end_url = '/analysis'

    options = Options()
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), options=options)

    for z in position_data:
        ticker = z.ticker
        url = (start_url + ticker + end_url)

        driver.get(url)
        time.sleep(1)

        # Close Cookies Banner, if applicable
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/button[1]').click()
        except:
            pass

        # Move to Analysis Screen
        driver.find_element_by_xpath(
            '/html/body/app-root/app-handshake/div/app-page-content/app-tab-nav/div/div/div/div/ul/li[6]').click()
        time.sleep(2)

        # Increase list to 100
        driver.find_element_by_xpath('//*[@id="dropdownSize"]').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/app-root/app-handshake/div/app-page-content/app-tab-nav/app-news-table-results/section/div[2]/div[1]/form/div/ng-select/ng-dropdown-panel/div/div[2]/div[4]').click()
        time.sleep(1)
        news = driver.find_elements_by_xpath('//*[@id="news-table-results"]/table/tbody/tr')

        # Find instance of 'Total Voting Rights' in page
        for i in news:
            if 'total voting rights' in i.text.lower():
                link = driver.find_element_by_xpath(
                    '//*[@id="news-table-results"]/table/tbody/tr[{}]/td[1]/app-link-or-dash/a'.format(
                        news.index(i) + 1)).get_attribute('href')
                break

        # Click link to Total Voting Rights
        driver.get(link)
        time.sleep(2)

        # Analyse Text

        title = driver.find_elements_by_xpath('//*[@id="news-article-content"]/div[1]/div[6]')

        rawtext = title[0].text
        rawtext = rawtext[0:rawtext.find('This information is provided by RNS')]
        alltext = rawtext.split('. ')

        processed = []
        for i in alltext:
            if i == '':
                continue
            else:
                j = i.replace('\n', '')
                if 'shares' in j.lower():
                    if 'ordinary shares' in j.lower() or 'treasury' in j.lower():
                        processed.append(j)

        numbers = []

        for sentence in processed:
            splitli = sentence.split(' ')
            for i in splitli:
                numbers.append(re.sub('[^0-9,]', "", i))
        final_numbers_li = []

        for i in numbers:
            if len(i) > 6 and ',' in i:
                final_numbers_li.append(int(i.replace(',', '')))

        ordinary_shares = max(final_numbers_li)
        if len(final_numbers_li) > 1:
            if min(final_numbers_li) != max(final_numbers_li):
                treasury_shares = min(final_numbers_li)
            else:
                treasury_shares = 0
        else:
            treasury_shares = 0
        total_voting_rights = ordinary_shares - treasury_shares


        print(treasury_shares)
        print(total_voting_rights)
        print(ordinary_shares)

        o = position.objects.get(ticker=z.ticker)
        o.treasury_shares = treasury_shares
        o.shares_issued = ordinary_shares
        o.shares_outstanding = total_voting_rights
        o.save()
