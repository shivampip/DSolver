import logging
LOG_LEVEL = logging.DEBUG
#LOGFORMAT = "%(log_color)s%(levelname)s %(filename)s%(reset)s | %(log_color)s%(message)s%(reset)s"
LOGFORMAT = "%(log_color)s# %(message)s%(reset)s"
from colorlog import ColoredFormatter
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger('pythonConfig')
log.setLevel(LOG_LEVEL)
log.addHandler(stream)
log.info("Logging Started")


#log.debug("A quirky message only developers care about")
#log.info("Curious users might want to know this")
#log.warn("Something is wrong and any user should be informed")
#log.error("Serious stuff, this is red for a reason")
#log.critical("OH NO everything is on fire")

