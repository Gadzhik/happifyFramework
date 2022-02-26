from selenium.webdriver.common.by import By


class LoginPage:
    login_button_main_page = "/html/body/main/section[1]/div/a"
    username_xpath = "//*[@id='email']"
    password_xpath = "//*[@id='password']"
    login_button_xpath = "//*[@id='submit_in']"
    menu_click_xpath = "/html/body/header/div/div/div/button"
    profile_click_xpath = "//*[@id='sidenav']/ul/li[8]/button"
    logout_button_xpath = "//*[@id='sidenav']/ul/li[8]/ul/li[7]/a"

    def __init__(self, driver):
        self.driver = driver

    def setMainPageLoginButton(self):
        self.driver.find_element(By.XPATH, self.login_button_main_page).click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def loginButton(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def menuClickXpath(self):
        self.driver.find_element(By.XPATH, self.menu_click_xpath).click()

    def profileClickXpath(self):
        self.driver.find_element(By.XPATH, self.profile_click_xpath).click()

    def logoutButton(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

