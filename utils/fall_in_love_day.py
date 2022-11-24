import datetime
from . import FALL_IN_LOVE_DAY


def cal_fall_in_love_days(file_path: str) -> int:
    fall_in_love_day = datetime.datetime.strptime(FALL_IN_LOVE_DAY, '%Y-%m-%d')
    today = datetime.datetime.now()
    return (today - fall_in_love_day).days


if __name__ == '__main__':
    print(cal_fall_in_love_days('../config.yaml'))
