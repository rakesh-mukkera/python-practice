# Check whether a year is a leap year
'''year = int(input("enter a number : "))
if year % 400 == 0 or (year%100 != 0 and year % 4==0):
    print("its leap year")
else:
    print("its not a leap year")'''


# Write a Python program to check whether a given character is Vowel:
'''str1 = str(input("enter a char : "))
a = "aeiouAEIOU"
if len(str1) != 1 or not str1.isalpha():
    print("invalid input")
elif str1 in a:
    print("its a vowel")
else:
    print("its not a constant")'''


# Write a Python program to print the grade based on the following criteria:
'''marks = int(input("enter a number : "))
if 90 <= marks <= 100:
    print("a")
elif 80 <= marks <= 89:
    print("b")
elif 70 <= marks <= 79:
    print("c")
elif 60 <= marks <= 69:
    print("d")
elif 0 <= marks <= 59:
    print("fail")
else:
    print("invalid input")'''



# Check whether a number is divisible by both 3 and 5
'''mul = int(input("enter a number : "))
if mul % 3 == 0 and mul % 5 == 0:
    print("this number is divided by the 3 and 5")
else:
    print("this is not divide by this numbers")'''


# Find the smallest among four numbers
'''a = 10
b = 25
c = 5
d = 18
if a < b and a<c and a<d:
    print("a is big")
elif b<a and b<c and b<d :
    print("b is big")
elif c<a and c<b and c<d :
    print("c is big")
elif d < a and d<b and d<c:
    print(" d is big")
else:
    print("all are equal")'''


# Check whether a character is:
# Uppercase letter
# Lowercase letter
# Digit
# Special character

ch = (input("enter a string : "))
# ch = len(ch)==1
if "A"<= ch <= "Z":
    print("the enter char is cap")
elif "a" <= ch <="z":
    print("the char is small")
elif "0"<= ch <= "9":
    print("its number")
else:
    print("its a special character")
