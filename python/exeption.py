import sys

try:
    x = int(input("input for x : "))
    y = int(input("input for y : "))
except ValueError :
    print("harus integer ngabs")
    sys.exit(1)

try :
    result = x / y
except ZeroDivisionError:
    print("error bego, mana bisa di bagi ama 0")
    sys.exit(1)

print(f"{x} / {y} = {result}")