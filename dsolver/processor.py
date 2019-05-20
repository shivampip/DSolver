class Processor:
    def __init__(self):
        pass 


    def find_missing_package(self, out):
        res= out.find("No module named")
        if(res==-1):
            return None
        else:
            name_start = out.find("'", res) + 1
            name_end= out.find("'", name_start) - 1
            name= out[name_start: name_end]
            return name 