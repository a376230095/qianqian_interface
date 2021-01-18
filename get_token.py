# -*- coding: utf-8 -*-

# 获取access_token
import requests
from common.get_config import GetConfig


def get_token(secret):
    id = "ww630f49269e06f865"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}"
    print(url)
    res = requests.get(url=url)
    print(res)
    # res一个响应的对象，属性
    # print(res.text)
    # 想要获取access_token，但是text是一个字符串，要从字符串提取子字符串，需要用到正则
    # 如果响应体是一个字典的话，获取token很方便,用requests的json方法，把响应体变成字典
    return res.json()["access_token"]


# 这个代码他找不到config.ini这个文件，导致了代码错误了
contact_secret = GetConfig().get_value("weixin", "contact_secret")
print(get_token(contact_secret))
