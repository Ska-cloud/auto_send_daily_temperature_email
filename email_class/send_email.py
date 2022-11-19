import logging
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText


class SendEmail:
    SMTP_SERVER = 'smtp.qq.com'

    def __init__(self, sender: str, receiver: str, username: str, pop_token: str, theme: str):
        self.sender = sender
        self.receiver = receiver
        self.username = username
        self.pop_token = pop_token
        self.theme = theme

    def send_email(self, mail_content: str) -> bool:
        message = MIMEText(mail_content, 'html', 'utf-8')
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = Header(self.theme, 'utf-8')

        try:
            smtp = smtplib.SMTP()
            smtp.connect(SendEmail.SMTP_SERVER)
            smtp.login(self.username, self.pop_token)
            smtp.sendmail(self.sender, self.receiver, message.as_string())
            smtp.quit()
            logging.info(f"""{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, send success""")
            return True
        except smtplib.SMTPException as e:
            logging.exception(f"""{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, send fail,{e}""")
            return False


if __name__ == '__main__':
    send_email = SendEmail('1037719686@qq.com', '1037719686@qq.com', '1037719686@qq.com', 'wziwhpkhtsujbcbj', 'test')
    send_email.send_email('./email_template.html')
