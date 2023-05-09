import argparse 
import networkx as nx 

def getModuleName(name) :
    name = name[26:] 
    pos = name.find("->") 
    name = name[:pos - 1] 
    cnt = name.count("/") 
    nameList = name.split("/") 
    if cnt <= 2:
        name = nameList[0] 
    else :
        name = "/".join(nameList[:-2]) 
    return name.strip() 

def getPackageName(name) :
    name = name[26:] 
    pos = name.find("->") 
    name = name[:pos - 1] 
    cnt = name.count("/") 
    nameList = name.split("/") 
    if cnt <= 1 :
        name = nameList[0] 
    else :
        name = "/".join(nameList[:-1]) 
    return name.strip() 

def getClassName(name) :
    name = name[26:]
    pos = name.find("->") 
    return name[:pos - 1].strip()

def getmethodName(name) :
    name = name[26:] 
    pos = name.find("@") 
    name = name[:pos - 1] 
    return name.strip() 

def processFCG(apkPath, args) :
    print("[INFO    ] Start processing...")
    gexfPath = apkPath + ".gexf"  
    G = nx.read_gexf(gexfPath) 
    degree = dict() 
    exsistingNode = set() 
    exsistingEdge = set() 

    if args.MODULE == True :
        moduleNode = set() 
        for elm in G.nodes() :
            moduleName = getModuleName(elm) 
            moduleNode.add(moduleName) 
            degree[moduleName] = 0 
        moduleEdge = set() 
        for elm in G.edges() :
            edge = (getModuleName(elm[0]), getModuleName(elm[1])) 
            if edge[0] != edge[1] :
                moduleEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = moduleNode 
        exsistingEdge = moduleEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(moduleNode), len(moduleEdge))) 

    elif args.PACKAGE == True :
        packageNode = set() 
        for elm in G.nodes() :
            packageName = getPackageName(elm) 
            packageNode.add(packageName) 
            degree[packageName] = 0 
        packageEdge = set() 
        for elm in G.edges() :
            edge = (getPackageName(elm[0]), getPackageName(elm[1])) 
            if edge[0] != edge[1] :
                packageEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = packageNode 
        exsistingEdge = packageEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(packageNode), len(packageEdge))) 

    elif args.CLASS == True : 
        classNode = set() 
        for elm in G.nodes() :
            className = getClassName(elm) 
            classNode.add(className) 
            degree[className] = 0 
        classEdge = set() 
        for elm in G.edges() :
            edge = (getClassName(elm[0]), getClassName(elm[1])) 
            if edge[0] != edge[1] :
                classEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = classNode 
        exsistingEdge = classEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(classNode), len(classEdge))) 
    
    else :
        methodNode = set() 
        for elm in G.nodes() :
            methodName = getmethodName(elm) 
            methodNode.add(methodName) 
            degree[methodName] = 0 
        methodEdge = set() 
        for elm in G.edges() :
            edge = (getmethodName(elm[0]), getmethodName(elm[1])) 
            if edge[0] != edge[1] :
                methodEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = methodNode 
        exsistingEdge = methodEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(methodNode), len(methodEdge))) 

    internalNode = set() 
    externalNode = set() 
    for elm in exsistingNode :
        if degree[elm] == 0 :
            externalNode.add(elm) 
        else :
            internalNode.add(elm) 
    print("[INFO    ] There are {} internal nodes, {} external nodes.".format(len(internalNode), len(externalNode))) 
    return internalNode, externalNode, exsistingEdge 

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("gexfPath", help = "the gexf path to genarate the FCG") 
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--MODULE", help = "use module mode", action = 'store_true')
    group.add_argument("--PACKAGE", help = "use package mode", action = 'store_true') 
    group.add_argument("--CLASS", help = "use class mode", action = 'store_true') 
    group.add_argument("--METHOD", help = "use method mode", action = 'store_true')
    args = parser.parse_args() 
    print("[INFO    ] Start processing...") 
    G = nx.read_gexf(args.gexfPath) 
    degree = dict() 
    exsistingNode = set() 
    exsistingEdge = set() 

    if args.MODULE == True :
        moduleNode = set() 
        for elm in G.nodes() :
            moduleName = getModuleName(elm) 
            moduleNode.add(moduleName) 
            degree[moduleName] = 0 
        moduleEdge = set() 
        for elm in G.edges() :
            edge = (getModuleName(elm[0]), getModuleName(elm[1])) 
            if edge[0] != edge[1] :
                moduleEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = moduleNode 
        exsistingEdge = moduleEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(moduleNode), len(moduleEdge))) 

    elif args.PACKAGE == True :
        packageNode = set() 
        for elm in G.nodes() :
            packageName = getPackageName(elm) 
            packageNode.add(packageName) 
            degree[packageName] = 0 
        packageEdge = set() 
        for elm in G.edges() :
            edge = (getPackageName(elm[0]), getPackageName(elm[1])) 
            if edge[0] != edge[1] :
                packageEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = packageNode 
        exsistingEdge = packageEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(packageNode), len(packageEdge))) 

    elif args.CLASS == True : 
        classNode = set() 
        for elm in G.nodes() :
            className = getClassName(elm) 
            classNode.add(className) 
            degree[className] = 0 
        classEdge = set() 
        for elm in G.edges() :
            edge = (getClassName(elm[0]), getClassName(elm[1])) 
            if edge[0] != edge[1] :
                classEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = classNode 
        exsistingEdge = classEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(classNode), len(classEdge))) 
    
    else :
        methodNode = set() 
        for elm in G.nodes() :
            methodName = getmethodName(elm) 
            methodNode.add(methodName) 
            degree[methodName] = 0 
        methodEdge = set() 
        for elm in G.edges() :
            edge = (getmethodName(elm[0]), getmethodName(elm[1])) 
            if edge[0] != edge[1] :
                methodEdge.add(edge)
                degree[edge[0]] += 1  
        exsistingNode = methodNode 
        exsistingEdge = methodEdge 
        print("[INFO    ] Processing done!!!") 
        print("[INFO    ] Find {} nodes, {} edges.".format(len(methodNode), len(methodEdge))) 

    internalNode = set() 
    externalNode = set() 
    for elm in exsistingNode :
        if degree[elm] == 0 :
            externalNode.add(elm) 
        else :
            internalNode.add(elm) 
    print("[INFO    ] There are {} internal nodes, {} external nodes.".format(len(internalNode), len(externalNode))) 
