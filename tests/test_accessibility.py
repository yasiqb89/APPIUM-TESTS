from pages.accessibility_page import AccessibilityPage
from appium.webdriver.common.appiumby import AppiumBy

def test_open_accessibility_node_provide(driver):
    page = AccessibilityPage(driver)
    page.tap_accessibility_menu()
    page.tap_node_provider()

    assert "Enable TalkBack" in driver.page_source

def test_node_provider_text(driver):
    page = AccessibilityPage(driver)
    page.tap_accessibility_menu()
    page.tap_node_provider()

    text_elements = page.get_all_text_views()
    all_text = [el.text for el in text_elements]
    print("Text elements found:", all_text)

    assert any("Node" in text for text in all_text)
