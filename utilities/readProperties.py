import configparser

# В данном файле мы читаем данные из common.ini

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getFirstName():
        firstname = config.get('register info', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('register info', 'lastname')
        return lastname

