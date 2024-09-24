import random

wagerChoice = [1,2,3,4,5,6]
marbles = 10
rounds = 0

print("You are playing a marble game.")
print("You have 10 marbles, we will offer a wager.")
print("You have to guess if the wager is even or odd.")
print("If the guess is correct, you get the wager amount.")
print("If you don't answer correctly, you lose the amount of marbles that was in the wager.")
print("Get 20 marbles to win!")
print("Ready? Begin!\n")

def marbleChoice():
    global wagerChoice
    global even
    global odd
    global rounds
    global marbles

    rounds = rounds + 1
    wager = random.randint(1, 6)
    evenOrOdd = input("Even or odd?").lower()
    
    if evenOrOdd == "odd" or evenOrOdd == "even":
        print(f"The wager was {wager}!")
        win = winCheck(user=evenOrOdd, wager=wager)
    else:
        print("That's an invalid input.")

def winCheck(user, wager):
    global marbles
    if (wager % 2 == 0 and user == "even") or (wager % 2 != 0 and user == "odd"):
        print(f"You won {wager} marbles!")
        marbles += wager
    else:
        print(f"You lost {wager} marbles!")
        marbles -= wager



while True:
    print("You have " + str(marbles) + " marbles!\n")
    marbleChoice()
    if marbles >= 20:
        print("You win!")
        break
    if marbles <= 0:
        print("You lose!")
        print("Time to die! :)")
        break