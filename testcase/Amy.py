from airtest.core.api import *
import pytest,allure,os,random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from tools.tool import REPORT_PATH,log
from commom.com import getScreenshots,upSwipe
from faker import Faker
from fabulous.color import *
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
f = Faker(locale='zh_cn')


@allure.feature('回归测试：我的')
class TestMy(object):

    def setup_class(self):
        # sleep(3)
        # start_app('com.dubmic.talk')
        # print(green('启动开谈'.center(100, '*')))
        pass

    @allure.severity("normal")
    @allure.title('进入用户个人主页修改昵称和开谈号')
    def test_01(self):
        poco('com.dubmic.talk:id/iv_avatar').click()
        poco('com.dubmic.talk:id/txt_name').click()
        poco('com.dubmic.talk:id/txt_change_user_name').click()
        poco('com.dubmic.talk:id/edit_body').set_text(f.name())
        poco('com.dubmic.talk:id/btn_next').click()
        poco('com.dubmic.talk:id/txt_name').click()
        poco('com.dubmic.talk:id/txt_change_user_nickname').click()
        poco('com.dubmic.talk:id/edit_body').set_text(f.random_number(digits=15))
        poco('com.dubmic.talk:id/btn_next').click()
        sleep(2)
        getScreenshots('修改昵称和开谈号')

    @allure.severity("normal")
    @allure.title('查看关注和粉丝，并拉黑和举报用户')
    def test_02(self):
        poco('com.dubmic.talk:id/txt_attention_num').click()     #关注按钮
        if poco('com.dubmic.talk:id/user_display_name_tv').exists():
            poco('com.dubmic.talk:id/user_display_name_tv')[random.randint(0,3)].click()
            poco('com.dubmic.talk:id/iv_setting').click()
            if poco(text='已拉黑').exists():
                print('用户已被拉黑')
            else:
                poco('com.dubmic.talk:id/txt_set_black').click()
                poco('com.dubmic.talk:id/btn_ok').click()
            setting = poco('com.dubmic.talk:id/iv_setting')
            sc = poco.wait_for_any([setting],timeout=100)
            sc.click()
            poco('com.dubmic.talk:id/txt_set_report').click()
            poco('com.dubmic.talk:id/et_content').set_text(f.paragraph())
            poco('com.dubmic.talk:id/btn_save').click()
            poco('com.dubmic.talk:id/others_set_info_cb').click()   #更多推荐
            sleep(2)
            getScreenshots('更多推荐')
            keyevent("back")
            keyevent("back")

        else:
            print('没有关注的用户')
        poco('com.dubmic.talk:id/txt_fans_num').click()    #粉丝按钮
        keyevent("back")

    @allure.severity("critical")
    @allure.title('钱包、实名认证')
    def test_03(self):
        poco('com.dubmic.talk:id/tv_wallet').click()    #钱包
        poco('com.dubmic.talk:id/tv_bill').click()     #账单
        keyevent("back")
        poco('com.dubmic.talk:id/tv_recharge').click()
        keyevent("back")
        poco('com.dubmic.talk:id/tv_exchange').click()
        keyevent("back")
        poco('com.dubmic.talk:id/withdraw_layout').click()
        if poco('com.dubmic.talk:id/btn_verify').exists():
            poco('com.dubmic.talk:id/btn_verify').click()
            poco('com.dubmic.talk:id/edit_query').set_text(f.name())
            poco('com.dubmic.talk:id/edit_code').set_text(f.ssn())
            poco('com.dubmic.talk:id/btn_ok').click()
            sleep(1)
            getScreenshots('实名认证')
            poco('com.dubmic.talk:id/abfl_widget_tb_close').click()
            poco('com.dubmic.talk:id/abfl_dialog_positive_btn').click()
            keyevent("back")
            keyevent("back")
        else:
            print('已实名认证')

    @allure.severity("trivial")
    @allure.title('装扮')
    def test_04(self):
        poco('com.dubmic.talk:id/tv_decorate').click()
        sleep(1)
        getScreenshots('头像框')
        poco(text='对话框').click()
        sleep(1)
        getScreenshots('对话框')
        keyevent('back')

    @allure.severity("critical")
    @allure.title('设置')
    def test_05(self):
        poco('com.dubmic.talk:id/iv_setting').click()
        poco(text='兴趣管理').click()
        text = ['情感','pia戏','FM电台','cos','游戏','星座占卜','脱口秀','群聊派对','交友','二次元','点唱','处CP']
        poco(text=random.choice(text)).click()
        poco('com.dubmic.talk:id/txt_jump').click()
        sleep(1)
        getScreenshots('兴趣管理')
        poco(text='黑名单管理').click()
        if poco('com.dubmic.talk:id/user_contract_bt').exists():
            poco('com.dubmic.talk:id/user_contract_bt').click()
            keyevent('back')
        else:
             keyevent('back')

        if poco(text='未认证').exists():
            poco(text='未认证').click()
            poco('com.dubmic.talk:id/edit_query').set_text(f.name())
            poco('com.dubmic.talk:id/edit_code').set_text(f.ssn())
            poco('com.dubmic.talk:id/btn_ok').click()
            sleep(1)
            getScreenshots('实名认证')
            poco('com.dubmic.talk:id/abfl_widget_tb_close').click()
            poco('com.dubmic.talk:id/abfl_dialog_positive_btn').click()
            keyevent("back")
        if poco(text='未绑定').exists():
            poco(text='未绑定').click()
            wb = poco('com.sina.weibo:id/new_bnLogin')
            wbc = poco.wait_for_any([wb], timeout=100)
            wbc.click()
            sleep(1)
            getScreenshots('绑定微博')
            poco(text='已绑定').click()

    @allure.severity("minor")
    @allure.title('关于我们，意见反馈、提交反馈、用户协议、隐私协议')
    def test_06(self):
        upSwipe()
        poco(text='关于我们').click()
        keyevent('back')
        poco(text='意见反馈').click()
        poco('com.dubmic.talk:id/et_content').set_text(f.paragraph())
        poco('com.dubmic.talk:id/et_contact').set_text(f.phone_number())
        keyevent('back')
        poco('com.dubmic.talk:id/btn_save').click()
        getScreenshots('提交反馈')
        poco(text='用户协议').click()
        keyevent('back')
        poco(text='隐私协议').click()
        keyevent('back')

    @allure.severity("normal")
    @allure.title('绑定微博')
    def test_07(self):
        keyevent('back')
        if poco(text='绑定微博').exists():
            poco(text='绑定微博').click()
            wb = poco('com.sina.weibo:id/new_bnLogin')
            wbc = poco.wait_for_any([wb], timeout=100)
            wbc.click()
            sleep(1)
            getScreenshots('绑定微博')
        else:
            print('已绑定微博')

    @allure.severity("minor")
    @allure.title('添加or编辑个人简介')
    def test_08(self):
        poco('com.dubmic.talk:id/txt_hit_edit').click()
        poco('com.dubmic.talk:id/edit_view').set_text(f.text())
        poco('com.dubmic.talk:id/sub_btn_over').click()
        keyevent('back')

    def teardown_class(self):
        # os.system("adb shell am force-stop com.dubmic.talk")
        # print(green('杀掉开谈进程'.center(100, '*')))
        pass

