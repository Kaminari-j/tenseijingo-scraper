import os
from modules import TenseijingoModule
import userinfo


def get_html_with_date(date_from: str, date_to: str):
    # Todo : Convert this method to module and make available query by date from to
    download_path = r'./html'
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # https://digital.asahi.com User Id and Password
    user_id = userinfo.id
    user_password = userinfo.password

    s = TenseijingoModule(user_id, user_password)
    try:
        s.open_session()

        # Get list of content
        article_list = s.get_backnumber_list()

        list_of_dates = [dt for dt in article_list.keys()]
        list_of_dates.sort()
        idx_from = list_of_dates.index(date_from)
        idx_to = list_of_dates.index(date_to) + 1

        # Todo:
        #   if there no from date or to date
        #       how to handle does dates which are inside range
        #       ex) dateFrom = '20191001', dateTo = '20191010'
        #           list_of_dates = ['20191005', '20191006', '20191007']

        for content_date in list_of_dates[idx_from:idx_to]:
            print(content_date, end=': ')
            html_name = download_path + '/' + content_date + '.html'
            if not os.path.exists(html_name):
                content_dic = article_list[content_date]
                content = s.convert_content_bs_to_dict(content_dic['url'])

                print('Downloading.. ' + html_name.split('/')[-1])
                html = TenseijingoModule.making_html(content)
                with open(html_name, 'w') as f:
                    f.write(html)
                    f.close()
            else:
                print('skip')
    except ConnectionError as e:
        print(e)


if __name__ == '__main__':
    from datetime import date
    get_html_with_date('20191001', date.today().strftime('%Y%m%d'))