import json
import time
import traceback
from typing import Any

from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from lxml import etree
from selenium.webdriver.common.by import By


def parse_products_seller(
    url: str = 'https://www.ozon.ru/seller/proffi-1/products/',
    products_count: int = 10,
) -> list[dict[Any, Any]]:
    """

    Args:
        url: url на страницу продавца
        products_count: Кол-во товаров которое нужно получить, если 0 то все товары

    Returns:
        Список товаров
    """
    options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')

    # bypass Cloudflare
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")  # noqa: E501
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME, options=options)

    # bypass Cloudflare
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    _url = driver.command_executor._url + resource
    body = json.dumps({'cmd': "Page.addScriptToEvaluateOnNewDocument", 'params': {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
      '''
    }})
    driver.command_executor._request('POST', _url, body)

    # Товары продавца
    products: list[dict[Any, Any]] = []
    # Ссылки на страницы
    urls_pages: list[str] = []
    # Добавляем первую страницу, она же та что передал пользователь
    urls_pages.append(url)

    try:
        for number_page, url_page in enumerate(urls_pages, start=1):
            if number_page == 1:
                driver.get(url_page)
            else:
                driver.find_element(By.LINK_TEXT, str(number_page)).click()
            # time sleep в 10 секунд чтобы не словить бан
            time.sleep(10)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            page_etree = etree.HTML(str(soup))

            pages = page_etree.xpath('//*[@data-widget="megaPaginator"]/div[2]/div/div/div[1]/a')
            if len(pages) == 1:
                pages = page_etree.xpath('//*[@data-widget="megaPaginator"]/div[2]/div/div/div[2]/a')
            for page in pages:
                href = page.get('href')
                if href and 'page=' in href and f'https://www.ozon.ru{href}' not in urls_pages:
                    urls_pages.append(f'https://www.ozon.ru{href}')

            products_soup = soup.find('div', id='paginatorContent').div.div
            for product in products_soup:
                if isinstance(product, Tag) and product.text:
                    dom = etree.HTML(str(product))

                    product_dict = {}
                    product_dict['price'] = int(dom.xpath('/html/body/div/div[1]/div[1]/div/span[1]')[0].text[:-2].replace('\u2009', '').replace(' ', '').replace(' ', ''))
                    product_dict['name'] = dom.xpath('/html/body/div/div[1]/a/div/span')[0].text
                    product_dict['url'] = dom.xpath('/html/body/div/div[1]/a')[0].get('href').split('?')[0]
                    products.append(product_dict)
            if len(products) > products_count != 0:
                break
    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_exc()
    finally:
        # Закрываем сессию драйвера
        driver.close()
        driver.quit()
    if products_count == 0:
        return products
    return products[:products_count]
