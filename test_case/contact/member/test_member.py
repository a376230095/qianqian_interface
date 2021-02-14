#-*- coding: utf-8 -*-
import pytest
import allure
from api.contact.member_api import Member
from common.get_log import log

@allure.feature("通讯录中联系人的增删改查测试")
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
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.story("增加联系人")
    # @pytest.mark.parametrize(("userid,name,mobile,department,postion,gender,errcode,errmsg"),[
    #     ["","tong1234","13072661165",[1,2],"","",41009,"missing userid"],
    #     ["tong12341", "tong12341","" , [1, 2],"","",60129,"missing mobile"]
    # ],ids=["userid为空，添加失败","mobile为空，添加失败"])
    # def test_add_member(self,userid,name,mobile,department,postion,gender,errcode,errmsg):
    #     # userid为空，添加失败
    #     # mobile为空，添加失败
    #     log.info("------------开始增加联系人--------")
    #     res = self.member.add_member(userid,name,mobile,department,postion,gender)
    #     assert errcode == res["errcode"]
    #     assert errmsg in res["errmsg"]

    # 获取data数据和ids的数据
    add_data=member.get_yaml("data/api/contact/member/member_para_data.yml")["add"]["data"]
    add_ids=member.get_yaml("data/api/contact/member/member_para_data.yml")["add"]["ids"]

    def setup(self):
        # 删除联系人
        self.member.delete_member("tong1234567890")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("增加联系人")
    @pytest.mark.parametrize(("userid,name,mobile,department,postion,gender,errcode,errmsg"),
    add_data,ids=add_ids)
    def test_add_member(self,userid,name,mobile,department,postion,gender,errcode,errmsg):
        # userid为空，添加失败
        # mobile为空，添加失败
        log.info("------------开始增加联系人--------")
        res = self.member.add_member(userid,name,mobile,department,postion,gender)
        assert errcode == res["errcode"]
        assert errmsg in res["errmsg"]


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除联系人")
    def test_delete_member(self):
        log.info("------------开始删除联系人--------")
        res=self.member.delete_member("12234")
        assert res["errcode"] == 60111
        assert "userid not found" in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("获取联系人")
    def test_get_member(self):
        log.info("------------开始获取联系人--------")
        res=self.member.get_member("12234")
        assert res["errcode"] == 60111
        assert "userid not found" in res["errmsg"]





































