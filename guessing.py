import random
number = random.randint(1,100)
attempt = 0
while True:
    num = int(input("Guess the number between 1 and 100: "))
    attempt += 1
    if attempt<=7:
        if num == number:
            word = "attempt" if attempt == 1 else "attempts"
            print(f"You got that right, Number:{number} in your {attempt} {word}")
            break
        elif num<number:
            print("Too Low!")
        else:
            print("Too High!")
    else:
        print(f"Game Over! Number:{number}")
        break
