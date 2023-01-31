# description : program enter main function
# author : ryanzhang
# fileName : mail.py
# date : 2022-10-06

from email.mime.multipart import MIMEMultipart
import smtplib, os, json
from email.mime.text import MIMEText
from email.header import Header
import log


def send(receivers, content):
    logger = log.logger_config(logging_name='mail')
    path = os.getcwd()
    allinfo = json.load(open(path + "/json/mail.json", encoding="utf-8"))
    for item in allinfo:
        account = item.get('account')
        password = item.get('password')
        host = item.get('server')
        port = item.get('smtp_port')
    # Mail content
    mimemsg = MIMEMultipart()
    mimemsg['From'] = account
    mimemsg['To'] = receivers
    mimemsg['Subject'] = "今日微哨打卡失败"
    mimemsg.attach(MIMEText(content, "plain", "utf-8"))

    # Mail Send
    server = smtplib.SMTP(host, int(port))
    server.starttls()
    server.login(account, password)
    server.sendmail(account, receivers, mimemsg.as_string())
    server.quit
    logger.info('{},The mail was sent successfully'.format(receivers))
    return True
