import logging

logger = logging.getLogger()
fhandler = logging.FileHandler(filename='/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Logs/automation.txt', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)
