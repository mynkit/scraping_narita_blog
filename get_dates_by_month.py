import const
import re
import requests
from bs4 import BeautifulSoup


def get_dates_by_month(month) -> list:
    '''ある月(YYYYMM)にブログに投稿された日付を取得する
    Args:
        month (int): ブログの存在する日付を取得したい月.formatはYYYYMM.
    Returns:
        [int]
    '''
    URL = const.URL.format(month)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    dates = [int(re.findall('ymd=(\d{8})', a.get('href'))[0]) for a in soup.find_all('a') if a.get('href') and re.search('ymd=\d{8}', a.get('href'))]
    return sorted(dates)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--month', default=201104, type=int)
    args = parser.parse_args()
    month = int(args.month)
    dates = get_dates_by_month(month)
    print(dates)
