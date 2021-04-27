# Problem :
# Task : Estimating the risk of death from coronavirus. Write a program that;
# Takes "Yes" or "No" from the user as an answer to the following questions :
# Are you a cigarette addict older than 75 years old? Variable → age
# Do you have a severe chronic disease? Variable → chronic
# Is your immune system too weak? Variable → immune
# Set a logical algorithm using boolean logic operators (and/or) 
# and use if-statements with the given variables 
# in order to print out us a message : 
# "You are in risky group"(if True ) or "You are not in risky group" (if False).
# age =  # can be assigned only True/False
# chronic =  # can be assigned only True/False
# immune =  # can be assigned only True/False
# risk = ?

# "You are in risky group"(if True ) or "You are not in risky group" (if False).
# age =  # can be assigned only True/False
# chronic =  # can be assigned only True/False
# immune =  # can be assigned only True/False
# risk = ?

# print("Please enter (Y) for YES or (N) for NO for the following questions.\n")
# age = input("Are you a cigarette addict older than 75 years old? Yes/No : ")
# chronic = input("Do you have a severe chronic disease? Yes/No : ")
# immune = input("Is your immune system too weak? Yes/No : ")
# age1=age.lower()
# chronic1=chronic.lower()
# immune1=immune.lower()
# if age1[0] == "y" and chronic1[0] == "y" and immune1[0] == "y":
#   print("You are in risky group")
# else:
#   print("You are NOT in risky group")

print("Please enter Yes or No for the following questions\n")
age = input("Are you a cigarette addict older than 75 years old? Yes/No : ")
chronic = input("Do you have a severe chronic disease? Yes/No : ")
immune = input("Is your immune system too weak? Yes/No : ")
age=age.lower()
chronic=chronic.lower()
immune=immune.lower()

if age == "yes" and chronic == "yes" and immune == "yes":
    print("You are in risky group")

elif immune == "yes" and (age == "yes" or chronic == "yes"):
    print("You are in risky group")
elif age == "yes" and (chronic == "yes" or  immune == "yes"):
    print("You are in risky group")
elif chronic == "yes" and (age == "yes" or  immune == "yes"):
    print("You are in risky group")

elif age == "no" and chronic== "no" and immune == "no":
    print("You are NOT in risky group")

elif immune == "no" and (age == "no" or chronic == "no") :
    print("You are NOT in risky group")
elif age == "no" and (chronic == "no" or  immune == "no"):
    print("You are NOT in risky group")
elif chronic == "no" and (age == "no" or  immune == "no"):
    print("You are NOT in risky group")

else:
    print("Something wrong, program will be closed. ")
