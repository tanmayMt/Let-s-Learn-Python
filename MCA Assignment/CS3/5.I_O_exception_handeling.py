try:
    f=open("myFile","x")
    f.write("Hello")
except IOError:
    print("Error: Could not open the file")
else:
    print("Successfully wrote to the file")
    f.close()