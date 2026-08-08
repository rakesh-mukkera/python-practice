# Print numbers from 1 to 20.
'''a = 0
while a <= 20:
    print(a)
    a+=1'''

# Print numbers from 20 to 1 using a while loop.
'''a = 20
while a >= 1:
    print(a)
    a-=1'''



# Print all even numbers from 1 to 50 using a while loop.
'''a = 1
while a<=50:
    if a % 2 == 0:
        print(a)
    a+=1'''




# Print all odd numbers from 1 to 50 using a while loop.
'''a = 1
while a <= 50:
    if a % 2 != 0:
        print(a)
    a+=1
'''



# Write a program to print the multiplication table of a given number using a while loop.
'''num = int(input("enter a number : "))
a = 0
while a <= 10:
    print(f"{num}x{a}={num*a}")
    a+=1'''


# Find the sum of numbers from 1 to N using a while loop.
# num = int(input("enter a number : "))
# a = 0
# total = 0
# while a <=num:
#     total=a+total
    
#     a+=1
# print(total)


# Write a program to find the sum of all even numbers from 1 to N using a while loop
'''num =int(input("enter a number : "))
a = 0
total = 0
while a<= num:
    if a%2 == 0:
        total = total+a
    a+=1
print(total)'''


# Find the sum of all odd numbers from 1 to N using a while loop
'''num = int(input("enter a number : "))
a = 0
total = 0
while a<=num:
    if a%2!=0:
        total= total+a
    a+=1
print(total)'''



# Count how many numbers are there from 1 to N using a while loop
'''num = int(input("enter a number : "))
a = 1
count = 0
while a<=num:
    count+=1
    a+=1
print(count)'''



# Print the squares of numbers from 1 to N using a while loop
'''num = int(input("enter a number : "))
a = 1
while a<= num:
    print(f"{a*a}")
    a+=1'''


# Count the number of digits in a given number using a while loop
'''num = int(input("enter a number : "))
count = 0
while num > 0:
    num = num//10
    count+=1
print(count)'''

# Find the sum of digits of a given number.
'''num = int(input("enter a number : "))
total= 0
while num > 0:
    digit = num % 10
    total = digit+total
    num = num//10
print(total)'''

# Find the product of the digits of a number.
'''num = int(input("enter a number : "))
pro = 1
while num > 0:
    digit = num % 10
    pro = pro * digit
    num = num // 10
print(pro)'''


# Reverse a number using a while loop.
# Example:
# Input: 1234
# Output: 4321
'''num = int(input("enter a number : "))
a = 0
while num > 0:
    digit = num% 10
    a = a*10+digit
    num = num//10
print(a)
'''

# Write a program to find the largest digit in a given number using a while loop.
'''num = int(input("enter a number : "))
larg=0
while num > 0:
    digit = num % 10
    if digit > larg:
        larg = digit
    num = num // 10
print(larg)'''



# Find the smallest digit in a given number using a while loop.

'''num = int(input("enter a numbers : "))
small = 9
while num > 0:
    digit = num % 10
    if digit < small:
        small = digit
    num = num // 10
print(small)'''



# Count how many even digits are present in a given number
'''num = int(input("enter a numbers : "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 ==0:
        count+=1
    num = num // 10
print(count)'''



# Count how many odd digits are present in a given number
'''num = int(input("enter a number : "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count+=1
    num = num //10
print(count)'''


# Find the sum of all even digits in a given number.
'''num = int(input("enter a number : "))
sum1 = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum1 = sum1 + digit
    num = num // 10
print(sum1)'''

# Find the sum of all odd digits in a given number
'''num = int(input("enter a number : "))
odd1 = 0
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        odd1 = odd1+digit
    num = num // 10
print(odd1)'''


# Check whether a number is a Palindrome using a while loop
'''num = int (input("enter a number : "))
org = num
re= 0
while num > 0:
    digit = num % 2
    re = re* 10+digit
    num = num//10
if digit == org:
    print("its palindrome")
else:
    print("its not a palindrome")'''


# Find the second largest digit in a number

'''num = int(input("enter a number : "))
larg = 0
sec =0
while num > 0:
    digit = num % 10
    if digit > larg:
        sec = larg
        larg = digit
    elif digit > sec and digit != larg:
        sec  = digit
    num = num // 10
print(sec)
'''

#    Find the second Largest Even Digit in a given number.
'''num = int(input("enter a number : "))
larg = 0
seclarg = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        if digit > larg:
            seclarg = larg
            larg = digit
        elif digit > seclarg and digit != larg:
            seclarg = larg
    num = num//10
print(seclarg)'''


# Find the Smallest Even Digit
num = int(input("enter the number : "))
small = 10  
while num > 0:
    digit = num%10
    if digit % 2 == 0:
     if digit < small:
        small = digit
    num = num // 10
print(small)


