import re

# https://cs.lmu.edu/~ray/notes/regex/
# https://www.programiz.com/python-programming/regex

mystring = "UNIX tools rocks. Scrapple from the apple"
yourstring = "UNIX tools dances."

# check if a sub-string 456 exists in my_string
substr = "cks"
if substr in mystring:
    print("found!", substr)
else:
    print("not found", substr)

# Where does 456 occurs in my-string
# use index()
findex = mystring.index(substr)
print("found sub-str at ", findex)

# use find()
findex2 = mystring.find(substr)
print("again, found sub-str at ", findex2)

print("\n\t Use Regular Expression to find/match a pattern")

mystring = "UNIX tools rocks"
exp1 = 'cks'

# Try to find exp1 in in other string, this time regex returns an object that gives index.
result = re.search(exp1, mystring)
print("result:", result)
if result:
    print("\t '%s' found pattern at %d" % (exp1, result.start()))

# Try to find exp1 in in other string, this time regex returns None.
result = re.search(exp1, yourstring)
print("result:", result)
if result:
    print("\t '%s' found pattern at %d" % (exp1, result.start()))
else:
    print("\t pattern not found!")

##
print("\n\t dot(.) in regular expression")
mystring = "For me to poop on.."

exp1 = "o."  # dot(.) matches any character

result = re.search(exp1, mystring)
print("result:", result)
if result:
    print("\t '%s' found pattern at %d" % (exp1, result.start()))
else:
    print("\t pattern not found!")

print("\nFinding all occurances")
# find all occurances of the expression.
result2 = re.findall(exp1, mystring)
print("result2:", result2)
if result2:
    print("\t ", exp1, " found pattern as ", result2)
else:
    print("\t pattern not found!")

print("\n\t Character classes [] in regular expression")
mystring = "beat a brat on a boat"
exp1 = "b[eor]at"  # matches any character in []

# find all occurances of the expression.
print("\nFinding all occurances")
result2 = re.findall(exp1, mystring)
print("result2:", result2)
if result2:
    print("\t ", exp1, " found pattern as ", result2)
else:
    print("\t pattern not found!")

print("\n\t Character classes can be negated with [^] in regular expression")
mystring = "beat a brat on a boat"
exp1 = "b[^eo]at"  # matches any character except e or o

# find all occurances of the expression.
print("\nFinding all occurances")
result2 = re.findall(exp1, mystring)
print("result2:", result2)
if result2:
    print("\t ", exp1, " found pattern as ", result2)
else:
    print("\t pattern not found!")

# match phone number of this format
exp2 = r"^\([0-9]{3}\)-[0-9]{3}-[0-9]{4}$"
phone = "(662)-497-0040"

print("\n\tEmail Validation")
# Check if the following string are valid email address
# Valid Email format =<any-alpha-numeric-string>+<@>+<any-substring>+<any-substring-of-size-3>

myemail1 = "naresh.adhikari@sru.dedu"
myemail2 = "naresh.adhikari@gmail.edu"
myemail3 = "naresh.adhikari$yahoo.edu"  # invalid
myemail4 = "naresh_1234@facebook.edux"  # invalid

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
if (re.search(regex, myemail1)):
    print("Valid Email")

else:
    print("Invalid Email")

if (re.fullmatch(regex, myemail1)):
    print("Full match, Valid Email")

else:
    print("Full match, Invalid Email")