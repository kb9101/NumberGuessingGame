import random
computerNumber = random.randint(1,50)
userNumber = int(input("Enter your guess between 1 and 50 : "))
while True:
    if userNumber == computerNumber:
        print("You've made the right guess!")
        break

    elif userNumber < computerNumber:
        print("Your guess number is smaller than the original number! Please try again!")
        userNumber = int(input("Enter your guess between 1 and 50 : "))

    elif userNumber > computerNumber:
        print("Your gurss number is greater than the original number! Please try again!")
        userNumber = int(input("Enter your guess between 1 and 50 : "))