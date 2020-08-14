# from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from business.business import browser, switch_new_ck, switch_hold_ck


# browser = webdriver.Firefox()
# browser.get("http://10.102.1.3/index")
# browser.implicitly_wait(5)


# 登录
def login(username,password):
    browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/button').click()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/input').send_keys(username)
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input').send_keys(password)
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/button').click()


# 判断登录成功与否
def chack_login():
    sleep(1)
    e = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/div[4]')
    ActionChains(browser).move_to_element(e).perform()
    try:
        login_contrast = browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/ul/li/span")
        assert login_contrast.text == '退出'
    except:
        return False
    else:
        return True


def logout():
    e = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/div[4]')
    ActionChains(browser).move_to_element(e).perform()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/ul/li/span').click()
    sleep(1)
    browser.find_element_by_css_selector('html body div._2I2o7 div._9aPJQ.undefined div._1c9Ni button.dSVFM').click()
    sleep(1)
    try:
        browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/button')
    except:
        print('退出失败')
    else:
        print('退出成功')


# 机场航司筛选工具-热门机场推荐-广州白云-查看详情
def screen_rm_gzby():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]').click()
    sleep(1)
    browser.close()
    sleep(1)
    switch_new_ck()
    sleep(1)
    try:
        gzby = browser.find_element_by_xpath('//*[@id="contain"]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert gzby.text == '广州白云国际机场'
    except:
        return False
    else:
        return True



# 机场航司筛选工具-热门机场推荐-上海浦东-查看详情
def screen_rm_shpd():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        shpd = browser.find_element_by_xpath('//*[@id="contain"]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert shpd.text == '上海浦东国际机场'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门机场推荐-北京首都-查看详情
def screen_rm_bjsd():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        bjsd = browser.find_element_by_xpath('//*[@id="contain"]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert bjsd.text == '北京首都国际机场'
    except:
        return  False
    else:
        return True


# 机场航司筛选工具-热门机场推荐-深圳宝安-查看详情
def screen_rm_szba():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[4]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        szba = browser.find_element_by_xpath('//*[@id="contain"]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert szba.text == '深圳宝安国际机场'
    except:
        return  False
    else:
        return True

# 机场航司筛选工具-热门航司推荐-东方航空-查看详情
def screen_rmhs_dfhk():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        dfhk = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[2]')
        assert dfhk.text == '东方航空'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门航司推荐-海南航空-查看详情
def screen_rmhs_hnhk():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[2]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        hnhk = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[2]')
        assert hnhk.text == '海南航空'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门航司推荐-中国航空-查看详情
def screen_rmhs_zghk():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        zghk = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[2]')
        assert zghk.text == '中国航空'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门航司推荐-南方航空-查看详情
def screen_rmhs_nfhk():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        nfhk = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[2]')
        assert nfhk.text == '南方航空'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门城市推荐-广州-查看详情
def screen_rmcs_gz():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        gz = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert gz.text == '广州'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门城市推荐-深圳-查看详情
def screen_rmcs_sz():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        sz = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert sz.text == '深圳'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门城市推荐-上海-查看详情
def screen_rmcs_sh():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[3]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        sh = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert sh.text == '上海'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-热门城市推荐-北京-查看详情
def screen_rmcs_bj():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[4]').click()
    sleep(1)
    browser.close()
    switch_new_ck()
    sleep(1)
    try:
        bj = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span[2]')
        assert bj.text == '北京'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-查看所有机场
def screen_see_jc():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_link_text('查看所有机场 >').click()
    sleep(1)
    try:
        see_jc = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/h3')
        assert see_jc.text == '所有机场'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-查看所有航司
def screen_see_hs():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_link_text('查看所有航司 >').click()
    sleep(1)
    try:
        see_hs = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/h3')
        assert see_hs.text == '所有航司'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-查看所有城市
def screen_see_cs():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_link_text('查看所有城市 >').click()
    sleep(1)
    try:
        see_cs = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[3]/div[4]/div[2]/div[1]/h3')
        assert see_cs.text == '所有城市'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-机场筛选
def screen_jc():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/span[14]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span[7]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[3]/div[2]/span[4]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/div[2]/span[6]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[6]/div[2]/span').click()
    sleep(1)
    try:
        selected_1 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
        selected_2 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        selected_3 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/span')
        selected_4 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[4]/span')
        assert selected_1.text == '4F' and selected_2.text\
               == '多跑道机场' and selected_3.text == '1000万以上' and selected_4.text == '西南'
    except:
        return False
    else:
        return True


# 机场航司筛选工具-航司筛选
def screen_hs():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/span[6]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[contains(text(),"E190")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[contains(text(),"成都双流国际机场")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[6]/div[2]/span').click()
    sleep(1)
    try:
        selected_1 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
        selected_2 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        selected_3 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/span')
        selected_4 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[4]/span')
        assert selected_1.text == '已发布需求' and selected_2.text == '有国际航权' and selected_3.text == 'E190' and selected_4.text == '成都双流国际机场'
    except:
        return False
    else:
        return True


# 航司机场筛选工具-查看详情-更多
# def sereen_more():
#     switch_hold_ck()
#     sleep(1)
#     browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]/div[2]').click()
#     sleep(1)
#     browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]').click()
#     sleep(1)
#     browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]').click()
#     sleep(1)
#     browser.find_element_by_xpath()


# 航司机场筛选工具-城市
def screen_caty():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[4]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[4]').click()
    sleep(1)
    try:
        caty = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div/div[3]/div[4]/div[2]/div[1]/h3')
        assert caty.text == '所有城市'
    except:
        return False
    else:
        return True


# 航司机场筛选工具-机场筛选-选择筛选条件-清空数据-选择筛选条件-查询
def screen_jc_qk():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/span[6]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span[4]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[3]/div[2]/span[3]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/span[8]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/div[2]/span[3]').click()
    sleep(1)
    #  清空数据
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[6]/div[1]/span').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/span[2]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span[1]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[3]/div[2]/div/input[1]')\
        .send_keys('1500')
    sleep(1)
    qk_clear = browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[3]/div[2]/div/input[2]')
    qk_clear.clear()
    sleep(1)
    qk_clear.send_keys('5000')
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/span[3]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/div[2]/span[6]').click()
    sleep(1)
    # 点击查询
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[6]/div[2]').click()
    sleep(1)
    try:
        contrast_qk1 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
        contrast_qk2 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        contrast_qk3 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/span')
        contrast_qk4 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[4]/span')
        contrast_qk5 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]/span')
        assert contrast_qk1.text == '1A' and contrast_qk2.text == '高原机场' and contrast_qk3.text\
               == '1500万-500…' and contrast_qk4.text == '偏商务' and contrast_qk5.text == '西南'
    except:
        return False
    else:
        return True


# 航司机场筛选工具-航司筛选-选择筛选条件-清空数据-选择筛选条件-查询
def screen_hs_qk():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div[3]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"MD90")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"兰州中川国际机场")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[6]/div[2]/span').click()
    sleep(1)
    # 清空数据
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[6]/div[1]/span').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/span[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('//*[contains(text(),"ERJ145")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"无锡苏南硕放国际机场")]').click()
    sleep(1)
    try:
        contrast_hs_qk1 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
        contrast_hs_qk2 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        contrast_hs_qk3 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/span')
        contrast_hs_qk4 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[4]/span')
        contrast_hs_qk5 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[5]/span')
        assert contrast_hs_qk1.text == '安全度高' and contrast_hs_qk2.text == '全服务航空' and contrast_hs_qk3.text == \
               '有国际航权' and contrast_hs_qk4.text == 'ERJ145' and contrast_hs_qk5.text == '无锡苏南硕放国际机…'
    except:
        return False
    else:
        return True


# 航司机场筛选工具-航司筛选-选择筛选条件-查询-选择筛选条件-查询
def screen_hs_cf():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div[3]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[2]')
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/span[1]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"MD90")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"兰州中川国际机场")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[6]/div[2]/span').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/span[3]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"B737-900")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[contains(text(),"上海虹桥国际机场")]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[6]/div[2]/span').click()
    sleep(1)
    try:
        hs_cf1 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
        hs_cf2 = browser.find_element_by_xpath \
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        hs_cf3 = browser.find_element_by_xpath \
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/span')
        hs_cf4 = browser.find_element_by_xpath \
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[4]/span')
        hs_cf5 = browser.find_element_by_xpath \
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[5]/span')
        assert hs_cf1.text == '收益最高' and hs_cf2.text == '全服务航空' and hs_cf3.text == '有国际航权' and \
            hs_cf4.text == 'B737-900' and hs_cf5.text == '上海虹桥国际机场'
    except:
        return False
    else:
        return True


# 航司机场筛选工具-机场筛选-选择筛选条件-查询-选择筛选条件-查询
def screen_jc_cf():
    switch_hold_ck()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]').click()
    sleep(1)
    switch_new_ck()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath \
        ('/html/body/div[1]/div/div[3]/div/div[2]').click()
    sleep(1)
    browser.find_element_by_xpath \
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/span[6]').click()
    browser.find_element_by_xpath \
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/span[4]').click()
    browser.find_element_by_xpath \
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[3]/div[2]/span[3]').click()
    browser.find_element_by_xpath \
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/span[8]').click()
    browser.find_element_by_xpath \
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/div[2]/span[3]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[6]/div[2]/span').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/span[2]').click()
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/div[1]/span[2]').click()
    sleep(1)
    browser.find_element_by_xpath\
        ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[6]/div[2]').click()
    try:
        jc_cf1 = browser.find_element_by_xpath\
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
        jc_cf2 = browser.find_element_by_xpath \
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        jc_cf3 = browser.find_element_by_xpath \
            ('/html/body/div[1]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/span')
        assert jc_cf1.text == '1A' and jc_cf2.text == '高原机场' and jc_cf3.text == '偏商务'
    except:
        return False
    else:
        return True









if __name__ == '__main__':
    login('tmadmin','Aa123456')
    screen_rm_gzby()