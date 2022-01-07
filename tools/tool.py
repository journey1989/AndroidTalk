import os.path
import nnlog

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)

REPORT_PATH = os.path.join(BASE_PATH, 'allure_report')
print(REPORT_PATH)

SCREENSHOT_PATH = os.path.join(BASE_PATH, 'screenshots/')
print(SCREENSHOT_PATH)

TESTCASE_PATH = os.path.join(BASE_PATH, 'testcase/')

LOG_PATH = os.path.join(BASE_PATH, 'log')
print(LOG_PATH)

logname = os.path.join(LOG_PATH, 'log.txt')

log = nnlog.Logger(file_name=logname,level='debug', when='D')
