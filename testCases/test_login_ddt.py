import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    # Используем класс из readProperty.py
    baseURL = ReadConfig.getApplicationURL()
    # Путь до эксель файла в котором находятся нужные данные
    path = "./TestData/LoginData.xlsx"
    # Вызываем метод loggen из класса LogGen
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_Login **********")
        self.logger.info("*********** Verifying Login page **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        # Получаем данные из таблицы эксель
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows in a Excel: ", self.rows)

        lst_status = [] # Empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setMainPageLoginButton()

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.loginButton()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Home Page | Happify"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.menuClickXpath()
                    time.sleep(3)
                    self.lp.profileClickXpath()
                    time.sleep(3)
                    self.lp.logoutButton()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.menuClickXpath()
                    time.sleep(3)
                    self.lp.profileClickXpath()
                    time.sleep(3)
                    self.lp.logoutButton()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test failed ***")
            self.driver.close()
            assert False

        self.logger.info("*** End of Login DDT test ***")
        self.logger.info("*** Complete LoginDDT_002 ***")


