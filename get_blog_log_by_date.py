import const
import requests
import re
from bs4 import BeautifulSoup


def get_blog_log_by_date(date) -> str:
    '''日付から成田さんのブログスクレイピングする
    Args:
        date (int): 日付.formatはYYYYMMDD
    Returns:
        str
    '''
    print('date: %d' % int(date))
    URL = const.URL.format(date)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    table1 = soup.find_all('table')[1]
    try:
        [a.extract() for a in table1.find_all('a')]
        [center.extract() for center in table1.find_all('center')]
        table1.find('script').extract()
    except:
        pass
    description = table1.text

    return description


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date',  default=20110418, type=int)
    args = parser.parse_args()
    date = int(args.date)
    description = get_blog_log_by_date(date)
    print(description)
