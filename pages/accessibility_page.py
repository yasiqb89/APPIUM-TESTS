from appium.webdriver.common.appiumby import AppiumBy

class AccessibilityPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators 
    ACCESSIBILITY_MENU = (AppiumBy.ACCESSIBILITY_ID, "Accessibility")
    NODE_PROVIDER = (AppiumBy.ACCESSIBILITY_ID, "Accessibility Node Provider")
    TEXT_VIEW_ELEMENT = (AppiumBy.CLASS_NAME, "android.widget.TextView")

    # Actions
    def tap_accessibility_menu(self):
        self.driver.find_element(*self.ACCESSIBILITY_MENU).click()

    def tap_node_provider(self):
        self.driver.find_element(*self.NODE_PROVIDER).click()

    def get_all_text_views(self):
        return self.driver.find_elements(*self.TEXT_VIEW_ELEMENT)