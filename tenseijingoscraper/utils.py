import os
from datetime import timedelta, datetime as dt


def create_file(file_full_name: str, html: str):
    try:
        with open(file_full_name, 'w') as f:
            f.write(html)
            f.close()
        return True
    except IOError:
        raise IOError('[Error] : Failed to create html file.')


def naming_file(path: str, filenm: str) -> str:
    """
    create file name with `path` and `filenm` argument
    :rtype: str
    :param path: directory path of file
    :param filenm: name of file
    :return: [directory path]/[filenm].html
    """
    return f'{path}/{filenm}.html'


def prepare_directory(directory_path: str) -> bool:
    """
    check exist of directory
    :param directory_path:
    :return: bool
        Does directory has been created or exists
    """
    if os.path.exists(directory_path):
        return True
    else:
        try:
            os.makedirs(directory_path)
            return True
        except:
            print(f'Error : Failed To Create Directory "{directory_path}"\nPlease Check Directories')
            return False


class DateHandling:
    date_from = None
    date_to = None

    def __init__(self, date_list: list, date1: str, date2=None):
        if date2 is None:
            date2 = DateHandling.get_str_date_n_days_ago(date1, 90)
        self.date_from, self.date_to = DateHandling.rearrange_date_arguments(date1, date2)
        self.date_from = DateHandling.get_substantive_start_date(self.date_from, date_list)
        self.date_to = DateHandling.get_substantive_end_date(self.date_to, date_list)

    @staticmethod
    def get_str_date_n_days_ago(argdate: str, n: int):
        """
        :param argdate: a reference date string
        :param n: days apart from argdate
        :return: a date which argdate - n
        """
        return (dt.strptime(argdate, '%Y%m%d') - timedelta(days=n)).strftime('%Y%m%d')

    @staticmethod
    def rearrange_date_arguments(date_from: str, date_to: str):
        return (date_from, date_to) if date_from <= date_to else (date_to, date_from)

    @staticmethod
    def get_substantive_start_date(str_date: str, list_date: list):
        return min(list_date) if str_date not in list_date else str_date

    @staticmethod
    def get_substantive_end_date(str_date: str, list_date: list):
        return max(list_date) if str_date not in list_date else str_date

    @staticmethod
    def convert_to_date_object(date_of_content: str):
        return dt.strptime(date_of_content, "%Y-%m-%dT%H:%M+09:00")
