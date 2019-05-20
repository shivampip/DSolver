import argparse

from .mylog import log 
from .executor import Executor
from .processor import Processor 
from .report import Report 

file_path= ""


exe= Executor()
pros= Processor()
rep= Report()


def run():

    #Missing Package
    log.info("Resolving Missing Packages")
    while(True): 
        out= exe.run(file_path)
        pkg= pros.find_missing_package(out) 
        if(pkg is None):
            log.info("No missing package left")
            break 
        else:
            if(pkg in rep.found):
                rep.error.append(pkg)
                log.error("# {} package couldn't be installed.".format(pkg))
                break 
            log.info("Missing package: {}".format(pkg))
            rep.found.append(pkg)
            exe.install_package(pkg) 
            rep.installed.append(pkg)

    if(len(rep.error)==0):
        log.info("Running Error free script")
        exe.exe_script(file_path)
    
    rep.show()


##########################################################################################

if __name__=="__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help= 'Give the path to desired file', required=True) 
    parser.add_argument('-l', '--log', help=' Log file ', required= False)                

    args= parser.parse_args() 
    if(args.file is not None):
        file_path= args.file
        if(not exe.is_valid_path(file_path)):
            log.error("File path not valid")
        else:
            run()        
