from os import system 
import argparse 

class createFCG :
    def __init__(self, apkPath = "") :
        self.apkPath = apkPath 
        self.type = type 
        self.order = ""
    
    def generateOrder(self) :
        print("[INFO    ] Start initialization...")
        self.order = "androguard cg "; 
        self.order += self.apkPath + " "; 
        self.order += "--no-isolated "; 
        self.order += "-o " + self.apkPath + ".gexf"
        return self.apkPath + ".gexf" 

    def excute(self) :
        system(self.order)
        print("[INFO    ] FCG initialization done!!!")

def initFCG(apkPath) :
    fcg = createFCG(apkPath) 
    fcg.generateOrder()
    fcg.excute() 

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("apkPath", help = "apkPath you want to generate the FCG from")  
    args = parser.parse_args() 
    fcg = createFCG(args.apkPath) 
    fcg.generateOrder()
    fcg.excute() 
    
