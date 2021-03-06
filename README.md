## 打造自己的UI自动化框架

## 目录结构
+   lib/driver 
+       chrome-driver/fire-driver
+   utils/Initial_check.py 
+       检测操作系统 windows/linux
+   utils/logger.py
+       生成日志
+   Locators 测试页面定位
+      Locators/LoginLocators 登录模块的页面对象定位
+      - Locators/LoginLocators/login_locators.py
+      Locators/UserLacators 用户模块的页面对象定位
+      - Locators/UserLacators/user_locators.py
+   PageObjects 业务流程
+       IndexPage 主页模块的页面对象
        - index_page.py
        LoginPage 登录模块的页面对象
        - login_page.py
        UserPage 用户模块的页面对象
+   OutPuts/logs
+       日志文件
+   Page/Plugs/browserEngine 封装浏览器引擎
    ```python
    from Page.Plugs.BrowserEngine import BrowserEngine
    class Test():

        @classmethod
        def setUpClass(cls):
            # 加载浏览器引擎
            browser = BrowserEngine(cls)
            driver = browser.getBrowser()
    ```
    
+   Page/Plugs/basePage 封装基类
+   TestDatas 测试数据
+       GobalDatas 全局的测试数据
+       - gobal_datas.py
+       LoginDatas 登录模块的有效、无效、异常测试数据
+       - login_datas.py
+       UserDatas 用户模块的正常、异常的测试数据
+       - user_add_datas.py

## allure 测试报告
### 执行命令
```python
# pytest -vs --alluredir ./OutPuts/report/result --clean-alluredir # 生成原始文件，不能打开html报告

# allure serve ./OutPuts/report/allure-report # 打开html的报告需要启动allure服务

# --clean  # --clean 清除上一次的测试报告
# allure generate ./OutPuts/report/result -o ./OutPuts/report/allure-report -c


# allure open ./OutPuts/report/allure-report --host 192.168.0.104 --port 8800  # 打开报告

# allure open ./OutPuts/report/allure-report --port 8800

```
### @allure.step 标注操作步骤，比如 注册、登录、退出
+   用法

```python

import allure
@allure.step
def step1_register():
    pass

@allure.step
def step2_login():
    pass

# step 可以添加描述信息，支持使用位置参数、关键字参数占位符。也可以捕获关键字参数的默认值
@allure.step('Step with pay in the title, orderid: "{0}", fee: "{fee}"')
def step3_pay(orderid, fee=0):
    pass

def test_with_imported_step():
    step2_login()
    step3_pay("20200916001", 9)



```


## 参考文献
https://www.cnblogs.com/yudx/p/11413990.html
https://www.jianshu.com/p/82fdd2db9c44
https://www.cnblogs.com/mariahcat/p/9277082.html
https://www.jianshu.com/p/0fc9fc5f42e9
https://github.com/lewyuejian/yun_car900/blob/master/utils/common/WebDriver.py


https://www.cnblogs.com/ff-gaofeng/p/12090688.html
https://www.cnblogs.com/kgtest/p/12669480.html
https://zhuanlan.zhihu.com/p/79780757
https://www.freesion.com/article/7349195471/

参考项目 https://github.com/a2442559/python_web_framework/blob/master/Common/plugs/basepage.py
https://www.cnblogs.com/ronyjay/p/12979590.html
https://github.com/HandsomeBoy1221/UI_Frame

## 智能轮询元素是否显示
https://www.cnblogs.com/yhleng/p/9295188.html
## 改造
https://testerhome.com/articles/17472
https://www.cnblogs.com/ff-gaofeng/p/12090688.html
https://www.cnblogs.com/wuzhiming/p/11657091.html
https://testerhome.com/topics/7662?order_by=like&

+       1、回放录制 - 装饰器
+       2、添加超时器 - 装饰器
+       3、截图 - 改装装饰器

## 问题及解决
https://www.jianshu.com/p/b8f5a454f8d9

## 装饰器原理
https://blog.csdn.net/u010358168/article/details/77773199

## 日志
https://www.cnblogs.com/yyds/p/6897964.html

## pytest + allure 详细文档
https://blog.csdn.net/qq_42610167/article/details/101204066?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight