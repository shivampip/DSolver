import subprocess 
import sys 
import os 


class Executor:
    def __init__(self):
        pass 

    def run_command(self, cmd):
        proc = subprocess.Popen(cmd.split(), shell= True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, error = proc.communicate()
        return out, error 


    def run(self, file_path):
        proc = subprocess.Popen(['python', file_path,  'arg1 arg2 arg3 arg4'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out= str(proc.communicate()[0])
        return out 


    def install_package(self, package):
        subprocess.call([sys.executable, "-m", "pip", "install", package])

        #pip install "package>=0.2,<0.3"


    def exe_script(self, fname):
        exec(open(fname).read())


    def is_valid_path(self, path):
        return os.path.exists(path)