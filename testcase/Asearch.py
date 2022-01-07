from airtest.core.api import *
import pytest, allure, os
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from tools.tool import REPORT_PATH, log
from commom.com import getScreenshots, leftSwipe
from fabulous.color import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


@allure.feature('回归测试：搜索模块')
class TestSearch(object):

    def setup_class(self):
        # sleep(3)
        # start_app('com.dubmic.talk')
        # print(green('启动开谈'.center(80, '=')))
        # sleep(2)
        pass

    @allure.title('点击搜索栏，进入搜索界面')
    @allure.description('搜索界面')
    def test_01(self):

        search = poco('com.dubmic.talk:id/search_bt')
        sc = poco.wait_for_any([search], timeout=100)
        sc.click()
        sleep(2)
        getScreenshots('进入搜索界面')

    @allure.title('搜索界面:点击关注，再取消关注')
    def test_02(self):
        sleep(2)
        if poco('com.dubmic.talk:id/user_contract_bt').exists():
            poco('com.dubmic.talk:id/user_contract_bt')[0].click()
            sleep(2)
            poco('com.dubmic.talk:id/user_contract_bt')[0].click()
        else:
            log.debug('数据异常' + 'test_02')

    @allure.title('搜索界面左滑12次')
    def test_03(self):
        for i in range(12):
            sleep(1)
            leftSwipe()

    @allure.title('通过搜索界面进入用户主页')
    def test_04(self):
        userdisplay = poco('com.dubmic.talk:id/user_display_name_tv')[0]
        uc = poco.wait_for_any([userdisplay], timeout=100)
        uc.click()
        sleep(1)
        getScreenshots('用户个人主页')
        keyevent("BACK")

    @allure.title('搜索已存在的用户主页')
    def test_05(self):
        searchuser = poco('com.dubmic.talk:id/search_tv')
        uc = poco.wait_for_any([searchuser], timeout=100)
        uc.click()
        text('123', search=True)
        sleep(2)
        getScreenshots('搜索结果：已存在的用户')
        poco('com.dubmic.talk:id/search_edit_clear').click()
        poco('com.dubmic.talk:id/search_edit').click()
        text('标高452452', search=True)
        sleep(2)
        getScreenshots('搜索结果：不存在的用户')
        poco(text='取消').click()
        keyevent('back')

    def teardown(self):
        pass

    def teardown_class(self):
        # os.system("adb shell am force-stop com.dubmic.talk")
        # print(green('杀掉开谈进程'.center(80, '=')))
        pass

# if __name__ == '__main__':
#
#     # pytest.main(["-s", "-v", 'Asearch.py', "--alluredir=%s"%REPORT_PATH])
#     pytest.main(["-s", "-v", 'Asearch.py', "--alluredir=%s"%REPORT_PATH, "-m webtest"])
#     # os.popen('cd %s && allure generate --clean %s' % (REPORT_PATH, REPORT_PATH))
