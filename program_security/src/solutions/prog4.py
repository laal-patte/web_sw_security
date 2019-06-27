# Asks user to enter something, ie. a number option from a menu.
# While type != interger, and not in the given range,
# Program gives error message and asks for new input.

def get_user_input(start, end):
    loop = True  # controls while-loop
    while loop:
        try:
            user_input = int(input("Enter Your choice: "))
            if user_input > end or user_input < start:
                print("Please try again. Not in valid bounds.")
            else:
                loop = False  # aborts while-loop
        except ValueError:
            print("Please try again. Only numbers")
    return user_input

x = get_user_input(1, 6)
print(x)

#solution:
#try except for ValueError {if input not a number}.
#line 10: '>' -> '<' and '<' -> '>'
