import logging

# Добавляем логгирование


class LogGen:
    @staticmethod
    def loggen():
        # Задаем форматирование
        logging.basicConfig(filename='/home/nnm/PycharmProjects/happifyFramework/Logs/automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        # Задаем уровень логгирования
        logger.setLevel(logging.INFO)
        return logger

