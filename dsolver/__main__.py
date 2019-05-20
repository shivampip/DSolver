import argparse

from .mylog import log 
from .executor import Executor
from .processor import Processor 
from .report import Report 

file_path= ""


exe= Executor()
pros= Processor()
rep= Report()


def process_output(out):
    log.info("Processing output")
    pkg= pros.find_missing_package(out) 
    if(pkg is None):
        log.info("No missing package")
        return False 
    else:
        log.info("Found missing package {}".format(pkg))
        exe.install_package(pkg)
        return True


def run():
    out= exe.run(file_path)

    if(process_output(out)):
        return True 
    else:
        run()
    


##########################################################################################

if __name__=="__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help= 'Give the path to desired file', required=True) 
    parser.add_argument('-l', '--log', help=' Log file ', required= False)                

    args= parser.parse_args() 
    if(args.file is not None):
        file_path= args.file
        if(exe.is_valid_path(file_path)):
            run()
            log.info("Running Error free script")
            exe.exe_script(file_path)
            rep.show()
        else:
            log.error("File path not valid")
