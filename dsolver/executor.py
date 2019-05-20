from .mylog import log 
import subprocess 
import sys 
import os 


class Executor:
    def __init__(self):
        pass 


    def run(self, file_path):
        log.info("Trying to run {}".format(file_path))
        proc = subprocess.Popen(['python', file_path,  'arg1 arg2 arg3 arg4'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out= str(proc.communicate()[0])
        return out 


    def install_package(self, package):
        subprocess.call([sys.executable, "-m", "pip", "install", package])


    def exe_script(self, fname):
        exec(open(fname).read())


    def is_valid_path(self, path):
        return os.path.exists(path)