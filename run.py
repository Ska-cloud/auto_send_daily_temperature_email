import datetime

from api.baidu_weather_api import BaiduAPI
from email_class.generate_email_template import GenerateEmailTemplate
from email_class.send_email import SendEmail
from api.tianxing_api import TianXingDataAPI
from decorator_func.crontab import crontab
from utils import load_yaml
from utils import birthday
from utils import fall_in_love_day
# from utils.draw import Draw


@crontab
def work():
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    theme = f"{today_str}"
    # 天气信息
    baidu_api = BaiduAPI(__district_id)
    weather = baidu_api.get_today_weather()

    # # 生成气温走势图
    # draw = Draw(weather['forecasts'])
    # picture_code = draw.draw_temperature()

    # 每日英语
    daily_english = TianXingDataAPI.daily_english()

    # 相恋日期
    fall_love_day = fall_in_love_day.cal_fall_in_love_days('./config.yaml')

    # 生日日期
    birthday_day = birthday.cal_birthday_days('./config.yaml')

    # 生成邮件模板
    generate_email_template = GenerateEmailTemplate()
    mail_content = generate_email_template.render(
        city=weather['city'],
        text_day=weather['text_day'],
        temperature_high=weather['temperature_high'],
        temperature_low=weather['temperature_low'],
        wind_score=weather['wind_score'],
        feels_like=weather['feels_like'],
        content=daily_english['content'],
        note=daily_english['note'],
        # picture=picture_code,
        birthday_day=birthday_day,
        fall_love_day=fall_love_day
    )

    send_email = SendEmail(sender=__sender,
                           receiver=__receiver,
                           username=__username,
                           pop_token=__pop_token,
                           theme=theme)
    # 发送邮件
    result = send_email.send_email(mail_content=mail_content)

    # 反馈邮箱对象
    feedback_email = SendEmail(sender=__sender,
                               receiver=__sender,
                               username=__username,
                               pop_token=__pop_token,
                               theme=theme)
    if result:
        feedback_email.send_email(f"{today_str}, 发送成功")
    else:
        feedback_email.send_email(f"{today_str}, 发送失败")


if __name__ == '__main__':

    import logging

    logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                        filename='log/run.log',
                        filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    config = load_yaml.load_yml('./config.yaml')
    __district_id = config.get('district_id')
    __sender = config.get('sender')
    __receiver = config.get('receiver')
    __username = config.get('username')
    __pop_token = config.get('pop_token')
    print('----------------------自动发送邮件脚本已启动----------------------')

    crontab_event = work()
    crontab_event()
