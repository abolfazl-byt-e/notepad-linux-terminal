def insert(string):
    with open("note.txt", "a+") as notepad:
        string = "\n" + string
        notepad.write(string)
    notepad.close()
    print("your note added sucssecfull!!")


def delete_all():
    with open("note.txt", "w") as notepad:
        notepad.write("")
    notepad.close()
    print("all notes deleted sucssesfull!!")

def read():
    with open("note.txt", "r") as notepad:
        data = notepad.read()
    notepad.close()
    return data

def read_special_line(n):
    with open("note.txt", "r") as notepad:
        data = notepad.readlines()
    try:
        return data[n]
    except IndexError:
        print("number of lines of note is less than %d lines"%n)
while True:
    x = int(input("----------------------------\nwhat are you do?\n1=add a new note\n2=read all notes\n3=read a special line from note\n4=delete all notes\n0=exit\n----------------------------\n--> "))
    if x == 1:
        string = input("enter your note:\n")
        insert(string)
    elif x == 2:
        print(read())
    elif x == 3:
        n = int(input("enter number of line:\t"))
        print(read_special_line(n-1))
    elif x == 4:
        delete_all()
    elif x == 0:
        print("nice to meet you :)")
        break
    else:
        print("what the :)")
    y = input('----------------------------\ndo you want to continue(y,n): ')
    if y=="n":
        break



