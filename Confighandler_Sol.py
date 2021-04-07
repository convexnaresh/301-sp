#Author: Naresh Adh
#Date: 03/15/2021
#Through this program, students will learn to:
#1. validate an input file and contents in it.
#2. Handle file opening in a mode
#2.1. Handle file exceptions, etc.
#3. Search file contents

#https://mrichen.github.io/wdlearn/file_parsing/index.html

def parse_file(filename):
    #open the file to read, and implement the logic as required by the assignment-4
    fd=open(filename)

    for l in fd.readlines():
        #remove spaces and new line char in the beginning and end of the line
        l=l.strip()
        if len(l) == 0 or l.startswith("//"):
            continue
        #split the line by comma or :
        tokens = l.split(":") # [keyword, true,|false,+ ..| (empty)
        if len(tokens) ==2:
            keyword=tokens[0].strip()
            value=tokens[1]
            value = value.strip() #remove space
            if value.startswith("true,"):
                print(keyword)


def validate_file(filename):
    #validate if the file is a text file, if it is return true, otherwise return false
    import magic

    # checking file extension .txt does not work!
    if filename.endswith(".txt"):
        return True

    #this is secure implementations
    ftype = magic.from_file(filename)
    if ftype.startswith("ASCII text"):
        return True
    return False


#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    valid=validate_file(filename)

    #print all the setting values set to ON/true on the configuration file.
    if valid:
        print("File %s is a valid text file. Now printing all the settings set ON" %filename)
        parse_file(filename)
    else:
        print("File %s is NOT a valid text file. Program aborted!" % filename)
