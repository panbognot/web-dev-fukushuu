import logging
from pathlib import Path

p = Path.cwd() / 'ch11_debugging'

# You can change the levels using the following:
# DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename=p / 'myProgramLog.txt',
    level=logging.DEBUG, 
    format=' %(asctime)s - %(levelname)s - %(message)s')

# Pass a level to disable logs for that level and below
# logging.disable(logging.CRITICAL)

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')