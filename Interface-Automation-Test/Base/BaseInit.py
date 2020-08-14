from Base.BaseFile import BaseFile
from Base.BaseElementEnmu import Element


class BaseInit(object):
    def __init__(self):
        self.bf = BaseFile()

    #将原文件删除并创建新文件
    def mk_file(self):
        self.__destroy()
        self.bf.mk_file(Element.INFO_FILE)

    def __destroy(self):
        self.bf.remove_file(Element.INFO_FILE)
