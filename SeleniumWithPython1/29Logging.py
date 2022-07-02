import logging
#when there is any error while execution scripts we can capture in log.
logging.basicConfig(filename='F://RobotFrameworkSelenium With Python//logging.log')
logging.info('info')
logging.captureWarnings('capture')
logging.critical('critical')
logging.debug('debug')
logging.warning('warning')