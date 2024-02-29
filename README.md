# Paper, Cross, Rock Game

This simple console-based Python game involves two players. Each player can choose from three options: **Paper**, **Cross**, or **Rock**. The game determines the winner based on the choice each player makes. The game continues until the players decide to stop.

### Instructions

1. Run the Python code.
2. Enter your choice when prompted (either `Paper`, `Cross`, or `Rock`).
3. The computer will randomly select a choice for Player 2.
4. The program will determine the winner and display the result.
5. You can choose to play again.

### Game Logic

The game logic is implemented in the `paper_cross_rock` function. It determines the winner based on the choices made by both players. The function returns the result as a string.

### Getting Player Choice

The `get_player_choice` function is used to prompt players to enter their choice. It validates the input and ensures it's one of the valid choices (`Paper`, `Cross`, or `Rock`). If it's not valid, the player is prompted to enter a valid choice.

### Playing the Game

The main game loop is executed in the `play_game` function. It continues until the players decide to stop. After each round, the scores are displayed, and the players can choose to play again or exit the game.

### Running the Game

To run the game, execute the Python script. After each round, you will be asked if you want to play again. To exit the game, enter 'n' when prompted.

```bash
$ python paper_cross_rock.py
```
