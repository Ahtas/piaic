#%% Q.1.  Which of the following terms are related to dictionaries?
### Answer:
# a. value
# d. key


#%% Q.2. Just like lists, + operator is used to extend dictionaries?
### Answer:
# b. False


#%% Q.3. To access items from a dictionary, we specify the index of that item within [] like myDict[0] ?

### Answer:
# b. False

#%% Q.4. When we use [] to access the value from a dictionary which does not exist in that dictionary….?

### Answer:
# d. None of above

#%% Q.5. What does return the pop method of a dictionary?

### Code:

dict1 = {"name":"Arsalan","email":"arsalan@pakistanigeek.com"}
print(dict1.pop("email"))

### Answer:
# d. value of the key, if it exists in the dictionary



#%% Q.6. What does return popitem method return?

### Code:

dict1 = {"name":"Arsalan","email":"arsalan@pakistanigeek.com"}
dict1.popitem()

### Answer:
# b. tupple containing the pair of last item of the dictionary





#%% Q.7.Which of the following 2 methods can be used to iterate through the items of a dictionary?

### Answer:
# a. items()
# b. values()

#%% Q.8. Which one of the following is used to enclose a dictionary?

### Answer:
# b. {} curly brackets

#%% Q.9. Write Python Program add key-value pair in dictionary and check if a Given Key or Value or Both Exists in a Dictionary or Not.

### Answer:

def check_item_in_data(data,key,value):
    error = ""
    if data.get(key) and  data.get(key) == value:
        # check if field and value both are matched
        error += f"field: {key} and value: {value} both exists"
    else:
        # check if field or same value exists in field
        if data.get(key):
            # check if field already exist
            error += f"{key} field already exists"

        if data.get(key) == value:
            # check if data already exist
            error += f"{email} value is already exists"

    return [data,error]


data = {"name":"Arsalan"} # Check for no errors
# data = {"name":"Arsalan","email":"test@gmail.com"} # use this for field error
# data = {"name":"Arsalan","email":"arsalan@pakistanigeek.com"} # use this for field and value error

email = "arsalan@pakistanigeek.com"
data,error = check_item_in_data(data,"email",email)

if(error):
    print(error)

print(data)

#%% Q.10. Write a Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary and print only the words having Even (divisible by 2) frequency.

### Answer:

string = "I love Pakistan, Pakistan is our motherland and, our count is beautiful country, it is really nice feeling to live in pakistan, i love to serve pakistan"

words = string.replace(',','').lower().split() #remove comma,convert to lowercase and then split based on space

freq = [words.count(w) for w in words]

words_with_freq = dict(zip(words,freq)) #zip words and freq array and then convert into directory

even_length_words = [(w,f) for w,f in words_with_freq.items() if f % 2 == 0] # convert dict items in to list of tuples and filter even frequency items

for item in even_length_words:
    print(f"{item[0]} : {item[1]}")


#%% Q.11. X = ["Feb", Apr, Mar, May, Jun, Jul, Aug, Jan]. What will be output of following?

### Answer:

X = ["Feb", "Apr", "Mar", "May", "Jun", "Jul", "Aug", "Jan"]

print(X[0:3]) #  ['Feb', 'Apr', 'Mar']
print(X[2:8]) # ['Mar', 'May', 'Jun', 'Jul', 'Aug', 'Jan']
print(X[4:9]) #['Jun', 'Jul', 'Aug', 'Jan']
print(X[1:7:2]) # ['Apr', 'May', 'Jul']
print(X[-1:-7]) # []
print(X[-7:7]) # ['Apr', 'Mar', 'May', 'Jun', 'Jul', 'Aug']
print(X[-1:-8:-2]) # ['Jan', 'Jul', 'May', 'Apr']
print(X[:4]) # ['Feb', 'Apr', 'Mar', 'May']



#%% Q.12. Remove the correct number from the list X

### Code:

X = [ 9,2,8,4,5]
print(X)
X.remove(9)
print(X)

### Answer:
# 3) .remove(9)


#%% Q.13. p = 3 q = 'hello! ' print( q __?__ p) hello! hello! hello!

### Code:
p=3
q = 'hello! '
print(q*p)

### Answer:
# 1) *


#%% Q.14. y = "this is a random sentence"  print (y__?__) Output: THIS IS A RANDOM SENTENCE

### Code:
y = "this is a random sentence"
print(y.upper())

### Answer:
# 1) .upper()


#%% Q.15.

### Answer:

p = True # bool
q = 'True' # str
r = 2 # int
r = 2.0 # float
print(type(p)) # bool
print(type(q)) # str
print(type(r)) # float
print(type(s)) # NameError

#%% Q.16. What are the optional arguments to the function?
# function_1(R1, q, p=None, R2= None)

### Answer:
# 2) p and R2

#%% Q.17. Which command invokes method X() of the object p?

### Answer:
# 4) p.x()

#%% Q.18. X=4 , Y= 2

### Answer:

X=4
Y= 2
print(X % Y) # will output  0
print(X / Y) # will output  2.0
print(X // Y) # will output  2
print(Y % X) # will output  2


#%% Q.19. x = [[4, 1, 1], [5, 9, 0]]

### Answer:

# ========================================
x = [[4, 1, 1], [5, 9, 0]]

for i in x:
    for j in i:
        print(j)

# ========================================
for i,v in enumerate(range(len(x[0]))):
    print(x[0][i], "\t",x[1][i] )
# ========================================

for i in x:
    for j in i:
        print(j,end="\t")
print("")
# ========================================
for i in x:
    for j in i:
        print(j, end="\t")
    print("")

#%% Q.20. q = [10.62, 16.14, 6.45, 17.11]

# Code:
q = [10.62, 16.14, 6.45, 17.11]

for j,z in enumerate (q) :
    print( "Item " + str(j) + " - " + str(z))

### Answer:
# 3) j



#%% Q.21. Which of these about a dictionary is false?

### Answer:

# b) The keys of a dictionary can be accessed using values - we can't do it directly but using lambda function we can do it
# d) Dictionaries are mutable


#%% Q.22. What is the output of the following:

### Code:

D = dict()
for i in range (3):
    for j in range(2):
        D[i] = j

print(D)

### Answer:

# a. {0: 1, 1: 1, 2: 1}

#%% Q.23. You are writing a function that increments player score in a soccer game
# If no value is specified for points, then point must start with 1
# If no value is specified for bonus, then bonus should be True
# 01 def increment_score ( bonus , score , points ):

### Answer:

# To meet the first requirement line 01 must be change to
# def increment_score ( bonus , score , points = 1 ): (True)

# To meet the second requirement line 01 must be change to
# def increment_score ( bonus = True , score , points = 1 ): (False) Because after default parameters we can't write parameters without default values

# Once a parameter is defined with default value, any parameter to the right must also be defined with default values (True)



#%% Q.24. What will be output?

### Code:
def avg (x , y , z = 50 ):
    adding = x + y + z
    avg_value = adding / 3
    return avg_value
y = avg ( x = 5 , y = 9 , z = 20 )

print(y) # 11.333333333333334 will be printed

### Answer:

# 11.333333333333334 will be printed


#%% Q.25.  What will be output? Describe it with reason and logic behind.
# Do multiple experiments with arguments / parameters to remove error, if occurs.

### Code:
def avg ( *opt_values , name ):
    avg_value = sum (opt_values) / len(opt_values)
    print("name is: " + name + " Marks: " + str(avg_value))

avg ( 5 , 9 , 20, 34, 87, 112 , name="Ali" ) # 44.5  will be printed

### Answer:
# 44.5  will be printed
# There was an error for name parameters because we taking *opt_values as a first argument and if it is first argument we must have to pass
# all right side params as a named arguments. so it is fixed by using name="Ali" argument


#%% Q.26. Final output is not required. Just take copy pencil, think and write the output of each line,
# write down the link between parameters and arguments. Remove one or two ** from other_info and observe the ouput.

### Code:

def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
display_result(winner="Manchester", score="4-3", overtime ="yes", injuries="none")

### Answer:

# Output :
#The winner was Manchester
#The score was 4-3

# winner and score are named argument and will map to function params as it is
# overime and injuries will map to other_info which is directory unpacking/decomposing parameter
# remove one * will give an error as it will expect comma seperated values but we are passing named arguments which doesn't exists
# remove two ** will also give an error as it will expect other_info param as a single required parameters while we aren't providing this param



#%% Q.27. The position of parameters and arguments is re-arranged. Just think and find the logic behind output or error.

### Code:
def display_result(winner, score, **other_info): # Rearranged params because unpacking dictionary can't be in middle
    print("The winner was " + winner)
    print("The score was " + score)

display_result(winner="Manchester", overtime ="yes", injuries="none" , score="1-0" )


### Answer:
# unpacking dictionary can't be in middle

#%% Q.28. What will be the output of the following Python expression if X=123?

### Code:
X=123
print("%06d"%X) # 6 digits 0 padded if digit length is less then 6

### Answer:
# b) 000123


#%% Q.29. What will be the output of the following Python expression if x=22.19?

### Code:
x=22.19
print("%5.2f"%x)

### Answer:
# c) 22.19


#%% Q.30. What will be the output of the following Python code?

### Code:
'{0:f}, {1:2f}, {2:05.2f}'.format(1.23456, 1.23456, 1.23456)

### Answer:

# c) No output  but if print it then d) 1.234560, 1.234560, 01.23



#%% Q.31. Write down the output of each line after each iterations. Do multiple experiments to change values

### Code

i = 1
while False: # This code will never run because we set expression as false, if it set by true then it will run infinity time
    if i%2 == 0:  # if the value is even then break the loop
        break
    print(i)
    i += 2  # add 2 into i existing value

### Answer:

# As the code above it will never run due to False condition in while statement
# If we change
#     While True then it will run infinity time because break condition will never meet which is i should be even.
#     if we set i even number 2 then it will never print i value and break before reaching to print statement due to if condition
#     if we set i odd number then it will run infinity time


#%% Q.32. Write down the output of each line after each iterations. Do multiple experiments to change values

### Code

x = "abcdef"
i = "a"
while i in x:
    x = x[:-1] # reduce string length from end but never move cursor to next item
    print(i, end = " ")

### Answer:

# Iteration 1
# x = abcdef
# ouput a

# Iteration 2
# x = abcde
# ouput a

# Iteration 3
# x = abcd
# ouput a

# Iteration 4
# x = abc
# ouput a

# Iteration 5
# x = ab
# ouput a

# Iteration 6
# x = a
# ouput a

# Final Output:  a a a a a a

# List Empty and while conition is break


#%% Q.33. Write down the output of each line after each iterations. Do multiple experiments to change values

### Answer:
# list function will convert string into charater list
# reversed function will iterate in a reverse order on list
# join function will join the generated reverse order list into string
# and loop will iterate over string and print character one by one
# Also if we don't join the reverse list the output will be same

for i in ''.join(reversed(list('abcd'))):
    print (i)

# Iteration 1 - d
# Iteration 2 - c
# Iteration 3 - b
# Iteration 4 - a

#%% Q.34.

for i in range(10):
    if i == 5:
        break
    else:
        print(i)
else:
    print("Here")

### Answer:

# Iteration 1 - Fall in else block - will print = 0
# Iteration 2 - Fall in else block - will print = 1
# Iteration 3 - Fall in else block - will print = 2
# Iteration 4 - Fall in else block - will print = 3
# Iteration 5 - Fall in else block - will print = 4
# Iteration 6 - Fall in if block value of i = 5 - Loop will be break
# It will only fall in else block if the ranger or given list is zero its called for-else loop


#%% Q.35.
y = 6
z = lambda x: x * y
print (z(8))

### Answer:

#lambda functions are inline functions are annoymous function
#In above code we have created a lambda function which takes parameter x value and multiply with a block scope variable y and return it
#Ouput of above code will be 48 where x=8 and y = 6


#%% Q.36.  Write output and give proper logic of whatever the output comes

i=0
def change(i):
    i=i+1
    return i
change(1)
print(i)

### Answer:

# When we print i after calling change function it will show the old i value which was set at the time of initialization not the one we have
# changed in then "change" function. because the i have different scope in both block, in change function we are getting single paramter "i"
# which have local scope and it can't change the outter side variable value. until variable is passed through ref or the returned value again
# assigned to i where function is calling such as i = change(1)


#%% Q.37. Wasn't exists in file

### Answer:

#%% Q.38. Wasn't exists in file

### Answer:

#%% Q.39. Wasn't exists in file

### Answer:

#%% Q.40. What will be output? Define this output clearly


### Code:

def change(one, *two):
    print(type(two)) # print type of parameters which is tuple
    print(two) # print tuple value
change(1,2,3,4)

### Answer:

# Above code will output :
#   1- a type of variable "two"
#   2- a tuple value (2, 3, 4)
# As we used decomposing operater "*" in parameter which will convert all the comma seperated argument after required argument "one" into tuple


#%% Q.41. What will be output? Define this output clearly

### Code :

def find(a, **b):
    print(type(b))
find('letters',A='1',B='2')

### Answer:
# It will return dict type object,  **b will take all key value pair arguments after a and will generate a dictionary of these options


#%% Q.42.  Write output and define each line’s output for each iteration of ‘i’

def foo(i, x=[]):
    x.append(i)
    return x
for i in range(3):
    print(foo(i))

### Answer:

# For loop from 0 to 3
# Will pass i value into foo function

# Iteration 1 :
#   i = 0, x = empty array
#   appent i into x list
#   x will be [0]
#   Print value x which is return by function foo in loop

# Iteration 2 :
#   i = 1, x = [0]
#   append i into x list, which is already innitialized on first iteration
#   x will be [0, 1]
#   Print value x which is return by function foo in loop

# Iteration 3 :
#   i = 2, x = [0, 1]
#   append i into x list, which is already exists in memory
#   x will be  [0, 1, 2]
#   Print value x which is return by function foo in loop

# Here main point is to be noted x array is only initialized one time because its reference type and behave like static data in memory


#%% Q.43.  Evaluate the following Python arithmetic expression: and write which segment will execute first?
# (Brackets, Exponents, Multiplication, Addition / Subtraction, Left to right rule)

(3* (1+2)**2 - (2**2)*3)
### Answer:

# 1- Brackets
# 2- Exponents
# 3- Multiplication
# 4- Addition
# 5- Substraction

# 1 - (1+2) will be 3 - (3* (3)**2 - (2**2)*3)
# 2 - (2**2) will be 4 - (3* (3)**2 - (4)*3)
# 3 - (3)**2 will be 9 - (3* 9 - (4)*3)
# 4 - 3* 9 will be 27 - (27 - (4)*3)
# 5 - (4)*3 will be 12 - (27 - 12)
# 6 (27 - 12) will be 15 (27 - 12)
# 7 15 will be answer


#%% Q.44. You are creating a function that manipulates a number. The function has the following requirements:
# A float is passed into the function
# The function must take the absolute value of the float
# Any decimal points after the integer must be removed

### Code :
import math
x = math.fabs(-50.3) # used to retrive absolute value from float
math.floor(x) # used to remove decimal points

### Answer:
# E. math.fabs(x)  used to retrive absolute value from float
# C. math.floor(x) used to remove decimal points



#%% Q.45. You are writing code that generates a random integer with a minimum value of 5 and a maximum value of 11.
# Which two functions should you use? Each correct answer presents a complete solution. (Choose two.)

### Code :

from random import randint, randrange
print(randint(5, 11)) # end value is included.
print(randrange(5, 12, 1)) # will exclude end value

### Answer:
# B. random.randint(5, 11)
# C. random.randrange(5, 12, 1)

#%% Q.46. Write a program that receives marks from user and check the grade.

### Answer:
# In code below we don't need to specify upper limit "user_marks" in elif condition because these conditions are written in a sequence,
# The power of this code will show when your rearrange elif in any random order it will never never have logical error.

user_marks = input("Enter your marks: ")
if(user_marks.isnumeric() == True):
    user_marks = int(user_marks)
    grade = ""
    if(user_marks >= 90):
        grade = "A"
    elif(user_marks >= 80 and user_marks < 90):
        grade = "B"
    elif(user_marks >= 70 and user_marks < 80):
        grade = "C"
    elif(user_marks > 60 and user_marks < 70 ):
        grade = "D"
    elif(user_marks <= 60):
        grade = "E"
    print(f"Your Grade: {grade}")
else:
    print("Please enter numeric value")
