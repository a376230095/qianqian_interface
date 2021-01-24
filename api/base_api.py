# -*- coding: utf-8 -*-
# 这是父类，其他类去继承他
import requests


class BaseApi():

    # 定义一个方法，这个方法虽然在类里面，但不想用类的属性和方法，或者是对象的属性和方法
    @staticmethod
    def a():
        print("abc")

    def get_token(self,secret):
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


if __name__ == "__main__":
    a = BaseApi()
    print(a.a())
