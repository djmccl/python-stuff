import random
import os
import sys

print("Tutorial!")

# variables must start with a letter
n123 = 123

# five main types in Python
'''
Numbers, Strings, Lists, Tuples, Dictionariies
'''

# 7 arithmetic operators
# + - * / % ** //
print("5+2=", 5+2)
print("5-2=", 5-2)
print("5*2=", 5*2)
print("5/2=", 5/2)
print("5%2=", 5%2)
print("5**2=", 5**2)
print("5//2=", 5//2)

quote = "\"Always remember you are unique"

multi_line_quote = ''' just like everyone
else'''

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
print("\n" * 5) #5 new lines

#kill the newline print puts by default Python3 only, can you sys.stdout.write()
#NB... Remember to flush the stdout if you do it that way!
#print("I don't like ", end="")
#print(newlines)

#Lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes']
print("first item=", grocery_list[0])

grocery_list[0] = "Bread"
print("first item=", grocery_list[0])
