#-*- coding: utf-8 -*-

class A():
    _id=10

class B(A):

    def a(self):
        return self._id


a=B()
print(a.a())