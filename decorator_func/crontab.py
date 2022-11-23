import functools

import schedule


def crontab(timestamp):

    def _crontab(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 指定定时器的执行周期
            schedule.every().day.at(timestamp).do(func, *args, **kwargs)

            def register_task():
                while True:
                    schedule.run_pending()

            return register_task

        return wrapper

    return _crontab
