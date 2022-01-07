import os.path,sys
import nnlog

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
sys.path.append(BASE_PATH)
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")

REPORT_PATH = os.path.join(BASE_PATH, 'allure_report')
print(REPORT_PATH)

SCREENSHOT_PATH = os.path.join(BASE_PATH, 'screenshots/')
print(SCREENSHOT_PATH)

TESTCASE_PATH = os.path.join(BASE_PATH, 'testcase/')

LOG_PATH = os.path.join(BASE_PATH, 'log')
print(LOG_PATH)

logname = os.path.join(LOG_PATH, 'log.txt')

log = nnlog.Logger(file_name=logname,level='debug', when='D')

