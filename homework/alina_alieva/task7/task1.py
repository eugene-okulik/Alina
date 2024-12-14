win_number = 7
while True:
    number = int(input("Input your number: "))
    if number == win_number:
        print("Congratulations! You guessed it!")
        break
    elif number != win_number:
        print("Try again")
