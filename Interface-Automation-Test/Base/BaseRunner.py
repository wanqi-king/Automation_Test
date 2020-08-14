# -*- coding: utf-8 -*-
import unittest
import requests
import time
import sys
import hashlib


def md5_key(arg):
    md5 = hashlib.md5()
    md5.update(arg.encode("utf8"))
    return md5.hexdigest()

def get_session():
    req = requests.session()
    url = "http://192.168.16.60/login"
    account = "TMHZG"
    password = "Zou123456"
    password = md5_key(password)
    print("正在请求令牌……")
    data = {'username': account, 'password': password}
    try:
        rps = req.post(url, data=data, verify=False)
        print("令牌获取成功:\n", rps.headers['Set-Cookie'].split(';')[0])
        # print("令牌获取成功:\n", rps.json()['data']['token'])               ---------- 注：暂不支持目前版本，不含有JWT，目前只有cookie
        print("3秒后执行测试")
        return rps.headers['Set-Cookie'].split(';')[0]
        # return rps.json()['data']['token']# 返回登录后的token                ---------- 注：暂不支持目前版本，不含有JWT，目前只有cookie
    except:
        print("异常中断,15秒后结束脚本")


class ParametrizedTestCase(unittest.TestCase):
    """ 需要参数化的测试用例类从此类继承
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        cls.token = get_session()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @staticmethod
    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


