#-*- coding: utf-8 -*-
import time

# 打印时间戳
# print(time.time())

# 2021-02-11_10

# 获取30天前的时间戳
thirty=time.time()-(3600*24*30)
print(time.strftime("%Y-%m-%d_%H", time.localtime(thirty)))