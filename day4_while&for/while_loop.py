# Write a Python program to print all multiples of 7 up to a given number.
'''num = int(input("enter a number : "))
i = 1
while i <= num:
    if i % 7 == 0:
        print(i)
    i+=1'''


# Write a Python program to count the number of even digits and odd digits in a given number.
'''num = int(input("enter a number : "))
even_count = 0
odd_count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count +=1
    else:
        odd_count+=1
    num = num//10
print('even',even_count)
print(odd_count)'''



# Write a Python program to find the largest digit in a given number.
'''num = int(input("enter a number : "))
largest = 0
while num > 0:
    digit = num%10
    if digit > largest:
        largest = digit
    num = num //10
print("largest digit:",largest)'''



    #  Write a Python program to find the smallest digit in a given number

''''num = int(input("enter a number : "))
smallest = num
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10
print("smallest number : ",smallest)
    '''

# Print numbers from 1 to 20.
# num = 0
# while num <= 20:
#     print(num)
#     num+=1




# Print numbers from 20 to 1 using a while loop
num = 20
while num >= 0:
    print(num)
    num-=1



# Print all even numbers from 1 to 50 using a while loop.
n = 1
while n <= 50:
    if n % 2 == 0:
        print(n)
    n+=1



# Print all odd numbers from 1 to 50 using a while loop
n = 1
while n <= 50:
    if n% 2 != 0:
        print(n)
    n+=1




    # Find the sum of numbers from 1 to 100 using a while loop
num = 1
total = 0
while num <= 100:
     
    total +=num
    num+=1
print(total)


# Find the product of numbers from 1 to 10 using a while loop
num =1
total = 1
while num <= 10:
    total*= num
    num+=1
print(total)



# Count how many numbers are divisible by 3 between 1 and 100 using a while loop.
count = 0
i = 1
while i <= 100:
    if i% 3 == 0:
        count+=1
    i+=1
print(count)



# Find the sum of all even numbers from 1 to 100 using a while loop.
num = 0
total = 0
while num <= 100:
    if num% 2 == 0:
         total = total+num
    num+=1
print(total)






# Find the sum of all odd numbers from 1 to 100 using a while loop.
num = 0
total = 0
while num <= 100:
    if num % 2 !=0:
        total= total+num
    num+=1
print(total)



# Print the multiplication table of a given number using a while loop.
'''num = int(input("enter a number : "))
a = 0
while a<= 10:
    print(f"{num} x {a} = {num*a}")
    a+=1
'''

    # Count the number of digits in a number using a while loop.
num = int(input("enter a number : "))
count1 = 0
while num > 0 :
    num = num//10
    count1 +=1
     
print(count1)