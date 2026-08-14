# Given a list of numbers, find all pairs whose sum is equal to a given target
a=[1,2,3,4,5,6,7,8,9,10,11,]
target = 15
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            print(a[i],a[j])

# Given a list of numbers, find all triplets (3 different numbers) whose sum is equal to a given target
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
target = 12
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for q in range(j+1,len(numbers)):
            if numbers[i]+numbers[j]+numbers[q] == target:
                print(numbers[i],numbers[j],numbers[q])


 

# Find all duplicate numbers using nested loops.
numbers = [4, 7, 2, 9, 5, 7, 2, 4, 9, 1]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])



# numbers = [4, 7, 2, 9, 5, 7, 2, 4, 9, 1]
# Find the frequency of every number using nested for loops.
# Expected output:
# 4 → 2
# 7 → 2
# 2 → 2
# 9 → 2
# 5 → 1
# 1 → 1
'''
numbers = [4, 7, 2, 9, 5, 7, 2, 4, 9, 1]
for i in range(len(numbers)):
    count =1
    for j in range(i+1,len(numbers)):
        
        if numbers[i]==numbers[j]:
            count+=1
    print(numbers[i],count)'''


# Separate Numbers and Strings
# separate(10, "Python", 20, "SQL", 30, "Django")

# Output:

# Numbers: [10, 20, 30]
# Strings: ["Python", "SQL", "Django"]
def separator(*args):
        numbers=[]
        strings=[]
        for value in args:
            if type(value)==int or type(value)==float:
                numbers.append(value)
            elif type(value)==str:
                strings.append(value)
        print(numbers)
        print(strings)
separator(10, "Python", 20, "SQL", 30, "Django")
# print(result)
 


# Write a function:
# def employee(name, *skills, **details):
# Call it like this:
# employee(
#     "Rakesh",
#     "Python",
#     "SQL",
#     "Django",
#     city="Hyderabad",
#     experience=1,
#     salary=30000
# )
def emp(name,*skills,**details):
    for i,j in (name,skills,details):
        # print(i)
        print(i,j)
emp( "Rakesh",
    "Python",
    "SQL",
    "Django",
    city="Hyderabad",
    experience=1,
    salary=30000)
