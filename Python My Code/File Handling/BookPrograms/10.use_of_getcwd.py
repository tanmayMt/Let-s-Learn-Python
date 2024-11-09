import os

path=os.getcwd()
print("Current Absolute Path: ",path)
path=os.path.abspath("..")
print("os.path.abspath()    : ",path)