'''
    Python: Is interpreted
    Python is interactive
    Python is Object-Oriented
    Python is most popular language

    Python Installation, python 3.
    Python IDE: IDLE, Pycharm, Atom, etc.
    Working in a team on a Python Project: Git, Github.
'''
#Commenting methods: using # and ''' '''
#Importing library in python using 'import keywords'
import string
import math
import sys

#Python 3 variable declaration and initialization
lstart_year=2021 #int type, loan start year
loan=55.55 #float type
name="David Lee" #string type

'''
Python Data Types:
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
'''

x = 5
print(type(x), ",",type(loan),",",type(name),",",type(lstart_year))

#Type conversion
y= str(x)
z=str(loan)
print(type(y), ",", type(z))

'''
Type Conversion
    x = str("Hello World")	str	
    x = int(20)	int	
    x = float(20.5)	float
'''


print("\n\n")
print(name,",",lstart_year, loan)
lapprovedby=input("Enter loan approved by:")
print("Approved by:",lapprovedby)

#looping using for loop
maxloan_time=5 #in year
for i in range(0,maxloan_time):
    print("year-",i, "interest", loan*i/float(100), ", rounded interest=", round(loan*i/float(100)), "%.2f" %(loan*i/float(100)) )
print("\n\n")
#if-else
for i in range(0,maxloan_time):
    if i==3:
        print("Mid-term notification")
    elif i>3:
        print("Warning time begins")
    else:
        print("Normal loan time")
    print("\t year-",i, "interest", loan*i/float(100), ", rounded interest=", round(loan*i/float(100)), "%.2f" %(loan*i/float(100)) )
print("\n\n")


print("Using while loop")
#use while loop
counter=0
while counter <= maxloan_time:
    #put all logic such as testing, etc.
    print("\t year-", i, "interest", loan * i / float(100), ", rounded interest=", round(loan * i / float(100)),
          "%.2f" % (loan * i / float(100)))
    counter+=1
print("End using while loop.\n\n")

#lists (arrays)
years=[2021, 2022, 2023, 2024]
names=["david", "shane", "emma"] #list or array, list of strings.
#iterate through a list
for year in years:
    print("year:", year)
print("\n\n")

#insert an item in the list
years+=[2024, 2025, 2026]

a=10
a +=5


print("updated list after insert",years)
#iterating through list index
listsize=len(years)
for index in range(0,listsize):
    print("index-",index,"\t","item:",years[index])

#remove item on the list
years.pop(1) #pop by index.
print("updated list after pop",years)
print("\n\n")

#file input/output
outputfile="testfile.dat"
#open a file in a mode: read (r), write(w) or append(a)
fd = open(outputfile, "w") #fd is file descripter or file pointer, store its reference in the variable fd
#do something with open file
fd.write("#loan description for customer \n")
for year in years:
    fd.write("year-"+str(year)+"\n") #convert integer to string, and concat.
print("done with writing in file, closing file soon.")
#close it
fd.close()
print("\n\n")
#if more things to write on an existing file, open it on "append" mode.

#Data structures in Python
#1. Lists, tuples, sets
#2. Dictionary
#3.

#Python-functions
def function_name(var1, var2, var3):
    print("function_name(..,..,..)")
    print("parameters")
    print("var1, var2,var3",var1,var2,var3)
    #Other logic
    if type(var1)==type(var2)==type(var3):
        return var1+var2+var3 #concatenated all vars.
    else:
        return 0

def funa():
    print("this is fun a")


funa()


#calling a function
result=function_name(1,3,3) #passing all integers
result2=function_name("I-", "-you-", "-us-") #passing all string
result3=function_name("I", "am", 5) #passing string and integer

print("Result1:", result)
print("Result2:",result2)
print("Result3:",result3)

print("\n\n")
#Want to restrict the type of parameters to pass to a function?
def function_name2(var1:int):
    print("function_name2")
    print("parameters", var1)
    return "--"+ str(var1)

function_name2(78)

'''
#define more function, call a function from another function.
'''
def main():
    result1=function_name(1,2,3)
    result2=function_name2(result1) #calling another function from this function
    print("result2=", result2)
main()

'''
Read more on:https://www.tutorialspoint.com/python/python_basic_syntax.htm
'''

#make this file as a python library.
#this file's name becomes the name of python library/module.
if __name__ == '__main__':
    pass