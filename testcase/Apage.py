from airtest.core.api import *
import pytest, allure, os, random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from tools.tool import REPORT_PATH, log
from commom.com import getScreenshots, upSwipe
from faker import Faker


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
f = Faker(locale='zh_cn')


@allure.feature('回归测试：首页')
class TestMy(object):

    def setup_class(self):
        # sleep(3)
        # start_app('com.dubmic.talk')
        # print(green('启动开谈'.center(100, '*')))
        pass

    @allure.title('首页广告')
    def test_01(self):
        if poco("androidx.recyclerview.widget.RecyclerView").exists():
            poco("androidx.recyclerview.widget.RecyclerView").click()
            upSwipe()
            sleep(1)
            keyevent('back')

    @allure.title('首页进入房间')
    def test_02(self):
        if poco('com.dubmic.talk:id/iv_cover').exists():
            poco('com.dubmic.talk:id/iv_cover')[random.randint(0, 2)].click()
            poco('com.dubmic.talk:id/btn_leave').click()
        else:
            print('无房间')


    @allure.title('创建房间需要实名认证')
    def test_03(self):
        poco(text='创建房间').click()
        poco('com.dubmic.talk:id/btn_create_room').click()
        if poco('com.dubmic.talk:id/btn_ok').exists():
            poco('com.dubmic.talk:id/btn_ok').click()
            poco('com.dubmic.talk:id/edit_query').set_text(f.name())
            poco('com.dubmic.talk:id/edit_code').set_text(f.ssn())
            poco('com.dubmic.talk:id/btn_ok').click()
            sleep(1)
            getScreenshots('实名认证')
            poco('com.dubmic.talk:id/abfl_widget_tb_close').click()
            poco('com.dubmic.talk:id/abfl_dialog_positive_btn').click()
            keyevent('back')
            keyevent('back')

    @allure.title('创建私密房间')
    def test_04(self):
        poco(text='创建房间').click()
        poco(text='私密房间').click()
        with allure.step('添加房间标题'):
            poco('com.dubmic.talk:id/etTopic').set_text(f.sentence())
        with allure.step('点击创建房间'):
            poco('com.dubmic.talk:id/btn_create_room').click()
        with allure.step('点击邀请'):
            poco('com.dubmic.talk:id/iv_assist').click()
        sleep(1)
        a = poco('com.dubmic.talk:id/btnInvite').get_text()
        assert ('邀请好友' == a)
        getScreenshots('邀请好友上麦')
        keyevent('back')
        bp = poco('com.dubmic.talk:id/btn_permissions')
        bpc = poco.wait_for_any([bp], timeout=100)
        bpc.click()  # 点击私密房间右上角提醒按钮
        btn = poco('com.dubmic.talk:id/btn')
        btnc = poco.wait_for_any([btn], timeout=100)
        btnc.click()
        sleep(3)
        b = poco('com.dubmic.talk:id/tv_name').get_name()
        assert ('com.dubmic.talk:id/tv_name' == b)
        poco('com.dubmic.talk:id/btnViewRules').click()
        sleep(1)
        c = poco('com.dubmic.talk:id/btn_ok').get_text()
        assert ('我知道了' == c)
        poco('com.dubmic.talk:id/btn_ok').click()
        keyevent('back')
        poco('com.dubmic.talk:id/btn_say_text').click()
        poco('com.dubmic.talk:id/edit_input').set_text(f.sentence())  # 发布评论
        poco('com.dubmic.talk:id/btn_ok').click()
        poco('com.dubmic.talk:id/btn_room_mike').click()  # 禁麦
        poco('com.dubmic.talk:id/btn_room_free_gifts').click()  # 给自己送花
        poco('com.dubmic.talk:id/btn_room_give_gift_dialog').click()  # 打开送礼面板
        keyevent('back')
        poco('com.dubmic.talk:id/btn_more').click()
        poco('com.dubmic.talk:id/btn_close_room').click()  # 关闭房间
        poco('com.dubmic.talk:id/btn_ok').click()  # 关闭房间
        poco('com.dubmic.talk:id/ivClose').click()  # 关闭结束弹窗
        poco(text='创建房间').click()
        poco(text='私密房间').click()
        with allure.step('添加房间标题'):
            poco('com.dubmic.talk:id/etTopic').set_text(f.sentence())
        with allure.step('点击创建房间'):
            poco('com.dubmic.talk:id/btn_create_room').click()
        poco('com.dubmic.talk:id/btn_leave').click()  # 关闭房间
        poco('com.dubmic.talk:id/btn_close').click()
        if poco('com.dubmic.talk:id/ivClose').exists():
            poco('com.dubmic.talk:id/ivClose').click()
        else:
            log.error('有bug，房间结束弹窗没有出来')

    def teardown_class(self):
        # os.system("adb shell am force-stop com.dubmic.talk")
        # print(green('杀掉开谈进程'.center(100, '*')))
        pass

