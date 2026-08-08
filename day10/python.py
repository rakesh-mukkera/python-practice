# Strong Numbers in a Range
# Write a program to print all Strong Numbers between 1 and 100000.
# Example: 145 → 1! + 4! + 5! = 145/

'''num = int(input("enter a number : "))
for i in range(1,num+1):
    original = i
    temp = i
    sum=0
    while num >0:
        digit = temp%10
        fact = 1
        for j in range(1,digit+1):
            fact=fact*j
        sum=sum+fact
        temp=temp//10
if sum==original:
   print(original)'''


# Write a program to print all Strong Numbers between 1 and 100000.
# num=int(input("enter a number : "))
# for i in range(1,num+1):
#     original = i
#     temp = i
#     sum=0
#     while temp > 0:
#         digit = digit %10
#         fact = 1
#         for j in range(1,digit+1):
#             fact=fact*j
#             sum=sum+fact
#             temp=temp//10
# if temp==original:
#     print(original)

'''num = int(input("enter a number : "))
temp = num
sum = 0
x=len(str(num))
while num>0:
    digit = num%10
    sum=sum+digit**x
    num=num//10
if sum==temp:
    print("its armstone number")
else:
    print("its not a armstone number")'''


# Armstrong Numbers in a Range
# Take n from the user and print all Armstrong numbers from 1 to
'''num = int(input("enter a number : "))

for i in range(1,num+1):
    original = i
    temp = i
    sum = 0
    x=len(str(i))
    while temp > 0:
       digit = temp%10
       sum = sum+digit**x
       temp=temp//10
if sum==original:
    print(original)'''

'''num = int(input("enter a number : "))
count = 0
for i in range(1,num+1):
    original = i
    temp = i
    sum = 0
    fact = 1
    x=len(str(i))
    while temp > 0:
        digit = temp%10
        sum=sum+digit**x
        temp=temp//10
    if temp==original:
        count+=1
print(count)'''



# Take a number n from the user and find how many Strong Numbers are presen
'''num=int(input("enter a number : "))
for i in range(1,num+1):
    temp =i
    original = i
    sum=0
    # count = 0
    while temp>0:
        fact = 1
        digit = temp%10
        for j in range(1,digit+1):
          fact = fact*i
          sum=sum+fact
          temp=temp//10
if temp==original:
    print("its a strong number")
else:
    print("its not a strong number")'''


'''num = int(input("Enter the range: "))
for i in range(1, num + 1):
    original = i
    temp = i
    sum = 0
    while temp > 0:
        digit = temp % 10
        fact = 1
        for j in range(1, digit + 1):
            fact = fact * j
        sum = sum + fact
        temp = temp // 10
    if sum == original:
        print(original)'''

'''num=int(input("enter a number : "))
for i in range(1,num+1):
    temp = i
    original = i
    sum = 0
    while temp > 0:
        digit = temp%10
        fact = 1
        for j in range(1,digit+1):
            fact=fact*j
        sum = sum+fact
        temp=temp//10
    if original==sum:
        print(original)'''

'''num = int(input("enter a number : "))
for i in range(1,num+1):
    temp = i
    original = i
    count = 0
    while temp > 0:
        count=count+1
        temp=temp//10
    temp = i
    sum = 0
    while temp>0:
        digit = temp% 10
        sum=sum+digit**count
        temp = temp//10
    if original==sum:
        print(original)'''


# Write a Python program to print all numbers between 1 and 1000 that satisfy both conditions:

# The number itself must be prime.
# The sum of its digits must also be prime.
'''num = int(input("enter a number : "))
for i in range(1,num+1):
    # original = i
    # temp = i
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count = count+1
    if count==2:
        temp = i
        sum=0
        while temp >0:
            digit = temp%10
            sum=sum+digit
            temp=temp//10
        count2=0
        for k in range(1,sum+1):
            if sum%k==0:
                count2=count2+1
        if count2==2:
            print(i)
'''



# Perfect Numbers in a Range

# Write a Python program to print all Perfect Numbers between 1 and 10000.

'''num = int(input("enter a number : "))
# count = 0
for i in range(1,num+1):
    # temp = i
    original = i
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
            count = 0
        if original==count:
            print(original)
'''


# Write a Python program to print all numbers between 1 and 10000 that satisfy both conditions:

# The number must be prime.
# The number must be a palindrome

'''num = int(input("enter a number : "))
for i in range(1,num+1):
    original = i
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count == 2:
        temp =i
        reverse = 0
        while temp>0:
         digit = temp%10
         reverse =reverse*10+digit
         temp=temp//10
        if reverse==original:
         print(f"its a palindrome number{original}")'''


# Automorphic Numbers in a Range

# Write a Python program to print all Automorphic Numbers between 1 and 10000.
'''
num = int(input("enter a number : "))
for i in range(1,num+1):
    square = i*i
    original = i
    temp = i
    count = 0
    while temp > 0:
        digit = temp%10
        count= count+1
        temp=temp//10
    power=10**count
    last = square%power
    if last==original:
        print(original)'''
     
     
 
