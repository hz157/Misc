'''
声明：
此Code仅供学习参考，请勿用做非法用途
'''



import json
import csv
import datetime
import requests

    
def wirtecsv(path,data):
    # printa)
    with open(path,'a',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    f.close


def csvinfo():
    # 基本信息
    position = "思明区"
    path = "/Users/macbook/Desktop/data.csv"
    # 起始时间
    start = datetime.datetime.strptime("2022-03-01 00:00:00",'%Y-%m-%d %H:%M:%S') 
    # 中间时间
    middle = datetime.datetime.strptime("2022-03-01 00:00:00",'%Y-%m-%d %H:%M:%S') 
    # 结束时间
    end = datetime.datetime.strptime("2022-05-19 00:00:00",'%Y-%m-%d %H:%M:%S') 
    # 循环累加时间间隔
    space = datetime.timedelta(days=1)
    # csv标题
    title = ['time','id','name','lng','lat','min_zoom','max_zoom','label_min_zoom','label_max_zoom']
    wirtecsv(path,title)
    # 总计降水量
    total = {}
    # 经纬度
    lng = {}
    lat = {}
    
    # 死循环
    while(1):
        # 如果时间超了，结束循环
        if middle >= end:
            break
        # 往后加1天
        temp = middle + space 
        ### 构造请求参数Payload
        ## 起始时间
        # 拆分日期和时间 原字符串格式：2022-03-15 00:00:00
        strstart = str(start)
        strtemp = str(temp)
        dt = strstart.split(" ")
        # 拆分时间 原字符串格式：00:00:00
        time = dt[1].split(":")
        # 构造请求起始参数
        startpayload = "time=%5B" + dt[0] + "T" + time[0] + "%3A" + time[1] + "%3A" + time[2] 
        ## 截止日期                  
        # 拆分日期和时间 原字符串格式：2022-03-15 00:00:00
        strend = str(end)
        dt = strend.split(" ")
        # 拆分时间 原字符串格式：00:00:00
        time = dt[1].split(":")
        # 构造请求结束参数
        endpayload = "%2C" + dt[0] + "T" + time[0] + "%3A" + time[1] + "%3A" + time[2] + "%5D"
        # 拼接请求参数构造Payload
        payload = startpayload + endpayload
        # 请求地址构造
        url = "http://222.76.243.39:9101/rain?no_data_visible=false&hour_duration=24&" + payload
        l = ['time','id','name','lng','lat','val','type_name','address','area_name','city_name']
        # request GET请求
        f = requests.get(url)
        # 将返回数据加载为JSON格式
        d = dict(json.loads(f.text))
        # 获取关键字data内的数据
        d = d['data']

        data = [] # 所有数据
        single = {}
        total = {}

        # 循环d的长度 即实际数据有多少条循环多少次
        for i in range(len(d)):  
            # 如果关键字area_name的键值对与前面给出的位置信息一致，进入执行
            if d[i]['area_name'] == position:
                # 清空data内的数据
                data = []
                data.clear()
                # 获取第一层标题(无效数据)
                for j in d[i].keys():
                    single[j] = d[i][j]
                # 获取第二层数据(部分有效)
                for j in single.keys():
                    if j == 'display': 
                        rain = dict(single[j])
                # 获取有关降雨数据的标头
                water = rain['water']
                # 获取实际有效数据
                for k in water.keys():
                    single[k] = water[k]
                # 清空标题，下次获取
                del single['display']
                # 获取真实有效数据并写入CSV
                name = d[i]['name']
                for s in title:
                    # 经纬度
                    if(s=='lng'):
                        lng[name] = str(single['lng'])
                    if(s=='lat'):
                        lat[name] = str(single['lat'])
                    # 其他数据
                    data.append(str(single[s]))
                wirtecsv(path,data)
                # 累计总和
                total[name] = d[i]['val']
        middle = temp
        print(strstart+ "——" + strtemp)
    path_total = "/Users/macbook/Desktop/sum.csv"
    titlefortotal = ['name','value','lng','lat']
    alldata = []
    wirtecsv(path_total,titlefortotal)
    for j in total.keys():
        alldata.clear()
        alldata.append(j)
        alldata.append(total[j])
        alldata.append(lng[j])
        alldata.append(lat[j])
        wirtecsv(path_total,alldata)


# 程序入口
if __name__=="__main__":
    csvinfo()

    
