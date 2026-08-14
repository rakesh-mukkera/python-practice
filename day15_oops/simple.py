# Total and Average
'''def total_avg(*args):
    total =0
    avg = 0
    for i in args:
        total+=i
    print(total)
    avg=total/len(args)
    print(avg)
total_avg(10,20,30,40,50)'''


# student details
'''def student_details(**kwargs):

    for i,j in kwargs.items():
        print(i,":",j)
student_details( name="rakesh",
    age=22,
    course="python",
    city="hyderabad")'''

# employee
'''def employee(*skills,**details):
    for i in skills:
        print(i)
    for j,k in details.items():
        print(j,":",k)
employee("python","sql","django",name="rakesh",age=22,city="hyderabad")
'''

# high salary
'''def high_sal(**salary):
    high = 0
    high_name=""
    for i,j in salary.items():
        # high = j > high

        if j > high:
         high =j
         high_name=i
        #  high==i
    print(high_name,":",high)
         
high_sal(rakesh=25000,rajul=30000,krian=28000,pavan=40000,arun=35000)
'''

# Create a decorator named calculate_time.
# Apply it to a function named addition that accepts any number of positional arguments.
# When addition() is called, the decorator should print:
# Function started
# Total = 100
# Function ended
'''def calculate_time(func):
    def addition(*args):
        print("function staryed")
        result = func(*args)
        print("function ended")
        return result
    return addition
        # print("function ended")
@calculate_time
def all(*numbers):
    sum = 0
    for i in numbers:
        sum+=i
    print(sum)
    #  print("function ended")
all(10,20,30,40,50)
'''


# Create a decorator named logger.
# Apply it to a function named employee.
# Function call
# employee(
#     "Python",
#     "SQL",
#     "Django",
#     name="Rakesh",
#     age=22,
#     city="Hyderabad"
# )

'''def outer_func(func):
    def inner_func(*args,**kwarg):
        print("function started")
        result =func(*args,**kwarg)
        print("function ended")
        return result
    return inner_func
@outer_func
def all(*args,**kwargs):
    print("skills :")
    for i in args:
        # print("skills :")
        print(i )
        # print(f"skills : \n{i}")
    print("details")
    for j,k in kwargs.items():
        print(j,":",k)
all("python","sql","django",name="rakesh",age=22,city="hyd")
'''

# Create a decorator named authenticate.

# Apply it to a function named bank_account

'''def authenticate(func):
    def bank_account(*args,**kwargs):
        pin1 = kwargs.get("pin")
        # pin = int(input("enter a pin : "))
        if pin1 !=1234:
            print("authentication is fail")
            return
        print("authentication sucessful")
        Result = func(*args,**kwargs)
        return Result
    return bank_account
@authenticate
def all(*args,**kwargs):
    print("account:",args[0])
    print("balance:",kwargs["balance"])

all("rakesh",balance=50000,pin=1234)
'''

# Create a decorator named calculate_bill
'''def calculate_bill(func):
    def inner_func(*args,**kwargs):
        result=func(*args,**kwargs)
        return result
    return inner_func
@calculate_bill
def cart(*args,**kwargs):
    total_bill=0
    print("items : ")
    for i in args:
        print(i)

    for name,price in kwargs.items():
        total_bill+=price
        # print(i)
    print(f"total_bill : {total_bill}")        
cart("laptop","laptop","mouse",laptop=5000,mouse=1000,keyboard=2000)'''

# Create a decorator named validate.
# Apply it to a function named register.
# Call:
# register(
#     "Python",
#     "SQL",
#     "Django",
#     name="Rakesh",
#     age=22,
#     city="Hyderabad"
# )
'''def name_validate(func):
    def register(*args,**kwargs):
        if len(args) < 2:
            print("2 are mandatory")
            return
        if "name" not in kwargs:
            print("namme is required")
            return
        if "age" not in kwargs or kwargs["age"] <18:
            print("age must be 18 or above")
            return
        if "city" not in kwargs:
            print("city is required")
            return
        print("registration sucessfully")
        result=func(*args,**kwargs)
        return result
    return register
@name_validate
def register1(*args,**kwargs):
    print("skills")
    for skills in args:
        print(skills)
    for key,value in kwargs.items():
         
             
        print(key,":",value)

register1("python","sql","django",name="rakesh",age=22,city="hyd")
'''



# Create a decorator named check_login.
# Use this function:
# login(username="rakesh", password="python123")
def check_login(fact):
    def inner_func(*args,**kwargs):
        username = kwargs.get("user name")
        if username ==  kwargs.get("user name") :
            print("user name is correct")
        password= kwargs.get("password")
        if len(password) >= 8:
            if password == "python123":
                print("user password is correct")
            else:
                print("password is wrong") 
        else:
            print("the condition is false")
            return
        result = fact(*args,**kwargs)
        return result
    return inner_func
@check_login
def page_login(*args,**kwargs):
    print("page")
    for password in args:
        print(password)
    for key,value in kwargs.items():
        print(key,":",value)
page_login(username="rakesh",password="python123")

        

    