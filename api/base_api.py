# -*- coding: utf-8 -*-
# 这是父类，其他类去继承他
import os

import requests


class BaseApi():
    # 定义一个绝对路径，让其他子类都可以使用
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 定义一个方法，这个方法虽然在类里面，但不想用类的属性和方法，或者是对象的属性和方法
    @staticmethod
    def a():
        print("abc")

    def get_token(self,secret):
        id = "ww630f49269e06f865"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}"
        res = requests.get(url=url)
        # res一个响应的对象，属性
        # print(res.text)
        # 想要获取access_token，但是text是一个字符串，要从字符串提取子字符串，需要用到正则
        # 如果响应体是一个字典的话，获取token很方便,用requests的json方法，把响应体变成字典
        return res.json()["access_token"]

    # 封装requests模块，发送请求的内容，获取响应值
    def get_res(self,request_data:dict):
        # 通常获取响应的方法是,但post和get请求是不确定的，不能写死，下面的方法不可以用
        # res=requests.post()

        # 使用下面的方法封装requests模块，里面传请求需要的东西
        # 需要请求方法，method=xxx,url=xxx,params=xxx,data=xxx,json=xxx
        # 这个变量其实是相当于传一个字典进去
        # res= requests.request("变量")
        # 请求内容弄成一个字典的形式
        # request_data={
        #     "method":"get",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     "params":"corpid=ID&corpsecret=SECRET",
        #     "json":None
        # }
        # request方法里面的变量如果传一个字典的话，会自动去解包成以下的形式
        # **request_data才能进行解包，单独写request_data是不能解包的
        res=requests.request(**request_data)
        # res=requests.request(method="get",url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #                      params="corpid=ID&corpsecret=SECRET",json=None)
        return res


if __name__ == "__main__":
    a = BaseApi()
    # request_data={
    #     "method":"get",
    #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #     "params":"corpid=ID&corpsecret=SECRET",
    #     "json":None
    # }
    # print(a.get_res(request_data).text)
    print(a.base_path)
