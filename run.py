import datetime

from api.baidu_weather_api import BaiduAPI
from email_class import DO_JOB_TIME, DISTRICT_ID, SENDER, RECEIVER, USERNAME, POP_TOKEN
from email_class.generate_email_template import GenerateEmailTemplate
from email_class.send_email import SendEmail
from api.tianxing_api import TianXingDataAPI
from decorator_func.crontab import crontab
from utils import birthday
from utils import fall_in_love_day
# from utils.draw import Draw


class Run:
    def __init__(self):
        import logging

        logging.basicConfig(level=logging.INFO,
                            filename='log/run.log',
                            filemode='a',
                            format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        self.today_str = datetime.datetime.now().strftime('%Y-%m-%d')
        self.theme = f"{self.today_str}"
        print('----------------------自动发送邮件脚本已启动----------------------')

    @crontab(DO_JOB_TIME)
    def work(self):
        # 天气信息
        baidu_api = BaiduAPI(DISTRICT_ID)
        weather = baidu_api()

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

        send_email = SendEmail(sender=SENDER,
                               receiver=RECEIVER,
                               username=USERNAME,
                               pop_token=POP_TOKEN,
                               theme=self.theme)
        # 发送邮件
        result = send_email.send_email(mail_content=mail_content)

        # 反馈邮箱对象
        feedback_email = SendEmail(sender=SENDER,
                                   receiver=SENDER,
                                   username=USERNAME,
                                   pop_token=POP_TOKEN,
                                   theme=self.theme)
        if result:
            feedback_email.send_email(f"{self.today_str}, 发送成功")
        else:
            feedback_email.send_email(f"{self.today_str}, 发送失败")

    def __str__(self):
        return f"每天{DO_JOB_TIME}，定时发送邮件"


if __name__ == '__main__':
    run = Run()
    crontab_task = run.work()
    crontab_task()
