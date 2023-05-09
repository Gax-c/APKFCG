A python script to extract the function call graph from `.apk` file

I use `Androguard` to initialize the call graph. If you are interested in `Androguard`, you can visit its [repo]([androguard/androguard: Reverse engineering and pentesting for Android applications (github.com)](https://github.com/androguard/androguard)).



## Installation

### download the repo

```
git clone 
```





### install Androguard

First, make sure you have installed `Androguard`, if you have installed it, you can skip this slice. 

If not, you can visit its repo for installation, or you can install it from this repo. 

If you want to install `Androguard` from this repo, please follow the following steps: 

```
cd androguard
pip install -r requirements.txt
python setup.py install 
```

Please make sure the version of your `networkx` is 2.5

The version of this `androguard` is 3.4.0 





### usage

The main components are `initializeFCG.py`、`generateFCG.py`、`main.py`

`initializeFCG.py` is used to initialize the FCG, which uses `Androguard` to generate the FCG. 

`generateFCG.py`is used to filter the FCG, you can use the parameter `--CLASS`, `--METHOD`, etc. to filter the FCG. 

Finally the program will output the number of the nodes left, and three sets `internalNode`, `externalNode`, `exsistingEdge`will be returned. 

You can only use `main.py` to achieve the functions above. 





### example 

```
python main.py app-debug.apk --CLASS
```

run above to get the FCG of `app-debug.apk`. 