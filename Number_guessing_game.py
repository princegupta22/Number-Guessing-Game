import random
print("Hi Welcome to Number Guessing Game . You have 7 Chances to guess the number . Select between the number 1 to 100")
guess_number = (random.randrange(1,100))

chances = 7

guess_counter =0

while guess_counter< chances :
    guess_counter+=1
    my_guess=int(input("Enter your number: "))
    if(my_guess==guess_number):
        print(f"You Won the Game.. {guess_number} is the correct guess")
        break
    elif(guess_counter>=chances):
        print("You loss the game . Try again later")
    elif(my_guess>guess_number):
        print("Your guess is to high")
    elif(my_guess<guess_number):
        print("Your guess is to low")


