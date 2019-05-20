from .mylog import log 

class Report:
    def __init__(self):
        self.found= []
        self.installed= []
        self.error=[]



    def show(self):
        log.info("-"*40)
        log.info("REPORT")
        log.info("-"*40)
        log.info("Newly installed packages:")
        for pkg in self.installed:
            if(pkg not in self.error):
                log.info(" * {}".format(pkg))
        log.info("-"*40)
        log.error("Packages with error:")
        for pkg in self.error:
            log.error(" * {}".format(pkg))
        log.info("-"*40)
        if(len(self.error)==0):
            log.info("# Status: COMPLETED")
        else:
            log.info("# Status: INCOMPLETE")
        log.info("-"*40)   