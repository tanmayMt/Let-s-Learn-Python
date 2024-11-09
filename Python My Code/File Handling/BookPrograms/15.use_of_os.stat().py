import os

stats=os.stat("15.demo.txt")
# print(stats)
print("size= ",stats.st_size)