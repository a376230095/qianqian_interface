#-*- coding: utf-8 -*-
from api.contact.member_api import Member


class TestMember():

    # 增加联系人
    def test_add_member(self):
        # 引用member类
        member=Member()
        res=member.add_member()
        # 要加一个判断
        # 先断言errcode
        assert res["errcode"]==60103
        assert res["errmsg"]=="Warning: wrong json format. mobile existed:ZengZhiTon"
