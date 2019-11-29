## 自动化方法

selenium主要的包分为两个common和webdriver
Common包中主要是exceptions，这个包含了webdriver所有可能出现的例外情况，结合断言使用
webdriver包含了许多浏览器的API 

### 启动&关闭

```python
from seleniumimport webdriver # 导入webdriver包
driver = webdriver.Chrome() # 初始化一个火狐浏览器实例：driver
driver.get("https://www.baidu.com") # 通过get()方法，打开一个url站点
driver.quit() #关闭并退出浏览器
```

### 窗口大小&前后操作

maximize_window()        # 全屏

minimize_window()        # 最小化

get_window_size()  # 获取窗口尺寸

set_window_size(1280,800)  # 分辨率 1280*800，可以利用这个机器测试不同分辨率下的场景

控制浏览器后退、前进、刷新： back()、 forward()、refresh()

**示例**：

```
driver.set_window_size(800, 600)
```



### 截图

get_screenshot_as_file(路径)	截图

```
driver.get_screenshot_as_file("./baidu.jpg")
```

### 单元素的定位

**方式一**

find_element_by_id() 

find_element_by_name() 

find_element_by_class_name() 

find_element_by_tag_name() 

find_element_by_link_text() 

find_element_by_partial_link_text() 

find_element_by_xpath() 

find_element_by_css_selector()

```
driver.find_element_by_xpath('//*[@id="u1"]/a[1]')
```

**方式二**

from selenium.webdriver.common.by import By

find_element(By.方式, "元素")

```
driver.find_element(By.XPATH, '//*[@id="u1"]/a[1]')
```

### 多元素定位

find_elements_by_id() 

find_elements_by_name() 

find_elements_by_class_name() 

find_elements_by_tag_name() 

find_elements_by_link_text() 

find_elements_by_partial_link_text() 

find_elements_by_xpath() 

find_elements_by_css_selector()

 **示例**

```python
#选择页面上所有的tag name 为input的元素 
inputs = driver.find_elements_by_tag_name('input') 
#然后从中过滤出tpye为checkbox的元素，单击勾选 
for input in inputs:     
	if input.get_attribute('type') == 'checkbox':         
		input.click(）
```





### WebDriver API

#### 接口常用方法

clear      清除元素的内容 

send_keys  在元素上模拟按键输入 

click      单击元素 

submit      提交表单 

size      返回元素的尺寸 

text      获取元素的文本 

get_attribute(name)    获得属性值 

is_displayed()      设置该元素是否用户可见/判断元素是否显示在页面

```python
inputy = driver.find_element(By.XPATH, '//*[@id="kw"]')
inputy.clear()  # 清除文本框中内容
inputy.send_keys("selenium")  # 在搜索框中输入“selenium”
inputy.submit()  # 通过submit进行提交搜索操作，相当于回车
```

#### 打印信息（断言的信息)

 title    返回当前页面的标题   

current_url   获取当前加载页面的URL   

text    获取元素的文本信息

capabilities['browserName']

capabilities['browserVersion'] 	打印浏览器version的值

size	获取页面元素的大小

get_attribute('href'))  获取元素属性，例如 class, id, name, text, href, value,size等

```python
url1 = driver.find_element_by_xpath(    '//*[@id="1"]/div[3]/div[2]/a').get_attribute('href')  # 获取豆瓣阅读元素的url链接
```

#### 键盘操作的常用方法

**from selenium.webdriver.common.keys import Keys**

send_keys(Keys.BACK_SPACE) 删除键（BackSpace）   

send_keys(Keys.SPACE)  空格键(Space)   

send_keys(Keys.TAB)  制表键(Tab)   

send_keys(Keys.ESCAPE)  回退键（Esc）   

send_keys(Keys.ENTER) 回车键（Enter）   

send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）   

send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）   

send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）   

send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V)

```
ele = driver.find_element_by_id('kw')
ele.send_keys('python#')
ele.send_keys(Keys.BACK_SPACE)
```

####   鼠标操作的常用方法

**from selenium.webdriver.common.action_chains import ActionChains**

double_click()   双击   

drag_and_drop()  拖动   

move_to_element()  鼠标悬停在一个元素上   

click_and_hold()   按下鼠标左键在一个元素上

click(on_element=None) ——单击鼠标左键

click_and_hold(on_element=None) ——点击鼠标左键，不松开

context_click(on_element=None) ——点击鼠标右键

double_click(on_element=None) ——双击鼠标左键

drag_and_drop(source, target) ——拖拽到某个元素然后松开

drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

key_down(value, element=None) ——按下某个键盘上的键

key_up(value, element=None) ——松开某个键

move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

move_to_element(to_element) ——鼠标移动到某个元素

move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

perform() ——执行链中的所有动作

release(on_element=None) ——在某个元素位置松开鼠标左键

send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素

**示例1**：

```python
#引入ActionChains类 
from selenium.webdriver.common.action_chains import ActionChains 
#定位到要右击的元素 
right =driver.find_element_by_xpath("xx") 
#对定位到的元素执行鼠标右键操作 
ActionChains(driver).context_click(right).perform()
```

**示例**2：

```python
#引入ActionChains类 
from selenium.webdriver.common.action_chains import ActionChains  
#定位元素的原位置 
element = driver.find_element_by_name("xxx") 
#定位元素要移动到的目标位置 
target =  driver.find_element_by_name("xxx") 
#执行元素的移动操作 
ActionChains(driver).drag_and_drop(element,target).perform()
```

####  等待时间

sleep()：      python提供设置固定休眠时间的方法。

implicitly_wait()：  隐式等待， 找不到则依旧执行等待设置时间，找到了立即执行

WebDriverWait()：      显式等待方法，定义等待一定条件发生后再进一步执行代码

**其他**：

presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中

　　until_not(method, message='')
　　调用该方法体提供的回调函数作为一个参数，直到返回值为False
　　until(method, message='')
　　调用该方法体提供的回调函数作为一个参数，直到返回值为True

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
	# 设置显式等待10s
	print(ctime())
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, 'kw'))
	)
	print('我已经找到')
finally:
	print(ctime())
```

#### 多框架处理

switch_to.frame  方法 

#### 多窗口处理

current_window_handle     获得当前窗口句柄 

window_handles   返回的所有窗口的句柄到当前会话 

switch_to_window()       用于处理多窗口之前切换

备注：

**示例**：

```python
 #获得当前窗口 
nowhandle=driver.current_window_handle 
#打开注册新窗口 
driver.find_element_by_name("tj_reg").click() 
#获得所有窗口 
allhandles=driver.window_handles 
#循环判断窗口是否为当前窗口 
for handle in allhandles:     
	if handle != nowhandle:         
		driver.switch_to_window(handle)         
		print 'now register window!'         
		#切换到邮箱注册标签         
		driver.find_element_by_id("mailRegTab").click()         
		driver.close()          
driver.switch_to_window(nowhandle)#回到原先的窗口
```

#### Alert弹框处理

switch_to_alert()     用于获取网页上的警告信息。 

text         返回 alert/confirm/prompt 中的文字信息。 

accept        点击确认按钮。 

dismiss        点击取消按钮，如果有的话。 

send_keys      输入值，这个alert\confirm没有对话框就不能用了，不然会报错

#### 单选框&复选框

```python
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
```

#### 文件上传

driver.find_element_by_xx('xx').send_keys('d:/abc.txt')

**示例**：

```python
#定位上传按钮，添加本地文driver.find_element_by_name("file").send_keys('D:\\selenium_use_case\upload_file.txt')
```

#### 文件下载

确定Content-Type ： 下载文件的类型 

**方法一**： 

curl -I URL | grep "Content-Type" 

**方法二**： 

import requests 

print requests.head(’http://www.python.org’).headers[’content-type’] 

#### 控制浏览器滚动条

**示例**：

```python
#将页面滚动条拖到底部 
js="var q=document.documentElement.scrollTop=10000" 
driver.execute_script(js) 
 
#将滚动条移动到页面的顶部 
js_="var q=document.documentElement.scrollTop=0" 
driver.execute_script(js_) 
```

#### cookie处理

get_cookies()        获得所有cookie信息 

get_cookie(name)        返回特定name 有cookie信息  

add_cookie(cookie_dict)      添加cookie，必须有name 和value 值 

delete_cookie(name)      删除特定(部分)的cookie信息 

delete_all_cookies()      删除所有cookie信息

#### 验证码的解决方法

•  去掉验证码 

•  设置万能码 

•  验证码识别技术 

•  记录cookie 

## 自动化测试基础

### 分类

UI、接口、单元

### 前提条件

•功能成熟（需求变动较小） 

•产品更新维护周期长 

•项目进度不太大 

•比较频繁的回归测试 

•软件开发比较规范，具有可测试性

 •可以脚本具有可复用性 

### 框架类型 

主要分为数据驱动和关键字驱动两类框架

数据驱动框架的结构简单，理论上能实现任何复杂逻辑的测试脚本。因为它是纯脚本的框架，所以脚本
的维护量很大，它适合能力较强、规模小的自动化测试团队。 

关键字驱动框架结构复杂，对于一些复杂的测试逻辑比较难以实现（除非编写专用的函数），它可极大
的减少脚本的维护量，上手容易，适合较大规模的测试团

### 框架组成

用例管理，数据管理，脚本管理，测试结果管理，测试报告管理，Log和截图管理，功能点管理，执行管理

**框架基本组件**

1）配置文件

配置文件去控制一些，环境信息，开关，配置文件可以是txt/xml/yaml/properties/ini，一般.properties使用较多在JAVA里，本文是Python系列，我可能会选择ini文件

2）框架主要代码

主要包含日志类、自定义封装基类、配置文件读取以及各种调度

3）产品业务页面

核心思想：页面对象，业务逻辑分层，分页独立出来

4）测试脚本集合

考虑采用第三方单元测试框架来管理和创建测试单元

5）报告和日志文件输出

一般采用第三方插件来实现这个功能，好多报告格式是html，简单，明了的风格。日志输出也很重要，如果发生报错，脚本执行失败，通过日志快速定位发生问题位置

 6）持续集成

git,svn,ant,maven，jenkins，我们会把这整合到jenkins，达到持续集成，一键执行测试脚本

**样式**

![](C:\Users\Ecidi\Desktop\2.png)

### 层次

手工测试用例转换成自动化测试脚本的过程

能设计自动化测试框架，至少能够维护自动化测试框架。

流程自动化方案设计，例如，一键打包，自动开始测试，自动发送测试报告，自动运维部署上线等

### 读取配置文件内容

**配置文件**

[browserType]

browserName = Chrome

[testServer]

URL = https://www.baidu.com

**读取**

```python
    import ConfigParser
    import os

    root_dir = os.path.dirname(os.path.abspath('.')) # 获取项目根目录的相对路径

    config = ConfigParser.ConfigParser()
    file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    config.read(file_path)

    browser = config.get("browserType", "browserName")
    url = config.get("testServer", "URL")

```

### 系统时间和格式化时间



time.time()获取的是从1970年到现在的间隔，单位是秒

time.strftime('%Y-%m-%d%H:%M:%S', time.localtime()) # 格式化时间，按照 2017-04-15 13:46:32的格式打印

### 类

类的定义，class开头的就表示这是一个类，小括号里面的，表示这个类的父类，涉及到继承，默认object是所有类的父类。python中定义类，小括号内主要有三种：1. 具体一个父类，2. object 3. 空白

函数或方法的定义， def开头就表示定义一个函数，方法包括，实例方法，类方法，静态方法，注意看类方法和静态方法定义的时候上面有一个@标记。

包中模块必须有类，才可以调用
from 包.模块(.py) import 类

**类继承**

def classA(父类)：

### 封装Log类

```python
    # _*_ coding: utf-8 _*_
    import logging
    import os.path
    import time
     
     
    class Logger(object):
     
        def __init__(self, logger):
            # 创建一个logger
            self.logger = logging.getLogger(logger)
            self.logger.setLevel(logging.DEBUG)
     
            # 创建一个handler，用于写入日志文件
            rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            log_path = os.path.dirname(os.getcwd()) + '/Logs/'
            log_name = log_path + rq + '.log'  
            fh = logging.FileHandler(log_name)
            fh.setLevel(logging.INFO)
     
            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
     
            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
     
            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
     
        def getlog(self):
            return self.logger

```

**测试类**

```python
    import time
    from selenium import webdriver
    from test.logger import Logger
     
     
    mylogger = Logger(logger='TestMyLog').getlog()
    class TestMyLog(object):
     
        def print_log(self):
            driver = webdriver.Chrome()
            mylogger.info("打开浏览器")
     
    testlog = TestMyLog()
    testlog.print_log()

```

### BasePage类

常用的几个Selenium方法封装到BasePage这个类

## unitest单元测试框架

### 组件基本概念

**1.测试固件（test fixture）**

包括两部分，执行测试代码之前的准备部分和测试结束之后的清扫代码

这两部分一般用函数setUp()和tearDown()表示

**2.测试用例（test case）**

unittest中管理的最小单元是测试用例，

一个测试用例，包括测试固件，和具体测试业务的函数或者方法。

一个测试用例中，测试固件可以不写，但是至少有一个已test开头的函数，nittest会自动化识别test开头的函数是测试代码，所有的测试函数都要test开头，记住是小写的哦

**3.测试套件 （test suite）**

多测试用例的集合，叫测试套件

**4.测试执行器 （test runner）**

一个用来执行加载测试用例，并执行用例，且提供测试输出的一个组建。test runner可以加载test case或者test suite进行执行测试任务

### 测试用例格式

```python
    import unittest
 
     
    class 类名(unittest.TestCase):
     
        def setUp(self):
        def tearDown(self):
        def test_方法名(self):
     
    if __name__ == '__main__':
        unittest.main()

```

### POM（Page Object Model）



**思想**

把页面元素和业务逻辑和测试脚本分离出来到两个不同类文件。ClassA只写页面元素定位，和业务逻辑代码操作的封装，ClassB只写测试脚本，不关心如何元素定位，只写调用ClassA的代码去覆盖不同的测试场景，如果前端页面发生变化，只需要修改ClassA的元素定位，而不需要去修改ClassB中的测试脚本代码

**优点**

业务代码和测试脚本分离

每一个页面对应一个页面类，页面的元素写到这个页面类中

页面类主要包括该页面的元素定位，和和这些元素相关的业务操作代码封装的方法

代码复用，从而减少测试脚本代码量



### 脚本执行方法

#### addTest

说明：addTest()方法来加载一个测试用例到测试套件中去

流程：先初始化一个suite实例，然后这个实例有一个addTest()的方法，可以加载不同类里面的不同测试函数

格式：addTest(测试类的类名（‘测试函数名称，就是test开头的函数’）)

限制：不适数量较大用例

**示例**：

```python
    import unittest
    import testsuites
    from testsuites.test_baidu_search import BaiduSearch
     
     
    suite = unittest.TestSuite()
    suite.addTest(BaiduSearch('test_baidu_search'))
     
    if __name__=='__main__':
        #执行用例
        runner=unittest.TextTestRunner()
        runner.run(suite)
```



#### makeSuite()

说明：makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去

**示例**：

```python
    import unittest
    import testsuites
    from testsuites.test_baidu_search import BaiduSearch   
     
    suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
     
    if __name__=='__main__':
        #执行用例
        runner=unittest.TextTestRunner()
        runner.run(suite)

```

#### **discover**

说明：discover（）方法去加载一个路径下所有的测试用例

**示例**：

```python
    import unittest
   
    suite = unittest.TestLoader().discover("testsuites")
    
    if __name__=='__main__':
        #执行用例
        runner=unittest.TextTestRunner()
        runner.run(suite)

```

### 自动化测试报告

**示例**：

```python
import HTMLTestRunner
import os
import unittest
import time


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")

# 构建suite
suite = unittest.TestLoader().discover("testsuites")

if __name__ =='__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)

```









