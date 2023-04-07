
# List comprehension

# A compact way to process all or part of the elements in a sequence and return a list with the results.
# Python List comprehension provides a much more short syntax 
# for creating a new list based on the values of an existing list.

#Advantages of List Comprehension
"""
 - More time-efficient and space-efficient than loops.
 - Require fewer lines of code.
 - Transforms iterative statement into a formula.
 """
# Syntax of  List Comprehension
"""
newList = [ expression(element) for element in oldList if condition ] 
"""
# ----------------------------------------------------------------
# Example 1: Iteration with List comprehension
# Using list comprehension to iterate through loop
# ----------------------------------------------------------------
List = [character*2 for character in ["x", 2, 3]]
# Displaying list
print(List)
# Output
# [xx, 4, 6]
# ----------------------------------------------------------------
# Example 2: Even list using list comprehension
# ----------------------------------------------------------------
list = [i for i in range(11) if i % 2 == 0]
print(list)
# Output
# [0, 2, 4, 6, 8, 10]

result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]
print (result)
# Output
# ['0000', '0002', '0004', '0006', 
"""
En Python, este código utiliza el método format() de cadenas 
para dar formato a un número x en hexadecimal con un ancho mínimo de 4 caracteres, 
usando ceros a la izquierda como relleno.

La cadena de formato '{:#04x}' especifica el formato deseado:

# indica que se debe incluir el prefijo "0x" antes del número hexadecimal.
0 indica que se deben usar ceros a la izquierda como relleno.
4 indica el ancho mínimo del campo, que en este caso es de 4 caracteres.
x indica que se debe formatear el número en formato hexadecimal.
Por lo tanto, si x es un número entero en Python, como 10, el código dará como resultado la cadena '0x0a', que es la representación hexadecimal de ese número con un ancho mínimo de 4 caracteres.
"""

# ----------------------------------------------------------------
# Example 3: Matrix using list comprehension
# ----------------------------------------------------------------
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
# Output
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
D3 = [[[j for j in range(3)] for i in range(3)] for z in range(5)]
print(D3)
# Output
# [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], 
#  [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
print("mat")
mat = [[j for j in range(3)]*3 for i in ["x",2,3]]
print(mat)
# Output [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# Output [[0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2]]

# ---------------------------------------------------------------
# List Comprehensions vs For Loop
# ---------------------------------------------------------------
# There are various ways to iterate through a list. 
# However, the most common approach is to use the for loop. 
# Let us look at the below example:

# Empty list
List = []
# Traditional approach of iterating
for character in 'Geeks 4 Geeks!':
	List.append(character)
# Display list
print(List)
# Output ['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's', '!']
"""
Above is the implementation of the traditional approach to 
iterate through a list, string, tuple, etc. Now list comprehension 
does the same task and also makes the program more simple. 

List Comprehensions translate the traditional iteration approach
using for loop into a simple formula hence making them easy to use. 
Below is the approach to iterate through a list, string, tuple, etc. 
using list comprehension.
"""
# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']
# Displaying list
print(List)
# Output ['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's', '!']


# Flatten a list
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list = [item for sublist in l for item in sublist]
print(flat_list)
# Which means
flat_list_x = []
for sublist in l:
    for item in sublist:
        flat_list_x.append(item)
print (flat_list_x)

print (item)
listita = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list_y = [item for y in listita]
print(flat_list_y)


# Chat GPT Example
def is_valid_input(inputx):
    # Function to check if the input is valid
    return str(inputx).isdigit() and int(inputx) >= 0

def is_valid_size(size):
    # Function to check if the size is valid
    return size in ["small", "medium", "large"]

def is_valid_color(color):
    # Function to check if the color is valid
    return color in ["red", "green", "blue"]

inputx = 9
size = "largex"
color = "green"


# valid_input = all([condition(inputx, size, color) for condition in [is_valid_input(inputx), is_valid_size(size), is_valid_color(color)]])
valid_input = [condition for condition in [is_valid_input(inputx), is_valid_size(size), is_valid_color(color)]]
print(valid_input)
if valid_input:
    print("Valid input")
else:
    print("Invalid input")

valid_input = all([condition for condition in [is_valid_input(inputx), is_valid_size(size), is_valid_color(color)]])
print(valid_input)
if valid_input:
    print("Valid input")
else:
    print("Invalid input")

# Output TypeError: is_valid_input() takes 1 positional argument but 3 were given

# check if a string is alphanumeric

string_random = "hello world !"
ans = string_random.isalnum()
print(ans)

# check the len for a string
le = len("")
print(le)

def max_min(s):
    return 2 <= len(s) <=6

print(max_min("hc8976"))


def is_two_char(s: str):
    if len(s) >= 2:
        return (s[0].isalpha() and s[1].isalpha())
    return False

print(is_two_char("A"))

def my_function(parameter: str) -> int:
    """ do something with the parameter docstring """
    parameter = 2
    return parameter
print(my_function("a"))

# slicing notation

a = "990"

l = len(a)

b = not(a[:l-1:].isdigit())

print(b)



def is_zeroX(s: str):
    i = s.find("0")
    return i == -1 and s[:i].isnumeric()

print(is_zeroX("CS50"))

def is_zero(s: str):
    i = s.find("0")
    # si el indice es -1 entonces no hay ceros 
    if i != -1:
        # como hay cero, dime si las letras anteriore al cero son numeros
        print("IS DIGIT: "+str(s[:i:]))
        if(s[:i:].isdigit()):
            print(s[:i:])
            return True
        else:
            return False
    # si no hay ceros retorne verdadero
    else:
        return True
print(is_zero("CS50"))



print("CS5".isdigit())
print("CS5".isnumeric())

def is_zeroZ(s: str):
    a = ""
    for char in s:
        if char.isdigit():
            a = char
            break
    if a == "0":
        return False
    return True

print(is_zeroZ("CS50"))
    
def is_middle(s: str) -> bool:
    l = len(s)
    ans = True
    if l > 2:
        # AA i
        # AA Ai
        # AA ii
        # AA AAi
        # AA Aii
        # AA iii
        # AA AAAi
        # AA AAii
        # AA Aiii
        # AA iiii
        # AA 
        # AA iAi - l == 5
        # AA iAAi - l == 6
        # AA iAii
        # AA iiAi
        # AA AiAi
        
        if s[l-1].isalpha():
            for char in s:
                if char.isdigit():
                    ans = False
                    break
        elif l == 5 or l == 6:
            for i in range(2, l-1):
                if s[i].isdecimal() and s[i+1].isalpha():
                    ans = False
                    break
        return ans 
print("----------------------------------------------------------------")
print(is_middle("A8a9a9"))
#comment

def f():
    table = {
        "apple":130,
        "avocado":50,
        "banana":110,
        "cantaloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwifruit":90,
        "lemon":15,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80,
        "lime":20
    }
#If k is a str and d is a dict, you can check whether k is a key in d with code like:
#if k in d:
    food = str(input("Item: ")).lower()
    if food in table:
        print("Calories: ",table[food])

nums = [4, 2, 6, 8, 9, 10]
a = nums[4]-6
b = nums[1]-2
print(a,b)
print(nums[a:b:-1])

# Exceptions
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an Integer")
    else:
        break
print(f"x is {x}")
