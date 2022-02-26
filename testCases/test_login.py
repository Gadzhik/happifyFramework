import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    # Используем класс из readProperty.py
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    # Вызываем метод loggen из класса LogGen
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        # Добавляе логгирование
        self.logger.info("*********** Test_001_Login **********")
        self.logger.info("*********** Verifying Home Page Title **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        before_login_title = self.driver.title
        if before_login_title == "Happify: Science-Based Activities and Games":
            assert True
            self.driver.close()
            self.logger.info("*********** Home page title test is passed **********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home page title test is failed **********")
            assert False

    def test_login(self, setup):
        self.logger.info("*********** Verifying Login page **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setMainPageLoginButton()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        after_login_title = self.driver.title
        # Поправить after_login_title, принимает не тот title
        if after_login_title == "Log In":
            assert True
            self.logger.info("*********** Home page title test is passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("*********** Home page title test is failed **********")
            assert False

# Запуск 2-х инстанций Фаерфокса -> pytest -s -v -n=2 testCases/test_login.py --browser firefox