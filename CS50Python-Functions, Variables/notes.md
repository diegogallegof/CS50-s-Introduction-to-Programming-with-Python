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
    





