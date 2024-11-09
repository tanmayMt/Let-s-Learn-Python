with open("7.demo","w+") as f:
    f.write("Jio")
    f.seek(0)
    print(f.read())