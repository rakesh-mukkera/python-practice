# Create a decorator that prints "Function started" before calling a function.
'''def simple(func):
    def hello():
        print("function started")
        func()
    return hello
@simple
def start():
    print("rakesh")
start()
'''


# Create a decorator that prints:
# Function ended
# after the decorated function finishes executing.
'''def simple(func):
    def inner_func():
        
        func()
        print("function ended")
    return inner_func
@simple
def real():
    print("hello rakesh")
real()'''


# Write a Python decorator that executes some code before and after a function call
'''def simple(fuc):
    def inner_func():
        print("before function")
        fuc()
        print("after function")
    return inner_func
@simple
def my():
    print("hello Rakesh")
my()
'''
# Write a Python decorator that counts and prints how many times a function has been called
'''# count = 0
def simple_fun(func):
    count = 0
    def inner_fun():
        nonlocal count
        count+=1
        print(f"function called {count} times")
        func()
        # count+=1
        # print("function called 3 times")
    return inner_fun
@simple_fun  
def real():
    print("hello rakesh")
    # print("function called 2 times")
real() 
real()
real()'''

# Write a Python decorator that prints the name of the function before executing it
# o/p
# Function name: calculate
# Calculating...
'''def outer_func(func):
    def inner_func():
        func()
        print(f"function name :{func.__name__}")
    return inner_func

@outer_func
def calculation():
    print("calcution....")
calculation()'''


# Write a Python decorator that prints all the arguments passed to a function before executing it
'''def outer_func(func):
    def inner_func(a,b):
        print(f"the arguments are {a},{b}")

        result = func(a,b)
        return result   
    
    return inner_func
@outer_func
def final_func(a,b):
    return a+b
print(final_func(10,20))'''


# Write a Python decorator that prints the return value of a function after the function is executed.
'''def outer_func(func):
    a = 10
    b = 20
    def inner_func(a,b):
        
        result = func(a,b)
        print(f"return value {result}")
        return result

    return inner_func
@outer_func
def main_func(a,b):
    print(a+b)
main_func(10,20)
     '''


# Write a Python decorator that converts the return value of a function into uppercase
'''def outer_func(func):
    def inner_func():
        func()
        result =func()
        return result.upper()

    return inner_func
@outer_func
def final_func():
    return"hello rakesh"
print( final_func())'''
# Write a Python decorator that doubles the return value of a function.
'''def outer_func(func):
    def inner_func():
        result = func(10)
        return result
    return inner_func
@outer_func
def number(a):
    return a+a
result1 = (number())
print(result1)'''
# number(10)
# Write the decorator so that the decorator itself doubles whatever value the function returns.
'''def outer_func(func):
    def inner_func():
        result = func()
        return result*2
    return inner_func
@outer_func
def number():
    return 10
print(number())'''

# Write a Python decorator that checks whether the return value of a function is even or odd.
'''def outer_func(func):
    def inner_func():
        result = func()
        if result % 2 == 0:
            return "its even"
        else:
            return "its odd"
    return inner_func
@outer_func
def number():
    return 101
print(number())'''

# Write a Python decorator that allows a function to execute only
#  when the given number is greater than 10.
'''def outer_num(func):
    def inner_func(n):
         
        if n > 10:
            result = func(n)
            return result
        else:
            return "the result is lessthan 10"

    return inner_func
@outer_num
def number(n):
    return n*2
print(number(11))
print(number(10))'''



