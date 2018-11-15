import random
ans = random.randint(1, 9)
while True:
    user = int(input("Guess the number :"))
    if user == ans:
        print("You have guessed the correct number! ")
        break
    elif user > ans:
        print("Choose a smaller number! ")
    elif user < ans:
        print("Choose a larger number! ")