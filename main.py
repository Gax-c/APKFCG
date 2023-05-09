import argparse 
from generateFCG import processFCG 
from initializeFCG import initFCG 
from config import config 

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("apkPath", help = "the apk path to genarate the FCG") 
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--MODULE", help = "use module mode", action = 'store_true')
    group.add_argument("--PACKAGE", help = "use package mode", action = 'store_true') 
    group.add_argument("--CLASS", help = "use class mode", action = 'store_true') 
    group.add_argument("--METHOD", help = "use method mode", action = 'store_true')
    args = parser.parse_args() 

    initFCG(args.apkPath)
    internalNode, externalNode, exsistingEdge = processFCG(args.apkPath, args)     
