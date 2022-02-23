import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + ".")
print(rootPath)
sys.path.append(rootPath)