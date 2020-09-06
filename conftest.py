import pytest
import time
import os
import pdfkit
from appium import webdriver
from utilities.proxy import hmaone

dir_path = os.path.dirname(os.path.realpath(__file__))
Log_path = os.path.join(dir_path, "Logfeature")

os.system("appium -a 127.0.0.1 -p 4723")
time.sleep(4)


def pytest_html_report_title(report):
    report.title = "Amazon App Sanity Report"


def pdfreport():
    pdfkit.from_file('/Users/harshalwarkar/PycharmProjects/AmazonProject/Report/report.html', '/Users/harshalwarkar/PycharmProjects/AmazonProject/Report/report.pdf')


def pytest_addoption(parser):
    parser.addoption("--region_name", action="store", default="India")
    parser.addoption("--env", action="store", default="Production")


@pytest.fixture(scope="class")
def setupone(request):
    region = request.config.getoption("region_name")
    env = request.config.getoption("env")
    hmaone(region)

    if env == "Production":
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                  desired_capabilities={'platformName': 'Android', 'platformVersion': '9',
                                                        'deviceName': 'ZF6223G5T8', 'automationName': 'UiAutomator2',
                                                        'noReset': 'false', 'appActivity': 'com.amazon.mShop.splashscreen.StartupActivity',
                                                        'appPackage': 'com.amazon.mShop.android.shopping', 'app': '/Users/harshalwarkar/Downloads/Amazon_shopping.apk'})
        time.sleep(4)
        request.cls.driver = driver
        yield
        driver.quit()
        pdfreport()

