# conding = utf-8
# /usr/bin/env python
"""
author:帅气逼人的我
date:2019/11/26 8:52
"""
from selenium import webdriver
from github_exercise.logger import Logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestExercise(object):
    """github练习"""

    @staticmethod
    def print_log():
        """打印出每一步的日志"""
        driver = webdriver.Chrome()
        test_logger.info("调用谷歌浏览器驱动")
        print(driver.capabilities['browserName'])
        print(driver.capabilities['browserVersion'])
        test_logger.info("查看浏览器及其版本")
        driver.implicitly_wait(600)
        test_logger.info("设置隐式等待时间为10分钟")
        driver.get("https://www.baidu.com")
        test_logger.info("打开url进入百度首页")

        win_size = driver.get_window_size()
        test_logger.info("获取窗口大小")
        driver.minimize_window()
        test_logger.info("窗口最小化")
        driver.maximize_window()
        test_logger.info("窗口最大化")
        driver.set_window_size(800, 600)
        test_logger.info("设置窗口大小为800*600")

        driver.get_screenshot_as_file("./baidu.jpg")
        test_logger.info("截取百度首页截图并保存在当前目录下")

        driver.get("https://cn.bing.com/")
        test_logger.info("进入bing首页")
        driver.back()
        test_logger.info("回退到百度页面")
        driver.refresh()
        test_logger.info("刷新Bing页面")

        input_ele = driver.find_element_by_id('kw')
        test_logger.info("使用id获得定位搜索框元素为:{}".format(input_ele))
        input_ele.send_keys("豆瓣电影")
        test_logger.info("输入文本:豆瓣电影")
        input_ele.submit()
        test_logger.info("按enter键查询")
        driver.back()
        test_logger.info("回退到百度页面")
        input_ele.clear()
        test_logger.info("清空搜索框内容")
        input_ele.send_keys("豆瓣")
        test_logger.info("输入文本:豆瓣")
        input_ele.send_keys(Keys.ENTER)
        test_logger.info("输入回车enter键进行搜索")

        douban_reading_url = driver.find_element_by_xpath(
            '//*[@id="1"]/div[3]/div[2]/a').get_attribute('href')
        test_logger.info("获取豆瓣阅读元素的链接:{}".format(douban_reading_url))
        driver.back()

        test_logger.info("回退到百度页面")
        setting_ele = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
        ActionChains(driver).move_to_element(setting_ele).perform()
        time.sleep(2)
        test_logger.info("鼠标悬停在设置按钮上2秒")
        setting_ele.click()
        test_logger.info("点击设置")
        driver.find_element_by_xpath(
            '//*[@id="wrapper"]/div[6]/a[1]').click()
        test_logger.info("点击搜索设置")
        time.sleep(2)
        sel = driver.find_element_by_xpath('//*[@id="nr"]')
        Select(sel).select_by_value('50')
        time.sleep(2)
        test_logger.info("设置每页显示条数为50")
        driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
        time.sleep(2)
        test_logger.info("点击保存")
        driver.switch_to.alert.accept()
        time.sleep(2)
        test_logger.info("点击弹框上确定")

        WebDriverWait(
            driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, 'kw')))
        test_logger.info("设置10s显示等待时间查询搜索框")

        #  多窗口切换
        handle = driver.current_window_handle
        driver.find_element_by_xpath('//*[@id="jgwab"]').click()
        test_logger.info("进入京公网安")
        handles = driver.window_handles  # 获取当前全部窗口句柄集合
        for i in handles:
            if i != handle:
                driver.switch_to.window(i)
        test_logger.info("窗口切换至京公网安")
        time.sleep(2)
        print(driver.current_url)
        test_logger.info("获取京公网安页面url")
        driver.close()
        time.sleep(2)
        driver.switch_to.window(handle)
        test_logger.info("窗口切换至百度首页")

        # 断言
        try:
            assert (driver.title == "百度，你就知道")
            print("assert succeed")
        except Exception as e:
            print('assert failed,detail as:', e)
        test_logger.info("使用断言验证标题是否正确")

        # 获取页面元素文本
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
        driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
        er = driver.find_element_by_id('TANGRAM__PSP_10__error').text
        test_logger.info("获取页面元素文本:{}".format(er))

        driver.get('file:///D:/python_myq/github_exercise/radio.html')
        # 单选框
        radios = driver.find_elements_by_xpath('//*[@type = "radio"]')
        for i in radios:
            i.click()
            time.sleep(2)
        print("radio succeed")

        # 复选框
        checkbox = driver.find_elements_by_xpath('//*[@type="checkbox"]')
        for j in checkbox:
            if j.is_selected():  # 判断是否选中：is_selected(),没点击时候返回False,点击后返回True
                continue
            else:
                j.click()
        test_logger.info('点击网页中所有单选框和多选框')

        driver.quit()
        test_logger.info('关闭浏览器结束测试')


if __name__ == '__main__':
    test_logger = Logger(logger='TestExercise').getlog()
    testlog = TestExercise()
    testlog.print_log()

