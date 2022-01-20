print(10 > 9)
print (10 == 9)
print (10 < 9)
print(bool("Hello"))
print(bool(15))
# all 0, "" will be false

class myclass():
    def _len_(self):
        return 0

myobj = myclass()
print(bool(myobj))

# isinstane() function retun a boolean value, which can be used to determine if an object is of certain data type
x = 200
print(isinstance(x, int))