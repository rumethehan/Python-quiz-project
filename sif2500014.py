print("welcome to quiz game")

name = input("enter your name:")
print("Hello", name)
print("Let's start the quiz!")

score = 0

Q1 = input("1. what is the capital of Sri Lanka? ")

if Q1.lower() == "colombo":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Q2 = input("2. 150 + 170 = ")

if Q2 == "320":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Q3 = input("3. what is the highest mountain in sri lanka? ")

if Q3.lower() == "piduruthalagala":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Q4 = input("4. what is the national animal of Sri Lanka? ")

if Q4.lower() == "lion":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

print("Your score is:", score)

if score == 4:
    print("Excellent")
elif score == 3:
    print("Good job")
elif score == 2:
    print("Not bad")
else:
    print("Try again")
