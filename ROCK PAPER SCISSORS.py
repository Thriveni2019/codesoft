import random
def get_user_choice():
    u_choice=input("Please enter your choice : ")
    u_choice=u_choice.upper()
    if(u_choice == "ROCK" or u_choice == "PAPER" or u_choice == "SCISSORS"):
        return u_choice
    else:
        print("please enter  choice of ROCK or PAPER or SCISSORS only ")
def get_computer_choice():
    options=["ROCK","PAPER","SCISSORS"]
    random_choice=random.choice(options)
    return random_choice
def get_winner(user_input,computer_choice):
    if(user_input == computer_choice):
        print("It's Tie")
    else:
        if((user_input == "ROCK" and computer_choice == "SCISSORS") or (user_input == "SCISSORS" and computer_choice == "PAPER") 
           or (user_input == "PAPER" and computer_choice == "ROCK")):
            return "you win"
        else:
            return "you lose"


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        print(result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        elif 'tie' in result:
            continue

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()



