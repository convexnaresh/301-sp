# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)




print("\n\t Formatting Integers")
# formatting integers
str_1="Binary representation of {0} is {0:b}".format(12)
#'Binary representation of 12 is 1100'

# formatting floats
str_2="Exponent representation: {0:e}".format(1566.345)
#'Exponent representation: 1.566345e+03'

# round off
str_3="One third is: {0:.3f}".format(1/3)
#'One third is: 0.333'

# string alignment
str_4="|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')
#'|butter    |  bread   |       ham|'

print("{}".format(str_1))
print("{}".format(str_2))
print("{}".format(str_3))
print("{}".format(str_4))