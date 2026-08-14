# no args + no return type
'''def add():
    a=10
    b=20
    print(a+b)
add()'''


# args with no return
'''def add(a,b):
    print(a+b)
add(10,20)'''


# no args + return value
'''def add():
    a=10
    b=20
    return a+b
result=add()
print(result)'''


# args + return value
'''def add(a,b):
    return(a+b)
result = add(10,20)
print(result) '''



# Write a function with no arguments and no return value to print "Hello Python"
'''def basic():
    print("hello python")
basic()'''


# Write a function with no arguments and no return value to print the numbers 1 to 10
'''def numbers():
    for i in range(1,11):
        print(i)
numbers()'''


# Write a function that takes one argument and prints whether the number is positive or negative
'''def poss_neg(a):
    if a%2==0:
        print("its even")
    else :
        print("its odd")
     
        
poss_neg(10)
poss_neg(-19)
'''

# Write a function that takes two arguments and prints their sum.
'''def sum (a,b):
    print(a+b)
sum(10,20)'''


# Write a function that takes two arguments and prints the larger number.
'''def larger(a,b):
    if a>b:
        print(f"{a} is big")
    else:
        print(f"{b} is big")
larger(10,20)'''

# Write a function with no arguments that returns the sum of two numbers stored inside the function.
'''def inside():
    a=10
    b=20
    return a+b
result = inside()
print(result)'''


# Write a function with no arguments that returns the square of a number stored inside the function
'''def square():
    a=10
    return a*a
result = square()
print(result)'''


# Write a function that takes a number as an argument and returns its square
'''def square(a):
    return a*a
result=square(10)
print(result)'''


# Write a function that takes three arguments and returns their average
'''def avg(a,b,c):
    sum=(a+b+c)
    return  sum/3
result=avg(10,20,30)
print(result)'''


# Write a function that takes a number as an argument and returns whether it is even or odd.
'''def even_odd(a):
    if a%2==0:
        return "its even"
    else:
        return "its odd"
result=even_odd(101)
print(result)'''


# 1. ATM Balance Check
# Write a function that takes balance and withdraw_amount.

# If withdrawal amount is less than or equal to balance, return the remaining balance.
# Otherwise, return "Insufficient balance"

'''def ATM_Balance_check(balance,amount):
    if amount<=balance:
        return(f"withdraw sucessful.the remaining amount is{balance-amount}")
    elif amount > balance:
        return("insufficent balance")
result=(ATM_Balance_check(10000,11000))
result1=(ATM_Balance_check(10000,9000))
print(result)
print(result1)
'''


# Write a function that takes the marks of 5 subjects.

# Requirements:
# Calculate the total marks.
# Calculate the average.
# If average is 40 or above → return "Pass".
# Otherwise → return "Fail".

'''def sub_marks(sub1,sub2,sub3,sub4,sub5):
    total=(sub1+sub2+sub3+sub4+sub5)/5
    if total >= 40:
        return "pass"
    else:
        return "he want to improve"
result = sub_marks(60,70,70,80,40)
print(result)
result = sub_marks(10,20,30,40,30)
print(result)'''


# Write a function that takes units consumed and calculates the electricity bill:

# First 100 units → ₹2 per unit
# Next 100 units → ₹3 per unit
# Above 200 units → ₹5 per uni

'''def ele_bill(a):
    if a<=100:
        bill = a*2
    elif a<=200:
        bill= (100*2)+((a-100)*3)
    else:
        bill=(100*2)+(100*3)+((a-200)*5)
        return bill
result1 = ele_bill(1000)
print(result1)
result2 = ele_bill(150)
print(result2)
result4 = ele_bill(10)
print(result4)'''


# Write a function that takes a number n and counts how many even numbers are present from 1 to n.
'''def count_even(a):
    # a=int(input("enter a number : "))
    count = 0
    for i in range(1,a+1):
        if i%2==0:
            # print(i)
            count+=1
        print(count)
count_even(10)'''
# print(result)
    


    # Write a function that takes a number and returns its factorial using a for loop.
'''def fact (a):
    sum = 1
    for i in range(1,a+1):
        sum = sum*i
    return sum
result=fact(9)
print(result)'''


# Write a function that takes a number and returns the number of digits
'''def count_dig(a):
    count = 0
    while a>0:
        digit = a%10
        count+=1
        a=a//10
    return count
result = count_dig(101)
print(result)'''



# Write a function that takes a number and returns its reverse
'''def rev(a):
    reversed = 0
    while a>0:
        digit = a%10
        reversed=reversed*10+digit
        a=a//10
    return reversed
result = rev(12345)
print(result)'''



#    Palindrome Checker 🔥

# Write a function that takes a number and returns:
'''def palindrome(a):
    temp = a
    original = a
    rev = 0
    while temp>0:
        # original=a
        digit = temp%10
        rev=rev*10+digit
        temp=temp//10
    # return rev
    if rev==original:
        return "its palindrome"
    else:
        return "its not palindrome"

result=palindrome(141)
print(result)'''



# Write a function that takes a number and returns whether it is prime or not
'''def prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count == 2:
        return "its prime"
    else:
        return "its odd"
result = prime(11)
print(result)'''

# Mini ATM Transaction
def mini_atm_transaction(amout,withdraw):
     
        if   withdraw <=amout :
            return f"transuction sucessful \n remaining balance is {amout-withdraw}"
        elif withdraw %100!=0:
             return "enter a amount of multiple of 100"
        else:
            return "insufficient balance"
result = mini_atm_transaction(100000,9999)
print(result)



   