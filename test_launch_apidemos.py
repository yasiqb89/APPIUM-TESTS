from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def test_launch_apidemos():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "16"  # Match your emulator version
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"
    options.app_package = "io.appium.android.apis"
    options.app_activity = "io.appium.android.apis.ApiDemos"
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)
    time.sleep(5)
    driver.quit()