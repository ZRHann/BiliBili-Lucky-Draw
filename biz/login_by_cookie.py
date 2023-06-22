import configparser
import json
from time import sleep
from utils.selenium_util import init_webdriver


def login_by_cookie(bro, cookie_path):
    """
    根据保存的Cookie信息进行登录
    :param bro:
    :param cookie_path:
    :return:
    """
    try:
        with open(cookie_path, 'r', encoding='utf-8') as f:
            cookies = f.readlines()
        for cookie in cookies:
            cookie = cookie.replace(r'\n', '')
            cookie_li = json.loads(cookie)
            sleep(1)
            for cookie in cookie_li:
                bro.add_cookie(cookie)
            bro.refresh()
        print('使用cookie自动登录成功！')
        sleep(1)
    except Exception as e:
        print(e)
        print('登录失败')


if __name__ == '__main__':
    # 读取配置信息
    config = configparser.ConfigParser()
    config.read('config.ini')
    userId = config.get('user-info', 'userId')
    homeUrl = config.get('base-info', 'homeUrl')
    # 初始化
    bro, chains = init_webdriver()
    bro.get(homeUrl)
    # 登录
    cookie_path = './cookie/' + userId + '.txt'
    login_by_cookie(bro, cookie_path)
    input()
    bro.quit()