# **kwargs 
'''Real-time example
Imagine an employee function.
You don't know what information the user wants to provide:

def employee(**details):
    for key, value in details.items():
        print(key, ":", value)
employee(
    name="Rakesh",
    age=22,
    salary=30000,
    department="Python"
)
Output:
name : Rakesh
age : 22
salary : 30000
department : Python'''



# ATM transction
'''def atm(name, *transactions, **details):
    print("Customer:", name)
    print("Transactions:", transactions)
    print("Details:", details)

atm(
    "Rakesh",
    5000,
    2000,
    1000,
    account_type="Savings",
    city="Hyderabad"
)'''



# Write a function that accepts any number of product prices and returns the total price.
'''def cart(*price):
    total = 0
    for i in price:
        total+=i
    return total
print(cart(100,200,300))
'''


# Write a function that accepts:
# Student name → normal argument
# Any number of subject marks → *arg

'''def report(name,*marks):
    total = 0
    for i in marks:
        total+=i
    return f"{name}.he scored marks{total}"
result=(report('rakesh',80,60,70,80,50))
print(result)
print(report('raju',50,80,50,80,70))'''


# Write a function that accepts:
# Account holder name → normal argument
# Any number of deposit amounts → *args
# The function should calculate the total amount deposited.
def bank(name,*deposit):
    total = 0
    for i in deposit:
        total+=i
    return f"{name}:total amount in the bamk{total}"
print(bank("rakesh",2000,34345,6686,5565))