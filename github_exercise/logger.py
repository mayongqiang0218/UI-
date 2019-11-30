# conding = utf-8
# /usr/bin/env python
"""
author:帅气逼人的我
date:2019/11/26 9:00
"""
import logging
import os.path
import time


class Logger(object):
    def __init__(self, logger):
        """1"""
        # 创造一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创造一个handler,用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 格式化时间
        log_path = os.path.dirname(os.path.abspath(__file__))
        log_name = log_path + '/' + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler,用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s -  %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger