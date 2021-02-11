# -*- coding: utf-8 -*-
import logging
import os
import time

from common.get_config import cf


class GetLog():
    # 定义绝对路径(项目的根路径)
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 初始化我们的生成器对象，log生成器的对象
    def __init__(self):
        # logger表示一个生成器的对象
        self.logger = logging.getLogger()
        # 设置一个最低的默认的日志等级，我们的生成器本身默认的等级
        self.logger.setLevel(logging.INFO)
        # self.logger.setLevel(10)
        # 定义一个格式化器，让处理器来使用
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s",
                                           "%Y-%m-%d-%H:%M")

    # 定义流处理器，并添加流处理器到生成器
    def set_stream_handle(self):
        # 创建流处理器的对象
        self.stream_handle = logging.StreamHandler()
        # 流处理器也要日志等级
        self.stream_handle.setLevel(logging.INFO)
        # 流处理器是需要有格式的
        self.stream_handle.setFormatter(self.formatter)
        # 把流处理器弄到生成器中
        # self.logger.addHandler(self.stream_handle)

    # 定义文件处理器
    def set_file_handle(self):
        # 定义我们的时间格式，运行代码的时间
        time_format=time.strftime("%Y-%m-%d_%H", time.localtime(time.time()))+".log"
        log_file_path = os.path.join(self.base_path, "log", time_format)
        # 创建文件处理器的对象
        # 定义一个mode的变量，通过配置文件的方式去改变
        mode=cf.get_value("log","mode")
        self.file_handle = logging.FileHandler(log_file_path,mode=mode)
        # 设定文件处理器的日志等级
        self.file_handle.setLevel(logging.INFO)
        # 把格式化器弄到文件处理器中
        self.file_handle.setFormatter(self.formatter)

    # 把流处理器放入到我们的生成器中
    # 把文件处理器放到我摸的生成器中
    def get_logger(self):
        # 先运行定义流处理器
        # 调用这个方法，1，先创建流处理器对象，由于已经写了self.流处理对象
        # 因为这个流处理器需要有日志等级，所以要设置日志等级，就在第20行代码执行
        # 因为流处理器需要有格式，那么就在第22行代码执行
        self.set_stream_handle()
        # 生成器添加流处理器
        # 生成器对象logger，通过addHandler方法，把流处理器对象弄到自己的碗里来~
        self.logger.addHandler(self.stream_handle)
        # 使用上面定义的方法，生成文件处理器
        self.set_file_handle()
        # 把文件处理器放到生成器中
        self.logger.addHandler(self.file_handle)
        return self.logger


# 1.先把log类初始化，GetLog()
# 2.通过get_logger，把文件处理器和流处理器放到生成器中
# 3.get_logger必须返回一个生成器对象，这样子就可以直接使用

# 直接把log放到类下面，叫做单例模式
log = GetLog().get_logger()

if __name__ == "__main__":
    # 创建日志的类的对象,直接创建了生成器
    log = GetLog()
    # 创建了日志的流处理器，并把流处理器放入到生成器中
    log.get_logger()
    # log.set_stream_handle()
    # 这是打印info等级的日志
    log.logger.info("tongtong")
    # print(log.base_path)
