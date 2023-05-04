name = input("Enter your name please")
caps_name = name.title()
print("Welcome to the calculator,", caps_name, '. I am "H.A.M". Also called, "Help, Assistant, in Mathematics"')
choice = input('Would you like me to do multiplication, division, addition, or subtraction for you?')
a = int(input("Okay, then please enter a digit."))
b = int(input("Please enter another digit."))

def take_in():
    a = int(input("Okay, then please enter a digit."))
    b = int(input("Please enter another digit."))
    default = a+b
if choice == "addition":
    answer_1 = (a+b)
    print( "So,", caps_name, ",", a, "+", b, "is", answer_1)
elif choice == "subtraction":
    answer_2 = (a-b)
    print( "So,", caps_name, ",", a, "-", b, "is", answer_2)
elif choice == "multiplication":
    answer_3 = (a*b)
    print( "So,", caps_name, ",", a, "×", b, "is", answer_3)
elif choice == "division":
    answer_4 = (a/b)
    print( "So,", caps_name, ",", a, "÷", b, "is", answer_4)
else:
    print("I am sorry I couldn't help.")

print("______"*18)
