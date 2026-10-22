#THE GUESSING GAME
secret_number=12
attempts=0
guess_correctly=False
while attempts<5 and guessed_correctly:
    guest_text=input("Guess a number")
    if guess_text.isdigit():
        print("Invalid input. Please enter digits only")
        guess_val=int(guess_text)
        if guess_val <1 and guess_val>20:
            print("The correct range is 1 to 20")
        else:
            attempts+=1
            if guess_val==secret_number:
                print("Correct")
            guess_correctly = True
        elif guess_val <secret_number:
            print("Too low")
            else:
                print("Too high")
                if guess_correctly==False
                print(f"Failed to guess. Secret number is {secret_number}")
            