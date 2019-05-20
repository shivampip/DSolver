from .mylog import log 

class Report:
    def __init__(self):
        self.installed= []



    def show(self):
        log.info("-"*40)
        log.info("REPORT")
        log.info("-"*40)
        log.info("Newly installed packages:")
        for pkg in self.installed:
            log.info(" * {}".format(pkg))
        log.info("-"*40)

    