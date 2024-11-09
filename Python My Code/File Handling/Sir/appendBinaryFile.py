import pickle
f = open('myfile1.txt', 'ab')
pickle.dump('aaa',f)
f.close()
