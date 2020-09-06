import logging
from conftest import Log_path


class LogData:
    def getLogger(self):
        logger = logging.getLogger(__name__)
        logsone = logging.FileHandler(Log_path+"/logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        logsone.setFormatter(formatter)

        logger.addHandler(logsone)

        logger.setLevel(logging.DEBUG)
        return logger
