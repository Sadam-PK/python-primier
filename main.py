name = 'Abu Bakar'

print(name)

salam ='''
Asalam
Alaikum
'''

print(salam)

## Comma, Appostrophe

single_quote_str = 'He said, "He\'s fine"'

print(single_quote_str)

## Embedding value

myscore = 100

message = 'my score %s points'
print(message % myscore)

# another example

nums = 'what did the number %s says to %s? Nice belt!!'

print(nums%(0,8))

# Multiply String

str = "a"

print(str*5)

# embed space and string

space = ' ' * 10
name = 'my name is %s sadam'
print(name % space)

# Jupyter Linked to Github

print("testing connection")

# List

fruit_list = ['mangoes', 'bananas', 'graphes']

print(fruit_list)

print(fruit_list[0])

print((fruit_list[0:2]))

# list holds different data types

_list = ['list','can', 'hold','integers', 'i.e', 1,2,3,4, 'and', 'strings', 'together']

print(_list)

# list in list

num = [1,2,3,4,5]

str = ['asd','zxc']

mylist =[num,str]


print(mylist)

# List Appending

str.append('xcv')

print(mylist)

# delete from list

del str[0]

print(mylist)

#list can be multiplied

list1 = [1,2,3,4,5]

print(list1*5)

#list can't be divided

#tuple - uses paranthesis () instead of brackets like list

#list can be modifiied.. Tuple can't be manipulated, but can be deleted

fibs = (1,2,3,4,5)

print(fibs)

#maps - dictionary, collection of key:value pairs

sports={
    'ali':'cricket',
    'imran':'football',
    'sadam':'table tennis'
}

print(sports)

print(sports['sadam'])

del sports['sadam']

print(sports)

sports['imran'] = 'cricket'

print(sports)

#conditional statements

age = 11

if(age < 20):
    print("Okay! fine. Have a good day..")

#Keep indentation

if(age<10):
    print("alright")
elif(age>10 and age<20):
    print("overage")
else:
    print("too old")

#variable with no value -- null -- not same as Zero

val = None

print(val)

val = 0

print(val)

#difference between STRINGS and NUMBERS?

#are interconvertable

# age = 10
#
# age = str(age)
#
# print(type(age))
#
# age = int(age)
#
# print(type(age))
#
# #decimal string value can only be converted to FLOAT number
#
# age = 10.5
#
# print(age)
#
# age = str(age)
#
# print(type(age))
#
# age = float(age)
#
# print(type(age))

#Loops

for x in range(0,5):

    #     print('%s salam' %x)

    print(f"{x} salam")

#     both same

#List and range together

print(list(range(0,10)))

wizard_list = ['spider', 'frog', 'snail', 'bear', 'bat']

for i in wizard_list:
    print(i)

#While Loop

x = 50
y = 90

while x < 70 and y < 100: #both conditions needs to be true to add 1 in x, y
    x+=1
    y+=1
    print(x, y)

#Functions - makes code reusable and meaningful

def name(myname):
    print(f"my name is {myname}")


name("sadam")

fname = 'Muhammad'
lname = 'Omer'

def testFun():
    print(fname, lname)

testFun()

#return function value

def testFun():
    num = 2
    mul = 3

    return num*mul

print(testFun())

def testReturnFunction(num, mul):

    return num*mul

print(testReturnFunction(2,3))

# what is MODULE? a file with PythonCode

import time

print(time.asctime())

#Objects - objects simplify the data

class Animal:
    def whatClass(self):
        print("This is animals class")
animal = Animal()

animal.whatClass()

#Python built-in functions

#absolute value fun

print(abs(-10))

#bool

test = 1

print(f"{test} is {bool(test)}")

test = 0

print(f"{test} is {bool(test)}")

print(dir())

