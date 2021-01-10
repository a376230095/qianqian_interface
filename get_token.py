#-*- coding: utf-8 -*-

# 获取access_token
import requests


def get_token(secret):
    id="ww630f49269e06f865"
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}"
    res=requests.get(url=url)
    # res一个响应的对象，属性
    # print(res.text)
    # 想要获取access_token，但是text是一个字符串，要从字符串提取子字符串，需要用到正则
    # 如果响应体是一个字典的话，获取token很方便,用requests的json方法，把响应体变成字典
    return res.json()["access_token"]


