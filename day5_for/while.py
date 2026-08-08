# wap to find the sum of integers present in the given list?
# wap to print all the float numbers from the given tuple only if it is present in odd index.
# wap to reverse a string with out slicing or type casting
# wap to find the product of all the folat numbers present at odd index in a given list.
# wap to replace a specifice character with user enter character.


# numbers = eval(input("enter a list")) 
'''i = 0 
total = 0 
while i < len(numbers): 
    total += numbers[i] 
    i += 1 
print("Sum =", total)

'''
# wap to print all the float numbers from the given tuple only if it is present in odd index.
t = (10.5,2.53,'hello',10+3j,'while',22.7)

i = 0
while i < len(t):
    if i % 2 != 0 and type(t[i]) == float:
        print(t[i])
    i += 1



    # wap to reverse a string with out slicing or type casting
str1 = input("enter a string : ")
a = len(str1)-1
while  a>=0:
    print(str1[a],end="")
    a-=1



# wap which converts each and every word 1st character  uppercase and remaning character to lower case
# wap to split all the words from the string with out using the split method
# wap to remove the duplicate elements from the list
# reverse a number with out type casting
