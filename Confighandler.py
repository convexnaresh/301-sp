#Author: Naresh Adh
#Date: 03/15/2021
#Through this program, students will learn to:
#1. validate an input file and contents in it.
#2. Handle file opening in a mode
#2.1. Handle file exceptions, etc.
#3. Search file contents



def parse_file(filename):
    #open the file to read, and implement the logic as required by the assignment-4


    pass #//you can remove this line on your side.
def validate_file(filename):
    #validate if the file is a text file, if it is return true, otherwise return false


    return True
    pass #//you can remove this line on your side



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
