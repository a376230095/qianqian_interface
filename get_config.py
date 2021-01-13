#-*- coding: utf-8 -*-
import configparser


# 想定义一个config对象
config=configparser.ConfigParser()
# 读取config文件的内容
config.read("config.ini",encoding="UTF-8")
# 获取config文件内容的东西
# 通过section和option获取value值
contact_secret=config.get("weixin","contact_secret")
print(contact_secret)


def __init__():
    # 想定义一个config对象
    config=configparser.ConfigParser()
    # 读取config文件的内容
    config.read("config.ini",encoding="UTF-8")
    return config
# 获取config文件内容的东西
# 通过section和option获取value值

def get_config_value():
    config=get_config()
    contact_secret=config.get("weixin","contact_secret")
    print(contact_secret)

## 弄成一个class的话





