
#Author: Naresh
#Date:
#Topics: Numbers and strings in Python and in-class activity.

import sys
import math

smax_int = sys.maxsize #max of signed integer value (-)- - - - - - - -... - - - - - - - #64 bits.
umax_int = sys.maxsize * 2 +1 #max of un-signed value


print("s max size:",smax_int)
print("s min size:",-smax_int-1)
print("u max size:",umax_int)
print("math.log2(sys.maxsize * 2 + 2),",math.log2(sys.maxsize * 2 + 2))

print("\n")
#string functions

mystring="hello how are you"
print("length of string:",len(mystring))
yourstring="hello I am fine"

#compare the strings
if mystring == yourstring:
    print("Wow!, we greet the same.")


#String Function-1: convert the first character to upper case; https://www.w3schools.com/python/python_ref_string.asp
fupper_str=mystring.capitalize()
print("First letter uupper Case:",fupper_str)
allupper=mystring.upper()
print("All char upper:",allupper)


#string enumeration: Access both index and values
allow_list= ['apples', 'bananas', 'oranges']
for idx, val in enumerate(allow_list):
  print("index is %d and value is %s" % (idx, val))

#Task-1: Insert an item in an existing list and print the entire list again without using enumeration


#Task-2: Print the size of the given allow_list

print("\n")

#use tuples of strings #tuples are immutable and has fixed size.
allow_tuple= ('apples', 'bananas', 'oranges')
for idx, val in enumerate(allow_list, start=99):
  print("index is %d and value is %s" % (idx, val))

#Task-3: An attempt to modify an existing item in a tuple. Uncomment the following statement and report what is the error you received.

#allow_tuple[2]="pineapple"

#Task-4: Append a new element 'pineapple' in the given tuple allow_tuple


#Task-5: Print all items in the given tuple