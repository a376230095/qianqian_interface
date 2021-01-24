#-*- coding: utf-8 -*-

class Tong():

    # 定义类属性

    class_name="tong11"
    class_age=291

    # 定义对象属性
    def __init__(self,name,age):
        # self表示对象，对象.，就等于self.
        self.name=name
        self.age=age

    # 定义一个普通的方法(对象的方法)
    def object_method(self):
        print("bbb")

    # 定义一个类方法
    @classmethod
    def class_method(cls):
        # cls表示类,通过类.，相当于cls.
        print("abc")

    # 定义一个类方法，到底能不能去使用对象的属性呢？或者是对象的方法呢？
    # 类方法，是不可以使用对象方法的
    @classmethod
    def class_method1(cls):
        # 如果强迫性把cls改成self，也是不行的，因为看下一句话
        # 这里的self，是类.，等价于self.
        cls.object_method()

    # 静态方法，我不使用类的属性、方法、不使用对象的属性和方法
    @staticmethod
    def static_method():
        b=28



if __name__=="__main__":
    # print(Tong("tong", 26).name)
    # Tong.class_method1()
    # 类是无法直接访问对象属性
    # print(Tong.name) 会报错
    # 只要对象，才能去访问对象的属性
    # print(Tong("tong",28).name)
    # print(Tong("tong",28).age)
    # 类是可以访问类对象的
    # Tong.class_method()
    # 对象不知道能不能访问类方法
    # Tong("tong",27).class_method()
    # 对象，能不能使用类属性呢？
    # print(Tong("tong", 26).class_name)
    # 对象能不能去改变类属性
    # a=Tong("tong", 26)
    # 当对象直接使用类属性之后，这个属性，就会变成对象属性了
    # a.class_name="qianqian"
    # print(a.class_name)
    # print(Tong.class_name)