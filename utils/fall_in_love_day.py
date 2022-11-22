import datetime

from utils import load_yaml


def cal_fall_in_love_days(file_path: str) -> int:
    config = load_yaml.load_yml(file_path)
    fall_in_love_day = config.get('fall_in_love_day')
    fall_in_love_day = datetime.datetime.strptime(fall_in_love_day, '%Y-%m-%d')
    today = datetime.datetime.now()
    return (today - fall_in_love_day).days


if __name__ == '__main__':
    print(cal_fall_in_love_days('../config.yaml'))
