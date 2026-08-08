# count the prime numbers
'''num = int(input("enter a number : "))
count = 0
for i in range(1,num+1):
    factor = 0
    for j in range(1,i+1):
        if i%j==0:
            factor+=1
    if factor == 2:
        count+=1
print(count)
'''

# Write a Python program to check whether a given number is a Strong Number
'''num = input("enter a number : ")
original = num
sum = 0
while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1,range+1):
        fact = fact*i
    sum = sum+fact
    num = num//10
if sum == original:
    print("strong number")
else:
    print("not a strong number")
'''

# Write a Python program to check whether a given number is a Perfect Number.
'''num = int(input("enter a number : "))
perfect = 0
for i in range(1,num):
    if num%i==0:
        perfect = perfect+i
if perfect == num:
    print("its a perfect number")
else:
    print("its not a perfect number")'''

# Write a program to print all the factors of a number in descending order
'''num = int(input("enter a number : "))
see = 0
for i in range(num,0,-1):
    if num % i == 0:
      
     print(i)
'''


# Count how many even digits and odd digits are present in a number
'''num = int(input("enter a number : "))
even_count = 0
odd_count = 0
while num > 0:
    digit = num%10
    if digit% 2== 0:
        even_count+=1
    else:
        odd_count+=1
    num=num//10
print(even_count)
print(odd_count)'''


# Find the sum of only the prime digits in a number
'''num = int (input("enter a number : "))
sum = 0
while num > 0:
    digit = num%10
    if num == 2 or num == 5 or num == 7:
        sum=sum+digit
    num=num//10
print(sum)'''



# Reverse a Number (Without Using String)
'''num = int(input("enter a number : "))
reverse = 0
while num > 0:
    digit = num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)'''


# Check whether a number is a Palindrome Number
'''num = int(input("enter a number : "))
original = num
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse*10+digit
    num=num//10
if reverse == original:
    print("its palindrome number")
else:
    print("not a palindrome number")'''



# Check whether a number is an Armstrong Number
num=int(input("enter number : "))
original = num
length = 0
sum = 0
temp = num
while temp > 0:
    length +=1
    temp=temp//10
temp=num
while temp >0:
    digit = temp%10
    sum = sum(digit**length)
    temp=temp//10
if sum == original:
    print("armstrong number")
else:
    print("not a armstrong number")

