import logging
import os
import time
from config import BasePath


class GetLog:
    __logger = None
    @classmethod
    def get_log(cls):
        if cls.__logger is None:
            cls.__logger = logging.getLogger("million_logger")
            cls.__logger.setLevel(logging.INFO)
            handler1 = logging.StreamHandler()
            handler2 = logging.FileHandler(filename=BasePath+os.sep+"log"+os.sep+"{}_log".format(time.strftime("%Y%m%d %H%M%S",time.localtime())),encoding="utf-8")
            format = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",datefmt = "%Y%m%d%X")

            handler1.setFormatter(format)
            handler2.setFormatter(format)

            cls.__logger.addHandler(handler1)
            cls.__logger.addHandler(handler2)

        return cls.__logger
