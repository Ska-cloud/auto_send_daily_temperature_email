import datetime

from utils import load_yaml


def cal_birthday_days(file_path: str) -> int:
    config = load_yaml.load_yml(file_path)
    birthday_day = config.get('birthday_day')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    interval = (datetime.datetime.strptime(f"{today.split('-')[0]}-{'-'.join(birthday_day.split('-')[1:])}", '%Y-%m-%d')
                - datetime.datetime.now()).days + 1
    return interval if interval > 0 else (
                datetime.datetime.strptime(f"{int(today.split('-')[0]) + 1}-{'-'.join(birthday_day.split('-')[1:])}",
                                           '%Y-%m-%d')
                - datetime.datetime.now()).days + 1


if __name__ == '__main__':
    print(cal_birthday_days('../config.yaml'))
