from airtest.core.api import *
import pytest, allure, os
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from tools.tool import REPORT_PATH
from commom.com import getScreenshots
from fabulous.color import *
from faker import Faker

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
f = Faker(locale='zh_cn')


@allure.feature('回归测试：预告模块')
class TestNotice(object):

    def setup_class(self):
        pass
        # sleep(3)
        # start_app('com.dubmic.talk')
        # print(green('启动开谈'.center(100, '*')))

    @allure.title('进入预告并关注预告')
    def test_01(self):
        notice = poco('com.dubmic.talk:id/top_icon_widget_1')
        nc = poco.wait_for_any([notice], timeout=100)
        nc.click()
        if poco('com.dubmic.talk:id/notice_detail_follow_status_bt').exists():
            poco('com.dubmic.talk:id/notice_detail_follow_status_bt')[0].click()
            poco('com.dubmic.talk:id/follow_all_user_bt').click()
            poco('com.dubmic.talk:id/ok_bt').click()
        else:
            print('未有预告')
        getScreenshots('关注预告')

    @allure.title('进入预告点击推荐和我的')
    def test_02(self):
        poco(text='推荐').click()
        sleep(2)
        poco(text='我的').click()

    @allure.title('创建预告')
    def test_03(self):
        poco('com.dubmic.talk:id/add_notice_bt').click()
        poco('com.dubmic.talk:id/edit_view').set_text(f.sentence())
        poco('com.dubmic.talk:id/edit_view_ms').set_text(f.paragraph())
        poco('com.dubmic.talk:id/sub_btn_over').click()
        sleep(2)
        getScreenshots('创建预告')

    @allure.title('删除预告')
    def test_04(self):
        poco('com.dubmic.talk:id/notice_detail_edit_tv').click()
        poco('com.dubmic.talk:id/btn_remove_notice').click()
        poco('com.dubmic.talk:id/follow_all_user_bt').click()
        keyevent('back')

    def teardown_class(self):
        # os.system("adb shell am force-stop com.dubmic.talk")
        # print(green('杀掉开谈进程'.center(100, '*')))
        pass