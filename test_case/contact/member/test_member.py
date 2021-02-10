#-*- coding: utf-8 -*-
import pytest

from api.contact.member_api import Member
from common.get_log import log


class TestMember():

    # 提取member类，让每个方法都公用这个member对象
    member = Member()

    # # 增加联系人
    # def test_add_member(self):
    #     # 引用member类
    #     res=self.member.add_member()
    #     # 要加一个判断
    #     # 先断言errcode
    #     assert res["errcode"]==60104
    #     # assert res["errmsg"]=="Warning: wrong json format. mobile existed:ZengZhiTong"
    #     assert "mobile existed" in res["errmsg"]
    #
    # # 删除联系人
    # def test_delete_member(self):
    #     # 引用member类
    #     res=self.member.delete_member()
    #     assert res["errcode"] == 60111
    #     assert "userid not found" in res["errmsg"]

    #
    @pytest.mark.parametrize(("userid,name,mobile,department,errcode,errmsg"),(
        ["","tong1234","13072661165",[1,2],41009,"missing userid"],
        ["tong12341", "tong12341","" , [1, 2],60129,"missing mobile"]
    ),ids=["userid为空，添加失败","mobile为空，添加失败"])
    def test_add_member(self,userid,name,mobile,department,errcode,errmsg):
        # userid为空，添加失败
        # mobile为空，添加失败
        log.info("------------开始增加联系人--------")
        res = self.member.add_member(userid,name,mobile,department)
        assert errcode == res["errcode"]
        assert errmsg in res["errmsg"]


    def test_delete_member(self):
        # 引用member类
        log.info("------------开始删除联系人--------")
        res=self.member.delete_member("12234")
        assert res["errcode"] == 60111
        assert "userid not found" in res["errmsg"]





