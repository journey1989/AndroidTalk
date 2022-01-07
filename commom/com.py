from airtest.core.api import *
from tools.tool import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

def getScreenshots(snapshotname):
    nowtime = time.strftime('%Y%m%d %H%M%S')
    return snapshot(filename=f'%s' % SCREENSHOT_PATH + nowtime + snapshotname + '.jpg', msg=snapshotname)



def leftSwipe():
    d,h = poco.get_screen_size()
    start_dp = (d/2,h/2)
    end_dp = (d/1080,h/2)
    swipe(start_dp, end_dp, duration=0.1)


def rightSwipe():
    d,h = poco.get_screen_size()
    start_dp = (d/2,h/2)
    end_dp = (d/10,h/2)
    swipe(start_dp, end_dp, duration=0.1)


def downSwipe():
    d,h = poco.get_screen_size()
    start_dp = (d/2,h/2)
    end_dp = (d/2,h/1)
    swipe(start_dp, end_dp, duration=0.1)

def upSwipe():
    d, h = poco.get_screen_size()
    start_dp = (d / 2, h / 2)
    end_dp = (d / 2, h / 20)
    swipe(start_dp, end_dp, duration=0.1)




