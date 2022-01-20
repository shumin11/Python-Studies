#Multiline strings   # use three double quotes to cite a string
a = """Lorem ipsum dolor sit amet,
consectetur adispiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print (a)

# # or use three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adispiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. '''
print (a)

#STRINGS ARE ARRAYS
a = "Hello, World"
print(a[1])  #get the character at position 1

#LOOPING THROUGH A STRING
for x in "banana":
    print(x)
    
#STRING LENGTH
a = "Hello, World!"
print(len(a))

#Check if a phrase is in a string, use "in"
txt = "The best things in life are free!"
print("free" in txt) #True

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
#"not in"
txt = "The best things in life are free!"
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is Not Present")
    
b = "Hello, World!"
print(b[2:5])
# from start to position 5
print(b[:5])
# from 2 to all the way to end
print(b[2:])
# from position -5, but not included -2
print(b[-5:-2])

#String in uppercase
a = " Hello, World! "
print(a.upper())
#lower case
print(a. lower())
#remove whitespace before or after the actual text
print(a.strip())
#replace a string 
print(a.replace("H", "J"))  # replace letter"H" using "J"

#split() method splits the string into substrings if it finds instances of the separator:
print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print (c) 
c = a + " " + b
print(c)

# format()
# it takes the passed argument, formats them, and place them in the string where the placeholder {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieced of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# index number{0} can be used for placing arguments at the correct place
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."


# ESCAPE CHARACTER "\"
# WRONG txt = "We are the so-called \"Vikings\" from the north."
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#single '
txt = 'It\'s alright.' #single quote
txt = "This will inset one \\ (backslash)." # insert one \ in the sentence.
txt = "Hello\nWorld!" #换行 \n
print(txt)
txt = "Hello\rWorld!"   # \r carriage return 只输出\r后面的文字
print(txt)
txt = "Hello\tWorld!"             # \t tab
print(txt)
txt = "Hello \bWorld!"            # \b backspace
print(txt)
            # \f form feed
             # \ooo Octal value
             # \xhh  Hex value 
# capitalize() converts the first character to upper case
# casefold() converts string into lower case
# center() returns a centered string  
# count()  
# encode()
# endswith()         
# expandtabs()
# find()
# format()
# format_map()
# index()
# isalnum()
# isalpha()
# isdecimal()
# isdigit()
# isidentifier()
# islower()
# isnumeric()
# isprintable()
# isspace()
# istitle()
# isupper()
# join()
# ljust()
# lower()
# lstrip()
# maketrans()
# partition()
# replace()
# rfind()
# rindex()
# rjust()
# rpartition()
# rsplit()
# rstrip()
# split()
# splitlines()
# startswith()
# strip()
# swapcase()
# title()
# translate()
# upper()
# zfill()

            
    









