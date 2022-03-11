# Python

print("Hello World!")
print("\n")
print("    /\\")
print("   /  \\")
print("  /    \\")
print(" /      \\")
print("/________\\")
print("\n")


character_name = "the man"
character_activity = "gardening"
print(character_name.title() + " was " + character_activity + ".")
print(character_name.title() + " was " + character_activity.replace("garden", "look") + ".")
print("\n")


judah_s_age = 37
print("Judah is " + str(judah_s_age) + " years old.")
print("\n")
family_names = ["Israel", "Leah", "Reuben", "Joseph"]
family_ages = [54, 44, 29, 24]
family_ages[2] = 30
print(str(family_names[0]) + " is " + str(family_ages[0]) + " years old.")
print(str(family_names[1]) + " is " + str(family_ages[1]) + " years old.")
print(str(family_names[2]) + " is " + str(family_ages[2]) + " years old.")
print(str(family_names[3]) + " is " + str(family_ages[3]) + " years old.")
print("\n")


import math
print(round(4.5))
print(math.ceil(4.5))
print(math.floor(4.5))
print("\n")
def say_hi():
    print("Hello User!")

say_hi()


def say_hi(name):
    print("Hello " + name)


say_hi("Milcah")
say_hi("Ben")
print("\n)


def cube(num):
    return num ** 3


print(cube(2))

result = cube(5)
print(result)


def square(integer):
    print(integer ** 2)


square(4)
print("\n")


is_male = False
is_tall = False

if is_male and is_tall:
    print("You are an alpha.")
elif not is_male and not is_tall:
    print("You are cute!")
elif is_male and not is_tall:
    print("You know what it means to get ahead with effort.")
else:
    print("You are svelte...")
print("\n")


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3 and num2 > num1:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    elif num1 > num2 and num1 == num3:
        print(num1 + num3)
    else:
        print(num2)


max_num(3, 998, 3)
print("\n")


i = 1
while i <= 10:
    print(i)
    i += 1

print("End of loop.")
print("\n")


# my_name = "Rumplestiltskin"
# guess = ""
# guess_count = 0
# guess_limit = 3
# max_guess = False
#
# while guess != my_name and not max_guess:
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count += 1
#     else:
#         max_guess = True
#
# if max_guess:
#     print("Out of guesses, your baby is mine!")
# else:
#     print("Nooooo! How did you guess ittt! ***POOF!***")


def raise_to_power(base_num, pow_num):
    exp_result = 1
    for number in range(pow_num):
        exp_result = exp_result * base_num
    print(result)


raise_to_power(5, 3)
print("\n")


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

for element in number_grid:
    for each in element:
        print(each)
print("\n")


def pig_latin(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + letter + "p" + letter
        else:
            translation = translation + letter
    return translation


print(pig_latin("To be or not to be, that is the question."))
print("\n")


import random


def hogwarts_sorting():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    return random.choice(houses)

print(hogwarts_sorting())
print("\n")


class Chef:
    def special(self):
        print("The chef is preparing your fried chicken.")

    def vegan(self):
        print("The chef is preparing your tofu salad.")

    def rice(self):
        print("The chef is preparing your fried rice.")


class ChineseChef(Chef):
    def special(self):
        print("The chef is preparing your kung pao chicken.")

myChef = Chef()
myChineseChef = ChineseChef()

myChef.special()
myChineseChef.special()
print("\n")
