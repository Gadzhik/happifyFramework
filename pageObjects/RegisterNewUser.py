import random
import string
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterUser:
    # Add register page elements
    getStartedBtnXpath = "/html/body/main/section[1]/div/button"
    getStartedTodayBtnXpath = "//button[@class='button blue js-quiz mx-0 first-focus']" # Добавлен вручную
    genderRadioBtnXpath = "//span[@id='answer_0']" # Добавлен вручную
    ageRadioBtnXpath = "//span[@id='answer_2']" # Добавлен вручную
    checkBoxRaceSelect = "//a[@id='answer_6']" # Добавлен вручную
    clickNextBtnXpath = "//button[@class='button bottom js-multi-answer']" # Добавлен вручную

    jobRadioBtnXpath = "//span[@id='answer_2']"
    relationshipsRadioBtnXpath = "//span[@id='answer_2']"
    kidsCheckBoxBtnXpath = "//a[@id='answer_0']"
    kidsClickNextBtnXpath = "//button[@class='button bottom js-multi-answer']"
    adversityRadioBtnXpath = "//span[@id='answer_3']"
    connectedOthersRadioBtnXpath = "//span[@id='answer_2']"
    stressRadioBtnXpath = "//span[@id='answer_2']"
    experienceRadioBtnXpath = "//span[@id='answer_2']"
    meditationRadioBtnXpath = "//span[@id='answer_0']"
    otherConditionsNextBtnXpath = "//button[@type='submit']"
    usernameFieldXpath = "//input[@type='text']"
    emailFieldXpath = "//input[@type='email']"
    passwordFieldXpath = "//input[@name='password']"
    confirmPasswordFieldXpath = "//input[@name='cpassword']"
    iAgreeCheckBoxXpath = "//label[@class='terms_box-label']"
    continueBtnXpath = "//button[@class='button orange uppercase js-submit']"
    bodyContentXpath ="/html/body"
    #bodyContentXpath = "//h1[@class='TrackPromoBnr_title skip_nav_target']"

    # Нужно сделать Create Your Account
    fnameFieldXpath = "//input[@id='first-name-input']"
    lnameFieldXpath = "//input[@id='last-name-input']"
    monthSelectXpath = "//option[@value='0']"
    daySelectXpath = "//option[@value='30']"
    yearSelectXpath = "//option[@value='1980']"
    continueButtonXpath = "//button[@class='ModalForm_btn button orange']"
    privateModeCheckBoxXpath = "/html/body/div[4]/div/div/div/div/section/ul/li[1]/div[1]/div[1]"
    continuePrivateButtonXpath = "//*[@id='customize_profile']/div/div/button"
    startFirstTrackXpath = "//div[@class='col-md-7 col-sm-12 desc']//following-sibling::a[2]"
    howHappifyWorksButtonXpath = "//div[@class='intro-slide slide-1 viewed']//div[@class='slide-header']//button"
    basicSkillButtonXpath = "//button[@class='forward intro-slides-arrow-forward js-forward button-next']//following-sibling::h1"
    emotionalImprovementsButtonXpath = "//button[@class='finish intro-slides-arrow-finish js-close button-next']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnGetStartedBtn(self):
        self.driver.find_element(By.XPATH, self.getStartedBtnXpath).click()

    def clickOnStartedTodayBtn(self):
        self.driver.find_element(By.XPATH, self.getStartedTodayBtnXpath).click()

    # Добавить xpath для каждого пола
    # def clickOnGenderRadioBtn(self, gender):
    #     if gender == 'Male':
    #         self.driver.find_element(By.XPATH, self.genderRadioBtnXpath).click()
    #     elif gender == 'Female':
    #         self.driver.find_element(By.XPATH, self.genderRadioBtnXpath).click()
    #     else:
    #         self.driver.find_element(By.XPATH, self.genderRadioBtnXpath).click()

    def clickOnGenderRadioBtn(self):
        self.driver.find_element(By.XPATH, self.genderRadioBtnXpath).click()

    def clickOnAgeRadioBtn(self):
        self.driver.find_element(By.XPATH, self.ageRadioBtnXpath).click()

    def clickOnCheckBoxRaceSelect(self):
        self.driver.find_element(By.XPATH, self.checkBoxRaceSelect).click()

    def clickOnNextBtn(self):
        self.driver.find_element(By.XPATH, self.clickNextBtnXpath).click()

    def clickOnJobRadioBtn(self):
        self.driver.find_element(By.XPATH, self.jobRadioBtnXpath).click()

    def clickOnRelationshipsRadioBtn(self):
        self.driver.find_element(By.XPATH, self.relationshipsRadioBtnXpath).click()

    def clickOnKidsCheckBoxBtn(self):
        self.driver.find_element(By.XPATH, self.kidsCheckBoxBtnXpath).click()

    def clickOnKidsClickNextBtn(self):
        self.driver.find_element(By.XPATH, self.kidsClickNextBtnXpath).click()

    def clickOnAdversityRadioBtn(self):
        self.driver.find_element(By.XPATH, self.adversityRadioBtnXpath).click()

    def clickOnConnectedOthersRadioBtn(self):
        self.driver.find_element(By.XPATH, self.connectedOthersRadioBtnXpath).click()

    def clickOnStressRadioBtn(self):
        self.driver.find_element(By.XPATH, self.stressRadioBtnXpath).click()

    def clickOnExperienceRadioBtn(self):
        self.driver.find_element(By.XPATH, self.experienceRadioBtnXpath).click()

    def clickOnMeditationRadioBtn(self):
        self.driver.find_element(By.XPATH, self.meditationRadioBtnXpath).click()

    def clickOnOtherConditionsNextBtn(self):
        self.driver.find_element(By.XPATH, self.otherConditionsNextBtnXpath).click()

    # User input
    def inputUsernameField(self, username):
        self.driver.find_element(By.XPATH, self.usernameFieldXpath).send_keys(username)

    def inputEmailField(self, email):
        self.driver.find_element(By.XPATH, self.emailFieldXpath).send_keys(email)

    def inputPasswordField(self, password):
        self.driver.find_element(By.XPATH, self.passwordFieldXpath).send_keys(password)

    def inputConfirmPasswordField(self, password):
        self.driver.find_element(By.XPATH, self.confirmPasswordFieldXpath).send_keys(password)

    def clickOniAgreeCheckBox(self):
        self.driver.find_element(By.XPATH, self.iAgreeCheckBoxXpath).click()

    def clickOnContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtnXpath).click()

    def inputFirstNameField(self, username):
        self.driver.find_element(By.XPATH, self.fnameFieldXpath).send_keys(username)

    def inputLastNameField(self, username):
        self.driver.find_element(By.XPATH, self.lnameFieldXpath).send_keys(username)

    def selectMonthListBox(self):
        self.driver.find_element(By.XPATH, self.monthSelectXpath).click()

    def selectDayListBox(self):
        self.driver.find_element(By.XPATH, self.daySelectXpath).click()

    def selectYearListBox(self):
        self.driver.find_element(By.XPATH, self.yearSelectXpath).click()

    def clickContinueButton(self):
        self.driver.find_element(By.XPATH, self.continueButtonXpath).click()

    def clickPrivateCheckBox(self):
        self.driver.find_element(By.XPATH, self.privateModeCheckBoxXpath).click()

    def clickContinuePrivateButtonXpath(self):
        self.driver.find_element(By.XPATH, self.continuePrivateButtonXpath).click()

    def clickStartFirstTrackXpath(self):
        self.driver.find_element(By.XPATH, self.startFirstTrackXpath).click()

    def clickHowHappifyWorksButtonXpath(self):
        self.driver.find_element(By.XPATH, self.howHappifyWorksButtonXpath).click()

    def clickBasicSkillButtonXpath(self):
        self.driver.find_element(By.XPATH, self.basicSkillButtonXpath).click()

    def clickEmotionalImprovementsButtonXpath(self):
        self.driver.find_element(By.XPATH, self.emotionalImprovementsButtonXpath).click()

    # def findBodyElementXpath(self):
    #     self.driver.find_element(By.XPATH, self.bodyContentXpath)
