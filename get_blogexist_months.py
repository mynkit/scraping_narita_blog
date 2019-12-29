import const
import requests
from bs4 import BeautifulSoup
import re


def get_blogexist_months() -> list:
    '''ブログの存在する月(YYYYMM)を全取得
    Returns:
        [int]
    '''
    URL = const.URL.format('1&ym=1')
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    months = [int(re.findall('ym=(\d{6})', a.get('href'))[0]) for a in soup.find_all(
        'a') if a.get('href') if re.search('ym=\d{6}', a.get('href'))]
    return sorted(months)


if __name__ == '__main__':
    months = get_blogexist_months()
    print(months)
