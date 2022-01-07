from airtest.core.api import *
import pytest, allure, random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from tools.tool import REPORT_PATH
from commom.com import getScreenshots, rightSwipe, downSwipe
from fabulous.color import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


@allure.feature('回归测试: 排行榜')
class TestRank(object):

    def setup_class(self):
        # sleep(3)
        # start_app('com.dubmic.talk')
        # print(green('启动开谈'.center(100, '*')))
        pass


    @allure.title('从首页进入排行榜并向右滑动，查看榜单数据')
    def test_01(self):
        poco('com.dubmic.talk:id/top_icon_widget_0').click()
        if poco('com.dubmic.talk:id/tv_tab_hot').exists():
            for i in range(2):
                rightSwipe()
                sleep(2)
                getScreenshots('人气榜单%d' % i)  # 0 周   1月
        else:
            print('数据异常' + 'test_01')
        poco(text='主播榜').click()
        for i in range(2):
            rightSwipe()
            sleep(2)
            getScreenshots('主播榜单%d' % i)
        poco(text='守护榜').click()
        for i in range(2):
            rightSwipe()
            sleep(2)
            getScreenshots('守护榜单%d' % i)

    @allure.title('排行榜：关注or已关注、查看规则')
    def test_02(self):
        poco('com.dubmic.talk:id/tvRelation').click()
        sleep(2)
        poco('com.dubmic.talk:id/tvRelation').click()
        sleep(2)
        poco('com.dubmic.talk:id/btnRule').click()
        getScreenshots('排行榜规则')
        poco(text='我知道了').click()

    @allure.title('排行榜：如果有人在直播，点击头像进入直播间，没有进入个人主页')
    def test_03(self):
        poco(text='人气榜').click()
        downSwipe()
        sleep(2)
        if poco('com.dubmic.talk:id/liveLoading').exists():
            poco('com.dubmic.talk:id/liveLoading').click()
            sleep(2)
            getScreenshots('从排行榜进入直播间')
            poco('com.dubmic.talk:id/btn_leave').click()
        else:
            print('没有人在直播')
            keyevent('back')


    @allure.title('排行榜：如果有人在直播，点击头像进入直播间，没有进入个人主页')
    def test_04(self):
        top = poco('com.dubmic.talk:id/top_icon_widget_0')
        tc = poco.wait_for_any([top], timeout=100)
        tc.click()
        poco(text='守护榜').click()
        if poco('com.dubmic.talk:id/liveLoading').exists():
            print('有人在直播')
            keyevent('back')
        else:
            poco('com.dubmic.talk:id/ivAvatar')[random.randint(0,4)].click()
            keyevent("back")
            keyevent('back')


    def teardown_class(self):
        # os.system("adb shell am force-stop com.dubmic.talk")
        # print(green('杀掉开谈进程'.center(100, '*')))
        pass