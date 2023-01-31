# description : program enter main function
# author : ryanzhang
# fileName : post.py
# date : 2022-10-06
import os

import json
import requests
import getinfo
import log


def run(studata,cook):
    """获取处理后的数据
    :param studatae:学生信息
    :param cook:传入的cookie
    :return :打卡结果
    """
    # 读取个人提交信息
    info = getinfo.data(studata, cook)
    logger = log.logger_config(logging_name='post')
    # if info == 0:
    #     print("今日打卡已完成，自动打卡取消\n")
    #     return "已完成"

    # 提交今日打卡
    url = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    head = {
        "Cookie": cook,
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": "https://yq.weishao.com.cn",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 weishao(6.8.16) wsi18n(zh)",
        "Accept-Encoding": "gzip, deflate"
    }
    info = {
        "sch_code": studata.get('schoolcode'),
        "stu_code": studata.get('stucode'),
        "stu_name": studata.get('name'),
        "identity": "student",
        "path": "path",
        "organization" : "输入你的组织",
        "gender": "boy",
        "activityid": "5446",
        "anonymous": 0,
        "canrepeat": 1,
        "repeat_range": 1,
        "question_data": [
            {
                "questionid": 58641,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 7,
                "option_sort": 0,
                "range_value": "",
                "content": studata.get('position'),
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58642,
                "optionid": "97559",
                "optiontitle": "否",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58644,
                "optionid": "97561",
                "optiontitle": "否",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58650,
                "optionid": 97569,
                "optiontitle": "是",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58651,
                "optionid": 97573,
                "optiontitle": "校内住宿",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "hide": "false",
                "answered": "true"
            },
            {
                "questionid": 58662,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 3,
                "option_sort": 0,
                "range_value": "",
                "content": studata.get('contact'),
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "hide": "false",
                "answered": "true"
            }
        ],
        "totalArr": [
            {
                "questionid": 58641,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 7,
                "option_sort": 0,
                "range_value": "",
                "content": studata.get('position'),
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58642,
                "optionid": "97559",
                "optiontitle": "否",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58643,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 3,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58644,
                "optionid": "97561",
                "optiontitle": "否",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58645,
                "optionid": "",
                "optiontitle": "",
                "question_sort": 0,
                "question_type": 2,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58646,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58647,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 4,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58648,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58649,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 4,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58650,
                "optionid": 97569,
                "optiontitle": "是",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "answered": "true"
            },
            {
                "questionid": 58651,
                "optionid": 97573,
                "optiontitle": "校内住宿",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "hide": "false",
                "answered": "true"
            },
            {
                "questionid": 58652,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58653,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58654,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58655,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 4,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58656,
                "optionid": 97580,
                "optiontitle": "是",
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "hide": "true",
                "answered": "true"
            },
            {
                "questionid": 58657,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 8,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58658,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58659,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58660,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 1,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58661,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 3,
                "option_sort": 0,
                "range_value": "",
                "content": "",
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "",
                "answerid": 0,
                "hide": "true",
                "answered": "false"
            },
            {
                "questionid": 58662,
                "optionid": 0,
                "optiontitle": 0,
                "question_sort": 0,
                "question_type": 3,
                "option_sort": 0,
                "range_value": "",
                "content": studata.get('contact'),
                "isotheroption": 0,
                "otheroption_content": "",
                "isanswered": "true",
                "answerid": 0,
                "hide": "false",
                "answered": "true"
            }
        ],
        "private_id": 0
    }
    data = requests.post(url, json=info, headers=head)
    jsonData = json.loads(data.text)
    if jsonData.get("errcode") == 0:
        print("打卡成功！")
        logger.info('{},Sign in successfully'.format(studata.get('stucode')))
        return "成功！"
    else:
        print("---未知的errcode\n" + str(jsonData) + "\n")
        logger.warning('{},Failed to sign in,Error prompt: {}'.format(studata.get('stucode'),str(jsonData)))
        return "未知结果"