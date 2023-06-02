while True:
    user_guess = int(input("When was Python 1.0 released? "))
    if user_guess > 1994:
        print("It was earlier than that!")
    elif user_guess < 1994:
        print("It was later than that!")
    else:
        print("Correct!")
        break