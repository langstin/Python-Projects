import random

n = random.randint(1, 100)
c = 0

while True:
    c += 1
    a = int(input("Guess the number: "))
    if a == n:
        print(f"Correct! You got it in {c} guesses")
        break
    elif a < n:
        print("Too low")
    else:
        print("Too high")
