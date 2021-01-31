# -*- coding: utf-8 -*-
# 这是父类，其他类去继承他
import os
from string import Template

import requests
import yaml


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

    # 读取yaml文件
    def get_yaml(self,path):
        yaml_path = os.path.join(self.base_path,path)
        with open(yaml_path,encoding="utf-8") as f:
            # 拿过来的字典需要完善，去完善params参数
            request_data=yaml.safe_load(f.read())
        return request_data

    # 使用模板技术，让yaml文件可以使用变量
    def template(self,path,data:dict):
        # 函数需要传两个值，一个是路径，yaml文件的路径
        # 函数需要传两个值，一个是字典data，是需要改变的变量的值
        # 比如要改变yaml文件的5个变量值，就需要写5个key和value的值
        # token、userid、mobile、name、department
        # key就是需要改变的变量名，value就是改变成什么样子
        # data={"token":"1234","userid":"tong1234","name":"tong",
        #       "mobile":"13172661165","department":[1,2]}
        # 导入这个类from string import Template
        # Template(变量)，变量接收一个字符串类型
        yaml_path = os.path.join(self.base_path, path)
        with open(yaml_path,encoding="utf-8") as f:
            # substitute(变量)是指要替换的内容，也就是我们的data
            # Template(f.read()).substitute(data)内容的返回值是一个字符串
            change_str=Template(f.read()).substitute(data)
            '''
            "method": "post"
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create"
            "params": "access_token=1234"
            "json":
                "userid": tong1234
                "name": tong
                "mobile": 13172661165
                "department": [1,2]
            '''
            # 由于change_str虽然改变了变量，但是get_res里面需要传一个字典
            # 因此需要把change_str改变成字典，通过yaml.safe_load去读取就好了
            request_data=yaml.safe_load(change_str)
            # yaml.safe_load方法的最终目的是不是想要获取一个字典
            # 只要safe_load(变量)，只要符合yaml文件的格式要求，是不是都可以把变量完美的变成python的字典呀
            # request_data=yaml.safe_load(Template(f.read()).substitute(data))

        return request_data



if __name__ == "__main__":
    a = BaseApi()
    # request_data={
    #     "method":"get",
    #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #     "params":"corpid=ID&corpsecret=SECRET",
    #     "json":None
    # }
    # print(a.get_res(request_data).text)
    print(a.get_yaml("data/api/contact/member/add_member_api.yml"))
