# Print the multiplication tables from 1 to 5.
'''for i in range (1,6):
     for j in range(1,11):
          print(i,"*",j,"=",i*j)
'''
#     Q2. Print all pairs (i, j) where both i and j go from 1 to 3.
# Expected output:
# (1,1)
# (1,2)
# (1,3)
# (2,1)
# (2,2)
# (2,3)
# (3,1)
# (3,2)
# (3,3)
'''for i in range(1,4):
     for j in range(1,4):
          print(i,j)
'''

#           Print all combinations of two numbers from 1 to 5.
# Expected Output:
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 2 1
# 2 2
# ...
# 5 5
'''for i in range(1,6):
     for j in range(1,6):
          print(i,j)
'''

#           Print all numbers from 1 to 5, and for each number print all of its factors.
# Expected Output:
# Factors of 1:
# 1
# Factors of 2:
# 1
# 2
# Factors of 3:
# 1
# 3
# Factors of 4:
# 1
# 2
# 4
# Factors of 5:
# 1
# 5
'''for i in range(1,6):
    print("factors of",i)
    for j in range(1,6):
        if i%j == 0:
            print(j)
    print()
   ''' 
# Print all common factors of two given numbers.
# Example:
# num1 = 12
# num2 = 18
# Expected Output:
# 1
# 2
# 3 
# 6
'''num1 = 12
num2 = 18
for i in range(1,min(num1,num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
'''
# Write a Python program to print all the common factors of two numbers entered by the user.
# Example:
# Enter first number: 24
# Enter second number: 36
'''num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        print(i)
        '''
# Write a Python program to find the Greatest Common Factor (GCF/HCF) of two numbers.
# Example:
# Enter first number: 24
# Enter second number: 36
'''num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
hig =1
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i== 0:
        hig = i
         
print("great : ",hig)
'''

# Write a Python program to find the LCM (Least Common Multiple) of two numbers.
# Example:
# Input:
# 12
# 18
# Output:
# LCM = 36
'''num1 = 120
num2 = 1809
least = max(num1,num2)
while True:
    if least%num1==0 and least%num2==0:
        print(least)
        break
    least+=1'''


    # Write a Python program to find the HCF (GCD) of two numbers entered by the user.

'''num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
n = 0
for i in range(1,min(num1,num2)+1):
    if num1%i== 0 and num2%i==0:
        n = i
print(n)'''



# Write a Python program to find the HCF (GCD) of three numbers.
# Example:
# Input:
# 24
# 36
# 48
# Output:
# 12
'''num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
num3 = int(input("enter a number : "))
hi = 0
for i in range(1,min(num1,num2,num3)+1):
    if num1%i== 0 and num2 % i == 0 and num3%i==0:
        hi = i
print(hi)'''


# check weather a given number is prime or not:
'''num1 = int(input("enter a number : "))
count = 0
for i in range(1,num1+1):
    if num1%i==0:
        count+=1
if count ==2:
    print("its prime number ")
else:
    print("its not a prime number")'''

# Write a Python program to check whether a given number is Prime or Not Prime.
'''num = int(input("enter a number : "))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count == 2:
    print("its a prime number : ")
else:
    print("its not a prime number : ")'''


# Write a Python program to print all prime numbers between 1 and 100
 
for i in range(1,101):
    count = 0
    for j in range(1,i+1):
        if i % j ==0:
            count+=1
    if count == 2:
        print(i)
