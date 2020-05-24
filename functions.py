def deleteFileName(relative_path, filename):
    with open(relative_path + "_.txt" , "r") as f:
        lines = f.readlines()
    f.close()
    with open(relative_path + "_.txt", "w") as f:    
        for filename in lines:
            if filename.strip("\n") != "nickname_to_delete":
                f.write(filename)
    f.close()

def printFiles(relative_path):
    f = open (relative_path + '_' + ".txt", "r")
    for list in f:
        print(list, end="")
    print("\n")
    f.close()