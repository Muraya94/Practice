# USING IF STATEMENTS WITH BOOLEAN VARIABLES

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male.")
elif not(is_male) and is_tall:
    print("You are not a male but are tall.")
elif is_male and not(is_tall):
    print("You are a short male.")
else:
    print("You are neither male nor tall.")

# COMPARISONS
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(943,435,4545))
