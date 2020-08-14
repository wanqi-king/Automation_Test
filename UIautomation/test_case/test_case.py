import allure
import pytest
from time import sleep
import unittest

from selenium import webdriver

from test_UI.test_UI import login, screen_rm_gzby, screen_rm_shpd, screen_rm_bjsd, screen_rm_szba, \
    screen_rmhs_dfhk, screen_rmhs_hnhk, screen_rmhs_zghk, screen_rmhs_nfhk, screen_rmcs_gz, screen_rmcs_sz, \
    screen_rmcs_sh, screen_rmcs_bj, screen_see_jc, screen_see_hs, screen_see_cs, screen_jc, screen_hs, chack_login, \
    screen_jc_qk, screen_hs_qk, screen_hs_cf, screen_jc_cf
from business.business import browser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # login('TM17721869646','Aa123456')
        # self.browser = webdriver.Chrome()
        # self.browser.get('http://10.102.1.3/index')
        # self.browser.maximize_window()
        # sleep(1)
        # self.browser = browser
        # self.handles = self.browser.window_handles
        print('测试开始！')
        # login('TM17721869646','Aa123456')


    def tearDown(self) -> None:
        print('测试结束！')
        # browser.close()

    @allure.feature('登录功能')
    def test_chack_login(self):
        '''登录'''
        contrast = chack_login()
        assert contrast == bool('True')

    @allure.feature('机场航司筛选工具-热门机场推荐-广州白云-查看详情')
    def test_screen_rm_gzby(self):
        '''机场航司筛选工具-热门机场推荐-广州白云-查看详情'''
        # self.browser.switch_to_window(self.handles[-1])
        # sleep(1)
        contrast = screen_rm_gzby()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门机场推荐-上海浦东-查看详情')
    def test_screen_rm_shpd(self):
        '''机场航司筛选工具-热门机场推荐-上海浦东-查看详情'''
        contrast = screen_rm_shpd()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门机场推荐-北京首都-查看详情')
    def test_screen_rm_bjsd(self):
        '''机场航司筛选工具-热门机场推荐-北京首都-查看详情'''
        contrast = screen_rm_bjsd()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门机场推荐-深圳宝安-查看详情')
    def test_screen_rm_szba(self):
        '''机场航司筛选工具-热门机场推荐-深圳宝安-查看详情'''
        contrast = screen_rm_szba()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门航司推荐-东方航空-查看详情')
    def test_screen_rmhs_dfhk(self):
        '''机场航司筛选工具-热门航司推荐-东方航空-查看详情'''
        contrast = screen_rmhs_dfhk()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门航司推荐-海南航空-查看详情')
    def test_screen_rmhs_hnhk(self):
        '''机场航司筛选工具-热门航司推荐-海南航空-查看详情'''
        contrast = screen_rmhs_hnhk()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门航司推荐-中国航空-查看详情')
    def test_screen_rmhs_zghk(self):
        '''机场航司筛选工具-热门航司推荐-中国航空-查看详情'''
        contrast = screen_rmhs_zghk()
        assert  contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门航司推荐-南方航空-查看详情')
    def test_screen_rmhs_nfhk(self):
        '''机场航司筛选工具-热门航司推荐-南方航空-查看详情'''
        contrast = screen_rmhs_nfhk()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门城市推荐-广州-查看详情')
    def test_screen_rmcs_gz(self):
        '''机场航司筛选工具-热门城市推荐-广州-查看详情'''
        contrast = screen_rmcs_gz()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门城市推荐-深圳-查看详情')
    def test_screen_rmcs_sz(self):
        '''机场航司筛选工具-热门城市推荐-深圳-查看详情'''
        contrast = screen_rmcs_sz()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门城市推荐-上海-查看详情')
    def test_screen_rmcs_sh(self):
        '''机场航司筛选工具-热门城市推荐-上海-查看详情'''
        contrast = screen_rmcs_sh()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-热门城市推荐-北京-查看详情')
    def test_screen_rmcs_bj(self):
        '''机场航司筛选工具-热门城市推荐-北京-查看详情'''
        contrast = screen_rmcs_bj()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-查看所有机场')
    def test_screen_see_jc(self):
        '''机场航司筛选工具-查看所有机场'''
        contrast = screen_see_jc()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-查看所有航司')
    def test_screen_see_hs(self):
        '''机场航司筛选工具-查看所有航司'''
        contrast = screen_see_hs()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-查看所有城市')
    def test_screen_see_cs(self):
        '''机场航司筛选工具-查看所有城市'''
        contrast = screen_see_cs()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-机场筛选')
    def test_screen_jc(self):
        '''机场航司筛选工具-机场筛选'''
        contrast = screen_jc()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场筛选工具-航司筛选')
    def test_screen_hs(self):
        '''机场航司筛选工具-航司筛选'''
        contrast = screen_hs()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('机场航司筛选工具-城市')
    def test_screen_caty(self):
        contrast = screen_hs()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('航司机场筛选工具-机场筛选-选择筛选条件-情况数据-选择筛选条件-查询')
    def test_screen_jc_qk(self):
        contrast = screen_jc_qk()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('航司机场筛选工具-航司筛选-选择筛选条件-情况数据-选择筛选条件-查询')
    def test_screen_hs_qk(self):
        contrast = screen_hs_qk()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('航司机场筛选工具-航司筛选-选择筛选条件-查询-选择筛选条件-查询')
    def test_screen_hs_cf(self):
        contrast = screen_hs_cf()
        assert contrast == bool('True')
        browser.close()

    @allure.feature('航司机场筛选工具-机场筛选-选择筛选条件-查询-选择筛选条件-查询')
    def test_screen_jc_cf(self):
        contrast = screen_jc_cf()
        assert contrast == bool('True')
        browser.close()






if __name__ == '__main__':
    unittest.main()
    pytest.main()
