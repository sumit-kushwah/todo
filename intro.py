import os
import functions

relative_path = '../'

print("Enter list to work with!! or 'ls' to see all available lists")
if os.path.exists(os.path.join(relative_path, "_.txt")):
    pass
else:
    os.system('touch ../_.txt')

filename = input()

if filename == 'ls':
    functions.printFiles(relative_path)
    print("Ok ! Now type your favourite list")
    filename = input()

while True:
    while (filename == '_'):
        print("This file name is reserved!! Enter another file name ")
        filename = input()
    filepath = os.path.join(relative_path, filename)
    print("enter command (r/d/c/e/a/s) [" + filename + "]")
    type = input()
    try : 
        if type == "r":
            f = open(filepath + ".txt", "rt")
            print("--------------------------------")
            print ("work todo!!")
            print(f.read())
            f.close()
            print("--------------------------------")
        elif type == "a" and type != '_':
            f = open(filepath + ".txt", "at")
            task = input()
            f.write("\n*" + " " + task)
            f.close()
            print("task added successfully!!")
        elif type == "c" and type != '_':
            if os.path.exists(filepath + ".txt"):
                pass
                print("this file already exists!!")
            else :
                ff = open(filepath + ".txt", "wt")
                ff.close()
                _ = open(relative_path + "_.txt", "a")
                _.write("\n" + filename)
                _.close()
                print("file created successfully!!")
        elif type == "d" and type != '_':
            os.remove(filepath + ".txt")
            functions.deleteFileName(relative_path, filename)
            print("file removed successfully!!")
        elif type == "s" and type != '_':
            name = input()
            filename = name
            print("you are switched to '" + name + "' list")
        elif type == "ls":
            functions.printFiles(relative_path)
        elif type == "e":
            break
        else :
            print("invalid input!!")
    # except FileNotFoundError:
    #     print("this list is not present for this operation")
    except Exception as e :
        print(e)
    
print("good bye!!")
