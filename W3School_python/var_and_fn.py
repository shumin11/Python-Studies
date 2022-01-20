# x = "awesome"
# def myfunc():
#     print("Python is " + x)   
# myfunc()

from re import X


# x = "awesome" # global variable
# def myfunc():
#     x = "fantastic"  # only for this function
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)

# def myfunc():
#     global x    # for x inside in a function to be used globally 
#     x = "fantastic"
# myfunc()
# print("Python is " + x)

x = "awesome"
def myfun():
    global x
    x = "fantastic"   # this can change the global x
myfun()
print("Python is " + x)

