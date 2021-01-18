#-*- coding: utf-8 -*-
import configparser
# 创建一个config的类
# 定义一个根路径，解决路径引用的问题
# 同时也可以避免使用这种尴尬的东西
import os

class GetConfig():

    # 定义一个根目录
    # os.path.dirname是指上一级目录
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 实现他的初始化,创建一个config的类，返回一个config的类
    # 如何去表达根目录/config.ini
    path=os.path.join(base_path,"config.ini")
    # 如果不用的话
    # path=base_path+"/config.ini"

    def __init__(self,config_file_path=path):
        # 创建config对象
        self.config=configparser.ConfigParser()
        # 读取config文件路径，实现多个对象操作config.ini的文件(配置文件)
        self.config.read(config_file_path,encoding="UTF-8")

    # 获取value值
    def get_value(self,section,option):
        value=self.config.get(section,option)
        return value

    # 设置一下value的值
    def set_value(self,section,option,value):
        self.config.set(section,option,value)
        # self.config.set(



if __name__=="__main__":
    # 用来测试这个文件的一些逻辑有没有实现，但是并不会去影响上面代码的逻辑
    a=GetConfig()
    a.set_value("test","tong","15")
    # print(a.get_value("test","tong"))
    # print(a.get_value("weixin", "contact_secret"))
    # print(a.config.get("weixin", "contact_secret"))
    # b=GetConfig("../tong.ini")
    # print(b.config.get("tong","age"))
    # print(a.base_path)
    # print(a.path)




