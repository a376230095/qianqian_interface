#-*- coding: utf-8 -*-
# 这个是通讯录的api的类，实现通讯录的增删改查
import requests

from api.base_api import BaseApi
from common.get_config import GetConfig


class Contact(BaseApi):

    # 增加成员
    def add_member(self):
        contact_secret = GetConfig().get_value("weixin", "contact_secret")
        # 增加成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token(contact_secret)}"
        data_request = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1, 2]
        }
        res = requests.post(url=url, json=data_request)

    # 删除成员
    def delete_member(self):

        secret=GetConfig().get_value("weixin","contact_secret")
        contact_token=self.get_token(secret)

        url="https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params=f"access_token={contact_token}&userid=USERID"
        res=requests.get(url=url,params=params)
        return res.json()


    # 获取成员
    def get_member(self):
        pass

    # 编辑成员
    def edit_member(self):
        pass


if __name__=="__main__":
    a=Contact()
    print(a.delete_member())

