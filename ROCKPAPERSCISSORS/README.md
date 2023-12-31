This Python code is a simple Rock-Paper-Scissors game that allows the user to play against the computer. The game continues until the user decides to quit by typing "Q" or "q". After each round, the program displays the result and keeps track of the number of times the user and computer win.

Here's a breakdown of the code:

1. The code initializes two variables, `user_wins` and `computer_wins`, to keep track of the number of wins for the user and the computer.

2. A list named `options` contains the possible moves: "rock", "paper", and "scissors". Each move is associated with a numeric value (0, 1, 2) for later comparisons.

3. The program enters a loop, prompting the user to input their move ("rock", "paper", "scissors") or "Q" to quit.

4. If the user inputs "Q" (case-insensitive), the loop breaks, and the game ends.

5. If the user's input is not a valid move ("rock", "paper", "scissors"), the loop continues to the next iteration, prompting the user again for a valid input.

6. If the user's input is valid, the computer randomly selects its move by generating a random number between 0 and 2 (inclusive). The computer's move is retrieved from the `options` list based on the generated random number.

7. The program displays the computer's move.

8. The user's move and the computer's move are compared to determine the winner.

9. If the user wins the round, the program prints "You won!" and increments the `user_wins` counter.

10. If the computer wins the round, the program prints "You lost!" and increments the `computer_wins` counter.

11. After each round, the loop continues, allowing the user to play again.

12. Once the user decides to quit the game, the loop breaks, and the program prints the total number of times the user and the computer won.

13. The game ends with a "Goodbye!" message.

This code provides a fun and interactive Rock-Paper-Scissors game experience for the user to play against the computer.
