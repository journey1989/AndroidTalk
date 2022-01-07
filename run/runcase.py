import pytest, os
from tools.tool import REPORT_PATH, TESTCASE_PATH

if __name__ == '__main__':

    for i in os.listdir(TESTCASE_PATH):
        if i.startswith('A') == True:
            pytest.main(["-v", "-s", f"%s{i}" % TESTCASE_PATH, "--alluredir=%s" % REPORT_PATH])
    os.system('allure serve %s'%REPORT_PATH)
