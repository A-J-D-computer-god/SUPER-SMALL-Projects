try:

    import os

    work = input("""What should i do? 
      w = write d = del r = read dl = del The file a = add Some thing c = close""")
    note = input("Please write your note")
    if work == "W" or "w":
        f = open("My_Note.txt","w")
        f.write(note)
        f.close()
    if work == "r" or "R":
       f = open("My_Note.txt","r")
       print(f.read())
    if work == "dl" or "DL":
           os.remove("My_Note.txt")
    if work == "d" or "D":
        f = open("My_Note.txt","w")
        f.close()
    if work == "a" or "A":
        f = open("My_Note.txt","a")
        f.write(note)

except:print("Err... Something Went Wrong")
