import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_demo:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    # 后置处理：收尾
    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("value",["Selenium","Appium","面试"])
    def test_work1(self, value):
        # 打开论坛
        self.driver.get("https://ceshiren.com/")
        # 隐式等待
        self.driver.implicitly_wait(4)
        # 定位高级搜索按钮并点击
        self.driver.find_element(By.ID, "search-button").click()
        # 点击跳转高级搜索页面
        self.driver.find_element(By.CSS_SELECTOR, "[title='打开高级搜索']").click()
        # 定位高级页面的搜索框
        search_edit = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='搜索']")
        # 输入搜索关键字
        search_edit.send_keys(value)
        # 定位搜索按钮
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".search-cta")
        # 点击搜索按钮
        search_button.click()
        # 定位第一条搜索结果的标题
        text = self.driver.find_element(By.CSS_SELECTOR,".topic-title").text
        # 断言
        assert value.lower() in text.lower()