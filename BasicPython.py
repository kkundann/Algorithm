# developed by van Rossum in 1991
# difference between Python 2 and python 3
# python 2:- print statement is not print_function
# python 3: has function and invoked with parantheses
# print ("Hello, World.")
#
# print(type('default string '))
# print(type(b'string with b '))
#
# for i in range(0,5):
#     print(i)

#python function decorator

# In Python, we can define a function inside another function.
# In Python, a function can be passed as parameter to another function (a function can also return another function

def abc(str):
    def xyz():
        return "Welcome to "
    return xyz()+str

def site(site_name):
    return site_name

print abc(site("GreeksforGeeks"))