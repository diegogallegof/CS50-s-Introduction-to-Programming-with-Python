# Exceptions

"""
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

"""
"""
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an Integer")
    else:
        break
print(f"x is {x}")
"""
"""def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
"""