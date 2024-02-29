import random

# Game logic
def paper_cross_rock(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"

    if (player1_choice == 'Paper' and player2_choice == 'Cross') or \
       (player1_choice == 'Cross' and player2_choice == 'Rock') or \
       (player1_choice == 'Rock' and player2_choice == 'Paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Get player choice
def get_player_choice(player_num):
    while True:
        if player_num == 2:
            bot_choices = ['Paper', 'Cross', 'Rock']
            player_choice = random.choice(bot_choices)
            print(f"Player 2 chooses {player_choice}")
        else:
            player_choice = input(f"Player {player_num}: Please choose Paper, Cross, or Rock: ").strip().title()
            if player_choice not in valid_choices:
                print("Invalid input. Please choose from Paper, Cross, or Rock.")
            else:
                return player_choice
        return player_choice


# Check if the player wants to play again
def play_again():
    return input("Do you want to play again? (y/n): ").strip().lower() == 'y'

# Main game loop
def play_game():
    player_scores = {"Player 1": 0, "Player 2": 0}
    
    while True:
        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)
        
        result = paper_cross_rock(player1_choice, player2_choice)
        print(result)
        
        if result == "Player 1 wins!":
            player_scores["Player 1"] += 1
        elif result == "Player 2 wins!":
            player_scores["Player 2"] += 1
            
        print(f"Scores: {player_scores}")

        if not play_again():
            break

# Valid choices
valid_choices = ['Paper', 'Cross', 'Rock']

# Run the game
play_game()
print("Thanks for playing!")
