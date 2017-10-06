# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 21:48:15 2017

@author: Administrator
"""

import sys,urllib2, json
url = 'https://api.heweather.com/x3/weather?cityid=CN101010100&key=1c7d1037d6a24778b5147ea049498218'
req = urllib2.Request(url)
resp = urllib2.urlopen(req).read()

json_data = json.loads(resp)
data = json_data['HeWeather data service 3.0'][0]
now_weather = data['now']['cond']['txt']

#获取城市
city = data['basic']['city']

#获取现在的天气、温度、体感温度、风向、风力等级
now_weather = data['now']['cond']['txt']
now_tmp = data['now']['tmp']
now_fl = data['now']['fl']
now_wind_dir = data['now']['wind']['dir']
now_wind_sc = data['now']['wind']['sc']

#今天的天气
today = data['daily_forecast'][0]
weather_day = today['cond']['txt_d']
weather_night = today['cond']['txt_n']
tmp_high = today['tmp']['max']
tmp_low = today['tmp']['min']
wind_dir = today['wind']['dir']
wind_sc = today['wind']['sc']

#天气建议

#舒适度
comf = data['suggestion']['comf']['brf']
comf_txt = data['suggestion']['comf']['txt']

#流感指数
flu = data['suggestion']['flu']['brf']
flu_txt = data['suggestion']['flu']['txt']

#穿衣指数
drsg = data['suggestion']['drsg']['brf']
drsg_txt = data['suggestion']['drsg']['txt']




