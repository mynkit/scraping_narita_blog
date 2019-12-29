from get_blog_log_by_date import get_blog_log_by_date
from get_dates_by_month import get_dates_by_month
from get_blogexist_months import get_blogexist_months
import pandas as pd


def main():
    all_discription = []
    months = get_blogexist_months()
    for month in months:
        dates = get_dates_by_month(month)
        for date in dates:
            discription = get_blog_log_by_date(date)
            df = pd.DataFrame({'month': [month], 'date': [date], 'discription': [discription]})
            all_discription.append(df)
    all_discription = pd.concat(all_discription)
    return all_discription

if __name__ == '__main__':
    all_discription = main()
    all_discription.to_csv('all_discription.csv', index=False, encoding='utf-8-sig')
