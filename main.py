# import random
# import string
# password = []
# alphabet = string.ascii_letters
# digits = string.digits
# punctuation = string.punctuation
# a = random.sample(list(alphabet),5)
# b = random.sample(list(digits),3)
# c = random.sample(list(punctuation),2)
# aa = "".join(a)
# bb = "".join(b)
# cc = "".join(c)
# password.append(aa)
# password.append(bb)
# password.append(cc)
# var = "".join(password)
# print(f"your strong password is (☞ﾟヮﾟ)☞ {var}")

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x/y
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# a = int(input("1 for add\n2 for sub\n3for multiplication\n4 for div\n:- "))
# if a == 1: print(add(num1,num2))
# elif a == 2: print(subtract(num1,num2))
# elif a == 3: print(multiply(num1,num2))
# elif a == 4: print(divide(num1,num2))
# else: print("error")


# gussing game---



# import random
#
# number_to_guess = random.randint(1, 100)
#
# while True:
#     a = int(input("Enter your guess: "))
#
#     if a < number_to_guess:
#         print("Too low! Try again.")
#     elif a > number_to_guess:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed it!")
#         break

# init
#
# read
# insert
# line num count
# find word largest
# aappen txt to a file and display
#
# git -> whole project -> give the link

# class name:
#     def __init__(self,name):
#         self.name = f"hello i am {name}"
# a = name("kim")
# print(a.name)
# print(max(["hello","abc","abcdfg"],key=len))
with open("D:\\xyz.txt","r") as f:
    print(f"'the org text'\n{f.read()}")

with open("D:\\xyz.txt","a") as f:
    print(f.write("\n             \n"))

with open("D:\\xyz.txt","r") as f:
    print(f"new line->{f.read()}")

with open("D:\\xyz.txt","r") as f:
    print(f"line number:- {len(f.readlines())}")

with open("D:\\xyz.txt","r") as f:
    print(f"the longest word:- {max(f.read().split(),key=len)}")

with open("D:\\xyz.txt","a") as f:
    print(f.write(" append line"))

with open("D:\\xyz.txt","r") as f:
    print(f"append_line ->{f.read()}")

    
