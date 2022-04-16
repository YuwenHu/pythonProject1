from math import *
from variables import character_age
from variables import character_name
from variables import trans_character_age_into_string
# import actions_by_user.input_by_users
# import my_calculator

# show my functions on this print page!!!!!!

# print
phrase = "Hello World."
num = -8
print("switch the phrase into lower case: " + phrase.lower())
print("to judge is phrase all upper case: " + str(phrase.isupper()))
print("the length of the phrase: " + str(len(phrase)))
print("the seven th word in the phrase: " + str(phrase[6]))
# assignment: use for loop to print all the "o" in the phrase
print("find the \"o\" in the phrase: " + str(phrase.index("o")))
print("result after replace the \"Hello: " + phrase.replace("Hello", "Wave the"))
print("absolute value of the num: " + str(abs(num)))
print("3 to the power of 2: " + str(pow(3, 2)))
# do the same thing while getting smaller number by using min()
print("the bigger number between: " + str(max(3, 9)))
print("round, 四舍五入: " + str(round(6.41)))
print("floor, 向更低取整: " + str(floor(6.7)))
print("ceil, 直接chop off小数: " + str(ceil(5.8)))
print("sqrt: square root: " + str(sqrt(49)))

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("my name is: \n\"" + character_name + "\"")
print("i am " + trans_character_age_into_string(character_age) + " years old. i will be "
      + str(character_age + 1) + " in the next year.")
# print("my name is: " + actions_by_user.input_by_users.input_name(my_name))
# print(f'{numb_calculator(numb1, numb2)})

