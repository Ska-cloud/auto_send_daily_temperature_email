import time
import logging

import requests

from utils.load_yaml import load_yml


class BaiduAPI:
    AK_TOKEN = ""

    def __init__(self, district_id: str):
        config = load_yml('config.yaml')
        BaiduAPI.AK_TOKEN = config.get('ak_token')
        self.district_id = district_id
        self.url = f"https://api.map.baidu.com/weather/v1/?district_id={self.district_id}&data_type=all&ak={BaiduAPI.AK_TOKEN}"

    def get_today_weather(self) -> dict:
        content = dict()
        try:
            content = requests.get(self.url).json()
            logging.info(f"""api_url: {self.url}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, success require temperature info""")
        except Exception as e:
            logging.exception(f"""api_url: {self.url}, {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, fail require temperature info, {e}""")
        if content:
            city = content['result']['location']['province']
            text_day = content['result']['forecasts'][0]['text_day']
            temperature_high = content['result']['forecasts'][0]['high']
            temperature_low = content['result']['forecasts'][0]['low']
            wind_score = content['result']['forecasts'][0]['wc_day']
            feels_like = content['result']['now']['feels_like']
        else:
            city = ''
            text_day = ''
            temperature_high = ''
            temperature_low = ''
            wind_score = ''
            feels_like = ''

        return {
            "city": city,
            "text_day": text_day,
            "temperature_high": temperature_high,
            'temperature_low': temperature_low,
            'wind_score': wind_score,
            "feels_like": feels_like,
            'forecasts': content['result']['forecasts']
        }


if __name__ == '__main__':
    baidu_api = BaiduAPI("310100")
    baidu_api.get_today_weather()
