import pickle
while True:
  print('1. Create a binary file')
  print('2. Reading records from a binary file')
  print('3. Append a new record into a binary file')
  print('4. Exit')
  choice = int(input('Enter your choice '))
  if choice==1:
    fname = input('Enter the file name ')
    f = open(fname, 'wb')
    list = []
    roll = input('Enter your roll number ')
    name = input('Enter your name ')
    list.append([roll,name])
    pickle.dump(list,f)
    f.close()
  elif choice==2:
    fname = input('Enter the file name ')
    f = open(fname, 'rb')
    try:
      while True:
        list = pickle.load(f)
        for i in list:
          print('Roll : ', i[0])
          print('Name : ', i[1])
    except Exception:
      f.close()
  elif choice==3:
    fname = input('Enter the file name ')
    f = open(fname, 'ab')
    list = []
    roll = input('Enter your roll number ')
    name = input('Enter your name ')
    list.append([roll,name])
    pickle.dump(list,f)
    f.close()
  elif choice==4:
    exit()
  else:
    print('Wrong choice ')
