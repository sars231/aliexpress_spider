#! /usr/bin/env python
# coding:utf-8

url = 'https://www.aliexpress.com/item/19pcs-Cool-Fashion-NBA-Cartoon-Basketball-Star-Waterproof-Stickers-Classic-Toys-PVC-Fashion-Laptop-Skateboard-Suitcase/32832905231.html?spm=2114.search0104.3.1.36055b0diX7ce9&ws_ab_test=searchweb0_0,searchweb201602_4_10152_10151_10065_10344_10068_5722815_10342_10325_10343_10546_10340_5722915_10548_10341_5722615_10696_10084_10083_10618_10307_5722715_10059_10534_100031_10103_441_10624_10623_10622_5722515_10621_10620,searchweb201603_50,ppcSwitch_5&algo_expid=76b150a6-c549-4d8e-b763-0717980155e3-0&algo_pvid=76b150a6-c549-4d8e-b763-0717980155e3&priceBeautifyAB=0'

from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)
time.sleep(5)
driver.find_element_by_class_name('close-layer').click()
target = driver.find_element_by_id('j-transaction-feedback')
#js="var q=document.documentElement.scrollTop=100000"
js = 'arguments[0].scrollIntoView();'
driver.execute_script(js,target)
time.sleep(5)
data = driver.page_source



soup = BeautifulSoup(data,'html.parser')
needs = soup.find(id='j-transaction-feedback').tbody.find_all('tr')

#print(need)

def deal_data(needs):
    while True:
        driver.find_element_by_class_name('ui-pagination-next').click()
        time.sleep(5)
        data = driver.page_source
        soup = BeautifulSoup(data,'html.parser')
        need = soup.find(id='j-transaction-feedback').tbody.find_all('tr')
        needs.extend(need)
        if soup.find(class_='ui-pagination-next ui-pagination-disabled'):
            break
    return needs

needs = deal_data(needs)

with open('r.csv','w+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    print('ok')
    for n in needs:
        row = n.text.strip().split('\n')
        print(row)
        writer.writerow(row)
