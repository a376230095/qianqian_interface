#-*- coding: utf-8 -*-
from common.get_config import GetConfig
from get_token import get_token
import requests



contact_secret = GetConfig().get_value("weixin", "contact_secret")
# 增加成员
url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token(contact_secret)}"
data_request={
    "userid": "zhangsan",
    "name": "张三",
    "alias": "jackzhang",
    "mobile": "+86 13800000000",
    "department": [1, 2]
}
# 用data去传,就表示是用表单的方式去传，企业微信要求我们用json的请求体去传，报错了
# res=requests.post(url=url,data=data_request)
# 解决这个传json的问题，需要把字典转化为json格式，json.dumps把字典转化成json
# requests给了一个方法，
res=requests.post(url=url,json=data_request)
print(res.json())
