while True:
    response = input("Do you want to play Paper, Scissors, Rock Y or N?").upper()
    if response == "N":
        print("See ya never wanna be ya")
        break
    if response == "Y":
        def statement_generator(statement, decoration):
            print(f"\n{decoration * 5} {statement} {decoration * 5}")

        def instructions():
            statement_generator("Instructions", "-")
            print('''
  Type either Scissors, Rock, or Paper
        You can tie by getting scissors scissors, rock rock, or paper paper
        You can lose by getting scissors rock, rock paper, or paper scissors
        You can also win by getting scissors paper, rock scissors, or paper rock
        Have fun or get depressed
        ''')


        want_instructions = input("Press <enter> to read the instructions "
                                  "or any key then <enter> to continue:")
        if want_instructions == "":
            instructions()

        response = input("Press enter to play")





        import random

        player_options = ("rock", "paper", "scissors", "dragon", "argentinosaurus", "jeff")
        options = ("rock", "paper", "scissors")
        running = True
        while running:
            player = None
            computer = random.choice(options)
            while player not in player_options:
                player = input('''Enter a choice (rock, paper, scissors) or try to find one of the three secret ones. 
                               The first one is what medieval people thought what dinosaurs were
                               The second is a dinosaur that starts with a
                               The third and final one is a name that starts with j : ''')
            print(f"Player: {player}")
            print(f"Computer: {computer}")
            if player == computer:
                print("It's a tie!, you barely get emotional damage, you almost have a skill issue")
            elif player == "rock" and computer == "scissors":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "paper" and computer == "rock":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "scissors" and computer == "paper":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "dragon" and computer == "scissors":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard")
            elif player == "dragon" and computer == "rock":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "dragon" and computer == "paper":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "argentinosaurus" and computer == "scissors":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "argentinosaurus" and computer == "rock":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "argentinosaurus" and computer == "paper":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "jeff" and computer == "rock":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "jeff" and computer == "scissors":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            elif player == "jeff" and computer == "paper":
                print("You win amazing, you don't get emotional damage, you don't have a skill issue, and you are also a try hard!")
            else:
                print("You lose, you failure, you get emotional damage, skill issue, l bozo, and try better!")
            if not input("Play again? (y/n): ").lower() == "y":
                running = False
        print("Thanks for playing! and see ya never wanna be ya")
        quit()