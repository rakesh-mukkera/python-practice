# Print numbers from 1 to 10.

# a = 1
# while a <= 10:
#     print(a)
#     a +=1


# Print numbers from 10 to 1 using a while loop.
# a = 10
# while a >= 1:
#     print(a)
#     a -=1


# Print all even numbers from 2 to 20 using a while loop.
# a= 2
# while a <=20:
#     print(a)
#     a+=2



# Print all odd numbers from 1 to 19 using a while loop.
# a=1
# while a<=19:
#     print(a)
#     a+=2


# Print the word "Python" 5 times using a while loop.

# a = 1
# while a <= 5:
#     print("python")
#     a+=1

# Print all numbers between 50 and 60 using a while loop.
# a= 50
# while a <= 60:
#     print(a)
#     a+=1

# Print all numbers divisible by 3 from 1 to 30 using a while loop.
# a = 3
# while a<=30:
#     print(a)
#     a+=3



# Print the squares of numbers from 1 to 10 using a while loop.
# a = 1
# while a <= 10:
#     print(a*a)
#     a+=1



# Print the cubes of numbers from 1 to 5 using a while loop.

# a = 1
# while a <=5:
#     print(a**3)
#     a+=1


# Print the multiplication table of 8 using a while loop.
# a = 1
# while a <= 10:
#     print(a*8)
#     a+=1


# Find the sum of numbers from 1 to 100 using a while loop.
# a = 1
# total = 0
# while a <= 100:
#     total +=a 
#     a+=1
# print("sum =",total)

# Find the sum of all even numbers from 1 to 50 using a while loop.
# a=1
# even_sum = 0
# while a<=50:
     
#     if a % 2 == 0:
#      even_sum += a    
    
#     a+=1
# print(even_sum)
    


# Find the sum of all odd numbers from 1 to 50 using a while loop.
# a = 1
# odd_sum = 0
# while a <= 50:
#     if a%2 != 0:
#       odd_sum+=a
#     #   print(odd_sum)
#     a+=1
# print(odd_sum)

# Find the factorial of a number entered by the user using a while loop.

# a = 1
# b = 0
# while a <= 5:
#     # a*a
#     b+=a*a
#     a+=1
# print(b)

# num = 5
# a = 1
# b = 1
# while b <= num:
#     a*=b
#     a+=1
# print(a)
# # print(5**3)


# Find the sum of digits of a number.
# a= 1
# b =0
# while a<=10:
#     b+=a
#     a+=1
# print(b)


num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print(count)