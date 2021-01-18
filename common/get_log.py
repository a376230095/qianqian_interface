#-*- coding: utf-8 -*-
import logging
class GetLog():

    # 初始化我们的生成器对象，log生成器的对象
    def __init__(self):
        # logger表示一个生成器的对象
        self.logger=logging.getLogger()
        # 设置一个最低的默认的日志等级，我们的生成器本身默认的等级
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(10)
        # 定义一个格式化器，让处理器来使用
        self.formatter=logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s", "%Y-%m-%d-%H:%M")

    # 定义流处理器，并添加流处理器到生成器
    def set_stream_handle(self):
        # 创建流处理器的对象
        self.stream_handle=logging.StreamHandler()
        # 流处理器也要日志等级
        self.stream_handle.setLevel(logging.DEBUG)
        # 流处理器是需要有格式的
        self.stream_handle.setFormatter(self.formatter)
        # 把流处理器弄到生成器中
        # self.logger.addHandler(self.stream_handle)



    # 把流处理器放入到我们的生成器中
    def get_logger(self):
        pass
        # 先运行定义流处理器
        # 调用这个方法，1，先创建流处理器对象，由于已经写了self.流处理对象
        # 因为这个流处理器需要有日志等级，所以要设置日志等级，就在第20行代码执行
        # 因为流处理器需要有格式，那么就在第22行代码执行
        # self.set_stream_handle()
        # 生成器添加流处理器
        # 生成器对象logger，通过addHandler方法，把流处理器对象弄到自己的碗里来~
        # self.logger.addHandler(self.stream_handle)


if __name__=="__main__":
    # 创建日志的类的对象,直接创建了生成器
    log=GetLog()
    # 创建了日志的流处理器，并把流处理器放入到生成器中
    # log.get_logger()
    log.set_stream_handle()
    # 这是打印info等级的日志
    log.logger.info("tongtong")
    print("2021-01-18-22:25|INFO  |get_log.py:38 | tongtong")
