from time import sleep
import pillow_services
import selenium.webdriver
import requests
import multiprocessing
import fake_useragent
from selenium.webdriver.firefox.options import Options
import os


def get_html(url):
    response = requests.get(url)
    return response.text


def get_fake_useragent():
    user_agent = os.getenv("FAKE_USER_AGENT")
    ip = os.getenv("FAKE_IP")
    port = 55993
    opt = selenium.webdriver.FirefoxProfile()
    opt.set_preference(f'general.useragent.override', user_agent)
    return opt


def get_options():
    options = Options()
    options.headless = True
    return options


def get_login_session():
    login = os.getenv("TELEPHONE")
    password = os.getenv("PASSWORD")
    driver = selenium.webdriver.Firefox(get_fake_useragent(), options=get_options())
    driver.set_page_load_timeout(1000)
    driver.get('https://www.avito.ru/login?authsrc=h')
    sleep(3)
    login_place = driver.find_element_by_name('login')
    login_place.send_keys(login)
    password_place = driver.find_element_by_name('password')
    password_place.send_keys(password)
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
    sleep(3)
    return driver


def download_phone_image(url, driver=None):
    try:
        driver = driver if driver is not None else selenium.webdriver.Firefox(get_fake_useragent(), options=get_options())
        driver.get(url)
        sleep(2)
        try:
            button = driver.find_element_by_css_selector('.styles-item-phone-button_height-3SOiy')
        except:
            button = driver.find_element_by_css_selector('a.item-phone-button:nth-child(1)')
        button.click()
        sleep(2)

        try:
            phone_image = driver.find_element_by_css_selector('.item-phone-big-number > img:nth-child(1)')
            location = phone_image.location
            size = phone_image.size
            driver.save_screenshot('avito_parser.png')
            pillow_services.crop_image('avito_parser.png', location, size)
        except:
            pass
    except Exception:
        pass
    driver.quit()


def get_json_with_links(offset):
    response = requests.get('https://www.avito.ru/web/1/main/items?locationId=635160&lastStamp=1623065770&limit=30',
                            params={'offset': str(offset)},
                            headers={'Referer': 'https://www.avito.ru'})
    return response.json()['items']


def get_links_on_json(json):
    with multiprocessing.Pool(10) as p:
        map = p.map(get_url_on_item, json)
        return map


def get_url_on_item(item):
    if 'urlPath' in item.keys():
        return 'https://www.avito.ru' + item['urlPath']


