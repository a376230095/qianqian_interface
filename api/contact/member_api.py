#-*- coding: utf-8 -*-
# 这个是通讯录的api的类，实现通讯录的增删改查
import os
from pprint import pprint

import requests
import yaml


from api.base_api import BaseApi
from common.get_config import GetConfig
from common.get_log import log


class Member(BaseApi):

    request_data_path="data/api/contact/member/add_member_api.yml"

    # 增加成员
    # def add_member(self):
    #     contact_secret = GetConfig().get_value("weixin", "contact_secret")
    #     # 增加成员
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token(contact_secret)}"
    #     data_request = {
    #         "userid": "zhangsan",
    #         "name": "张三",
    #         "alias": "jackzhang",
    #         "mobile": "+86 13800000000",
    #         "department": [1, 2]
    #     }
    #     res = requests.post(url=url, json=data_request)
    #     return res

    # 增加成员
    # def add_member(self):
    #     contact_secret = GetConfig().get_value("weixin", "contact_secret")
    #     # 定义一个请求内容
    #     request_data={
    #         "method":"post",
    #         "url":"https://qyapi.weixin.qq.com/cgi-bin/user/create",
    #         "params":f"access_token={self.get_token(contact_secret)}",
    #         "json":{
    #             "userid": "zhangsan",
    #             "name": "张三",
    #             "alias": "jackzhang",
    #             "mobile": "+86 13800000000",
    #             "department": [1, 2]}
    #     }
    #     res=self.get_res(request_data)
    #     return res

    # # 增加成员
    # def add_member(self):
    #     contact_secret = GetConfig().get_value("weixin", "contact_secret")
    #     yaml_path=os.path.join(self.base_path,"data/api/contact/member/add_member_api.yml")
    #     with open(yaml_path,encoding="utf-8") as f:
    #         # 拿过来的字典需要完善，去完善params参数
    #         request_data=yaml.safe_load(f)
    #         # 改变params参数的value值
    #         request_data["params"]=f"access_token={self.get_token(contact_secret)}"
    #         pprint(request_data)
    #     res=self.get_res(request_data)
    #     return res

    # 增加成员
    def add_member(self,userid,name,mobile,department,gender,position):
        contact_secret = GetConfig().get_value("weixin", "contact_secret")
        data={"token":f"{self.get_token(contact_secret)}","userid":userid,"name":name,
              "mobile":mobile,"department":department,"position":position,
              "gender":gender}
        request_data=self.template(self.request_data_path,data,"add")
        # 打印一下request_data，看看None值有没有传进去
        res=self.get_res(request_data)
        return res


    # 删除成员
    def delete_member(self,userid):
        contact_secret=GetConfig().get_value("weixin","contact_secret")
        data = {"token": f"{self.get_token(contact_secret)}", "userid": userid}
        request_data=self.template(self.request_data_path,data,"delete")
        res=self.get_res(request_data)
        return res


    # 获取成员
    def get_member(self,userid):
        contact_secret=GetConfig().get_value("weixin","contact_secret")
        data = {"token": f"{self.get_token(contact_secret)}", "userid": userid}
        request_data=self.template(self.request_data_path,data,"get")
        res=self.get_res(request_data)
        return res


    # 编辑成员
    def edit_member(self):
        pass


if __name__=="__main__":
    a=Member()
    # print(a.add_member("tong1234","tong1234","13172661165",[1,2],"manager","1"))
    print(a.add_member(None,"tong12345","13222661122",[1,2],"",""))
    # print(a.delete_member())
