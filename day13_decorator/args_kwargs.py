# Create a function add() that accepts two numbers and prints their sum
'''def add(a,b):
    return a+b
result = add(10,20)
print(result)'''


# Create a function display() that accepts name and age and prints both.
'''def details(name,age):
    return (name,age)
result =details("rakesh",22)
print(result)'''


# display the employee details
'''def employee(name,age,salary,department):
    return (name,age,salary,department)
result=employee("rakesh",age=22,salary=25000,department="techinical support")
print(result)'''



# def test(*args):
#     print(args)

# *args collects multiple positional arguments into a tuple

'''def test(*args):
    return args
print(test(10,20,30,30))'''


# def total(*args):

# and calculate the total of all numbers without using sum()
'''def total(*args):
    sum = 0
    for i in args:
        sum = i+sum
    print(sum)
total(10,20,30,40,50)'''


# def student(name, *marks):
# Call:
# student("Rakesh", 80, 90, 70, 85)
# The function should print:
# Name: Rakesh
# Marks: (80, 90, 70, 85)
# Total: 325
# Average: 81.25
'''def marks(name,*marksall):
    print(f"name :{name}")
    print(f"marks :{marksall}")
    sum = 0
    for i in marksall:
        sum+=i
    print(sum)
    count = 0
    for i in marksall:
        count+=1
        avg = sum/count
    print(avg)
marks("rakesh",100,90,80,70,60)
'''

# def details(**kwargs):
# Call:
# details(
#     name="Rakesh",
#     age=22,
#     course="Python",
#     city="Hyderabad"
# )
'''def details(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i, j in kwargs.items():
        # for j in i:
     print(i,":",j)
details(name="rakesh",age=22,course="python",city="Hyderabad")

# '''
# def employee(**details):
# Call it like this:
# employee(
#     name="Rakesh",
#     age=22,
#     salary=30000,
#     department="IT",
#     experience=1
# )
'''def employee(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)
employee(name="rakesh",age=22,salary=30000,department="it",experience=1)
'''

# def employee(name, *skills, **details):
# Call it like this:
# employee(
#     "Rakesh",
#     "Python",
#     "SQL",
#     "Django",
#     age=22,
#     salary=30000,
#     city="Hyderabad"
# )
'''def employee(name,*skills,**details):
    print(f"name :{name}")
    print(skills)
    for i,j in details.items():
        print(i,":",j)
employee ("rakesh","python","sql","django",age=22,salary=30000,city="Hyderabad")
'''
