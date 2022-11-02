import random as r
class game:
    gesture = ["rock","paper","scissors"]
    def rps():
        state = True
        while state:
            hand = input("Player 1 enter your choice: ").lower()
            p2 = game.gesture[r.randint(0,2)]
            if hand in game.gesture:
                print(f"Player 2 used: {p2}")
                if hand == p2:
                    print("It is a tie")
                elif hand == "rock":
                    if p2 == "scissors":
                        print("You win!")
                    else:
                        print("You lose")
                elif hand == "paper":
                    if p2 == "rock":
                        print("You win!")
                    else:
                        print("You lose")
                elif hand == "scissors":
                    if p2 == "paper":
                        print("You win!")
                    else:
                        print("You lose")
            else:
                print("Input is invalid")
                state = False