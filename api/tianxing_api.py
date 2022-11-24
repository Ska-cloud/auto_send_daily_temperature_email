import time
import logging

import requests

from . import TOKEN


class TianXingDataAPI:

    @staticmethod
    def rainbow_boast() -> dict:
        content = dict()
        url = f"https://apis.tianapi.com/caihongpi/index?key={TOKEN}"
        try:
            content = requests.get(url).json()
            logging.info(f"""api_url: {url}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, require rainbow boast success""")
        except Exception as e:
            logging.exception(f"""api_url: {url}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, require rainbow boast fail, {e}""")
        return content['result']['content']

    @staticmethod
    def daily_english() -> dict:
        content = dict()
        url = f"https://apis.tianapi.com/everyday/index?key={TOKEN}"
        try:
            content = requests.get(url).json()
            logging.info(f"""api_url: {url}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, require daily-english success""")
        except Exception as e:
            logging.exception(f"""api_url: {url}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, require daily-english fail, {e}""")

        return {'content': content['result']['content'], 'note': content['result']['note']}


if __name__ == '__main__':
    print(TianXingDataAPI.daily_english())
