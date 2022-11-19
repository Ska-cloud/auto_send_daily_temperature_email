import schedule
from utils.load_yaml import load_yml


def crontab(func):
    config = load_yml('config.yaml')
    job_time = config.get('do_job_time')

    def inner(*args, **kwargs):
        # 指定定时器的执行周期
        schedule.every().day.at(job_time).do(func)

        def register_task():
            while True:
                schedule.run_pending()
                # time.sleep(1)

        return register_task

    return inner
