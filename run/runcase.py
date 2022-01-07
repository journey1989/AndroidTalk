import pytest, os,sys
from tools.tool import REPORT_PATH, TESTCASE_PATH

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")

if __name__ == '__main__':

    for i in os.listdir(TESTCASE_PATH):
        if i.startswith('A') == True:
            pytest.main(["-v", "-s", f"%s{i}" % TESTCASE_PATH, "--alluredir=%s" % REPORT_PATH])
    os.system('allure serve %s'%REPORT_PATH)
