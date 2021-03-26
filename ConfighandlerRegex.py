#Author: Naresh Adh
#Date: 03/26/2021
#Through this program, students will learn to:
    #1. validate an input file and contents in it using regular expression.
    #2. Handle file opening in a mode
    #2.1. Handle file exceptions, etc.
    #3. Search file contents
    #4. Use tools to check is a regular expression is 'evil'

#function-1
def classify_settings(filename):

    # implement function-1 as instructed

    seton= []
    setoff = []
    setdefault = []

    #Open the file

    #Read line by line from the file

        #use regular expression to find a line which is set to be 'true'
            #then parse the line to get the keyword, and insert it into seton list
            # seton +=[keyword]

        # use regular expression to find a line which is set to be 'false'
             # then parse the line to get the keyword, and insert it into setoff list
             # setoff +=[keyword]

        # use regular expression to find a line which is set to be 'default'
             # then parse the line to get the keyword, and insert it into setoff list
             # setdefault +=[keyword]

    #//return lists
    return seton, setoff, setdefault
    pass


#function-2
def  print_settings(setonlist, setofflist, setdefaultlist) :

    #implement function-2 as instructed
    non = len(setonlist)
    print("1) Set On keywords:")
    for i in range(1,non+1):
        print("{i}) {}", i, setonlist[i])

    pass

#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)

    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")
