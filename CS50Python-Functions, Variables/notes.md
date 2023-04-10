### Notes
CLI - commnand Line Interface

- `name = input("what's your name")`

- `print("hello,", name)`

- `print(*objects, sep=' ', end='\n', file=None, flush=False)`

`print("hello", end="")`
`print(name)`
`print("name", name, sep="???")`
`print("hello \"friend\"")`
`print('hello "friend"')`

`print(f"hello, {name}")`
`f - format`
`name = name.strip()`

`name = name.capitalize()`
`name = name.title()`

`name = name.strip().title()`

`name = input("what's your name").strip().title()`

`first, last = name.split(" ")`
`print(f"hello, {first}")`

_________
`int
`% - modulo operator` 

_________
x = float(input("what's x?"))
y = float(input("what's y?"))

z = round(x + y)

`print(f"{z:,}")` --- 1,000 (999+1) add the , to the 1000

[documentation formated string](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)



[documentation for mini languaje ](https://docs.python.org/3/library/string.html#format-specification-mini-language) 
The ',' option signals the use of a comma for a thousands separator. For a locale aware separator, use the 'n' integer presentation type instead.

`z = round(x/y, 2)` 2/3 = 0.66666666666 - 0.67

`print(f"{z:.2f}") - 0.67`

_____
hello.py

def hello(to="world"):
    print("hello", to)

hello()
name = input("what's your name?")
hello(name)
______
def main():
    name = input("what's your name?")
    hello(name)

def hello(to="world"):
    print("hello", to)
main()

-------
calculator.py

def main():
    x = int(input("What's X?"))
    print("x squared is", square(x))

def square(n):
    return n * n

def square(n):
    return n ** 2

def square(n):
    return pow (n, 2)

main()

----------
### Commands
* ls -  list all the files in your current folder
* cp - copy a file from one place to another
* mv - move a file or really rename it from one name to another
* rm - for remove, delete a file
* mkdir - make a directory that is a folder
* cd - change directories from one folder to another
* rmdir - remove a directory
* clear - clear your terminal window 
----

x = int(input("What's X?"))
y = int(input("what's is Y?"))

if x < y:
    print("x is less than y")
elif x > y:
    print("x y greater than y")
else:
    print("x is equals to y")

----
#### Or
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

-----
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

------
score = int(input("Score: "))

if score >= 90 and score <= 100
    print("Grade: A")

The same 
if 90 <= score and sore <= 100
    print("Grade: A")

if 90 <= score <= 100
    print("Grade: A")

if socore >= 90:
    print("Grade: A")
elif socore >= 80:
    print("Grade: B")
elif socore >= 70:
    print("Grade: C")
elif socore >= 60:
    print("Grade: D")
else:
    print("Grade: F")

-----
parity.py

x = int(input("what's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

----
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

### Pythonic - the way you do things in python 

def is_even(n)
    return True if n % 2 == 0 else False

def is_even(n)
    return n % 2 == 0

-----

house.py

name = input("what's is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
_________

# Loops

## while

i = 3
while i !=0:
    print("meow")
    i = i - 1

i = 1
while i <= 3:
    print("meow")
    i = i + 1

i = 0
while i < 3:
    print("meow")
    i = i + 1

i = 1
while i <= 3:
    print("meow")
    i += 1

control c -- to cancel the infinit loop.

## for

## list

for i in [0, 1, 2]:
    print("meow")

for i in range(3)
    print("meow")

if you dont use i

for _ in range(3)
    print("meow")

print("meow\n" * 3)

print("meow\n" * 3, end="")

while True:
    n = int(input("What's n?"))
    if n < 0:
        continue
    else:
        break

while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
    n = int(input("What's n?"))
    if n > 0:
        return n
    
def get_number():
    while True:
    n = int(input("What's n?"))
    if n > 0:
        break
    return n

def meow(n):
    for _ in range(n)
        print("meow")

---------

hogwarts.py

students = ["Hermione","Harry","Ron"]

print(students[0])
print(students[1])
print(students[2])

--------
students = ["Hermione","Harry","Ron"]

for student in students:
    print(student)

too criptic??
for _ in students:
    print(_)

--------

students = ["Hermione","Harry","Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

## dict

Dictionary.


students = ["Hermione","Harry","Ron","Draco"]
houses = ["Griffindore","Griffindore","Griffindore","Slytherin"]

students = {
    "Hermione":"Griffindore",
    "Harry":"Griffindore",
    "Ron":"Griffindore",
    "Draco":"Slytherin"
}
print(student["Hermione"])
print(student["Harry"])
print(student["Ron"])
print(student["Draco"])

for student in students:
    print(student, students[student],sep = ", ")

------

students = [
    {"name":"Hermimone","house":"Griffindore","patronus":"Otter"},
    {"name":"Harry","house":"Griffindore","patronus":"Stag"},
    {"name":"Ron","house":"Griffindore","patronus":"Jack Russell Terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]
for student in students:
    print(student["name"],student["house"],student["patronus"],sep=", ")

 //keyword = None

_______

mario.py

def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#",end="")
        print()

def print_square(size):
    for i in range(size):
        print("#" * size)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()


try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")









