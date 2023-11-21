import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("value,expectation",
                         [("Selenium", ""),
                          ("Appium", ""),
                          ("面试", "")])
def test_work1(value, expectation):
    driver = webdriver.Chrome()
    # 打开论坛
    driver.get("https://ceshiren.com/")
    # 隐式等待
    driver.implicitly_wait(4)
    # 定位高级搜索按钮
    driver.find_element(By.ID, "search-button")
    # 点击跳转高级搜索页面
    driver.find_element(By.LINK_TEXT, "/search?expanded=true")
    # 定位高级页面的搜索框
    search_edit = driver.find_element(By.CSS_SELECTOR, "")
    # 输入搜索关键字
    search_edit.send_keys(value)
    # 定位搜索按钮
    search_button = driver.find_element(By.CSS_SELECTOR, "")
    # 点击搜索按钮
    search_button.click()
    # 定位第一条搜索结果的标题
    pass
    # 断言
    assert