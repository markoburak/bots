from selenium import webdriver


def get_rozetka():

    # url for website
    url = 'https://rozetka.com.ua/ua/search/?text=nikkor&section_id=80060&redirected=1'
    # driver path
    chrome_path = r'./web_driver/83/chromedriver.exe'

    # start driver
    driver = webdriver.Chrome(chrome_path)

    # parser for rozetka
    driver.get(url)
    lens_35= driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-search/div/main/search-result/div[2]/section/app-search-goods/ul/li[25]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]').text
    lens_50= driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-search/div/main/search-result/div[2]/section/app-search-goods/ul/li[4]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]').text
    lens_85= driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-search/div/main/search-result/div[2]/section/app-search-goods/ul/li[16]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]').text
    driver.quit()
    return "35mm = "+lens_35+ "hrn\n"+"50mm = "+lens_50+ "hrn\n"+"85mm = "+lens_85+ "hrn\n"

