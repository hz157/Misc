# description : program enter main function
# author : ryanzhang
# fileName : main.py
# date : 2022-10-06
import random
import sys
from datetime import datetime
import sign,post,mail
import os,time,json,log

if __name__ == '__main__':
    path = os.getcwd()
    logger = log.logger_config(logging_name='main')
    date = time.strftime("%Y/%m/%d")
    week = time.strftime("%A")
    config = json.load(open(path + "/json/config.json",encoding="utf-8"))
    if config.get("week") == "False":
        if week == "Saturday" or week == "Sunday":
            sys.exit()
    print("开始 " + date + " 的打卡任务\n")
    # 读取用户列表
    allinfo = json.load(open(path + "/json/users.json",encoding="utf-8"))
    text = '| 姓名 |  结果  |'
    sum = 0
    for item in allinfo:
        second = random.randint(0, 60)
        time.sleep(second)
        name = item.get("name")
        print("开始为 " + name + " 打卡...")
        try:
            # 获取用户cookie
            cook = sign.login(item)
            # print(cook)
            if cook.find("错误") != -1:
                # 触发异常后面的代码将无法执行
                raise Exception(cook)
            # 获取返回的打卡结果
            response = post.run(item, cook)
        except Exception as e:
            print("---为 " + name + " 打卡失败\n" + str(e))
            logger.warning('{},打卡失败'.format(item.get('stucode')))
            if config.get("email") == "True":
                mail.send(item.get('mail'), "{},您于{}执行自动打卡失败,请及时手动打卡。（此邮件仅作为提醒，请勿回复）".format(item.get('name'),datetime.datetime.today().strftime("%Y_%m_%d")))
            response = "打卡失败"
        # 为推送填写打卡信息
        text += f" \n| {name} | {response} |"


