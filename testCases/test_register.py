import pytest
import time
import datetime
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterNewUser import RegisterUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import string
import random


class Test_003_RegisterUser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() # Logger

    # Добавляем подсветку веб элементов
    # def highlight(element):
    #     driver = element._parent
    #     def apply_style(s):
    #         driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
    #                               element, s)
    #         original_style = element.get_attribute('style')
    #         apply_style("background: yellow; border: 2px solid red;")
    #         time.sleep(.3)
    #         apply_style(original_style)

    def test_userRegister(self, setup):
        self.logger.info("***** Test_003_RegisterUser *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        #print(self.driver.current_window_handle)
        self.driver.maximize_window()
        time.sleep(2)


# Добавим сюда прохождение ассессмента
        self.reguser = RegisterUser(self.driver)
        time.sleep(2)
        self.reguser.clickOnGetStartedBtn()
        time.sleep(2)
        self.reguser.clickOnStartedTodayBtn()
        time.sleep(2)
        self.reguser.clickOnGenderRadioBtn()
        time.sleep(2)
        self.reguser.clickOnAgeRadioBtn()
        time.sleep(2)
        self.reguser.clickOnCheckBoxRaceSelect()
        time.sleep(2)
        self.reguser.clickOnNextBtn()
        time.sleep(2)
        self.reguser.clickOnJobRadioBtn()
        time.sleep(2)
        self.reguser.clickOnRelationshipsRadioBtn()
        time.sleep(2)
        self.reguser.clickOnKidsCheckBoxBtn()
        time.sleep(2)
        self.reguser.clickOnKidsClickNextBtn()
        time.sleep(2)
        self.reguser.clickOnAdversityRadioBtn()
        time.sleep(2)
        self.reguser.clickOnConnectedOthersRadioBtn()
        time.sleep(2)
        self.reguser.clickOnStressRadioBtn()
        time.sleep(2)
        self.reguser.clickOnExperienceRadioBtn()
        time.sleep(2)
        self.reguser.clickOnMeditationRadioBtn()
        time.sleep(2)
        self.reguser.clickOnOtherConditionsNextBtn()
        time.sleep(2)

        self.logger.info("************** Assessment complete **************" )

        # User Add
        time.sleep(2)
        self.reguser.inputUsernameField("gkurban" + dt_str)
        time.sleep(2)
        self.reguser.inputEmailField("gkurban+lvtest" + dt_str + "@alarstudios.com")
        time.sleep(2)
        # self.reguser.inputEmailField(self.email)
        # time.sleep(2)
        self.reguser.inputPasswordField("p@ssw0rD")
        time.sleep(2)
        self.reguser.inputConfirmPasswordField("p@ssw0rD")
        time.sleep(2)
        self.reguser.clickOniAgreeCheckBox()
        time.sleep(2)
        self.reguser.clickOnContinueBtn()
        time.sleep(5)

        self.reguser.inputFirstNameField("gadzhi")
        time.sleep(2)
        self.reguser.inputLastNameField("gg")
        time.sleep(2)
        self.reguser.selectMonthListBox()
        time.sleep(2)
        self.reguser.selectDayListBox()
        time.sleep(2)
        self.reguser.selectYearListBox()
        time.sleep(2)
        self.reguser.clickContinueButton()

        time.sleep(2)
        self.reguser.clickPrivateCheckBox()
        time.sleep(2)
        self.reguser.clickContinuePrivateButtonXpath()
        time.sleep(5)
        self.reguser.clickStartFirstTrackXpath()

        self.logger.info("***** Register successful *****")
        time.sleep(2)
        self.reguser.clickHowHappifyWorksButtonXpath()
        time.sleep(2)

        self.reguser.clickBasicSkillButtonXpath()
        time.sleep(2)

        self.reguser.clickEmotionalImprovementsButtonXpath()
        time.sleep(2)

        self.logger.info("********** Saving user info **********")

        self.logger.info("********** User validation started **********")

        self.msg = self.driver.find_element(By.XPATH, '/html/body').text

        print(self.msg)
        if 'START FREE TRACK' in self.msg:
            assert True == True
            self.logger.info("********** User register passed **********")
        else:
            self.driver.save_screenshot("/home/nnm/PycharmProjects/happifyFramework/Screenshots" + "user_register_scr.png")
            self.logger.error("********** User Register Failed **********")
            assert True == False

# Random email generator
# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))


# Time now
dat_obj = datetime.datetime.now()
dt_str = dat_obj.strftime("%f")


# time 42.25