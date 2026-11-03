# PS No. 56 - Tic-Tac-Toe 
# Language: Python 3
# Concepts:  Lists, Functions, Conditions, Game Logic 
# Name: shivanshu tiwari
# Class: BCA 1C
# ERP No.: RU-26-02255
"""
PS No. 56 - Tic-Tac-Toe (Two-Player Console Game)
Language : Python 3
Concepts : Lists, Functions, Conditions, Game Logic

How the game works:
  1. Two players take turns on a 3 x 3 board. Player X always plays first.
  2. Each player types a position from 1 to 9 to place their mark.
  3. The board is shown after every move.
  4. The game ends when a player gets 3 in a line (win) or the board
     is full (draw). Then the program asks "Play again? (y/n)".

Positions on the board are numbered 1 to 9:

     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
"""

# ---------------------------------------------------------------------------
# Winning lines
# ---------------------------------------------------------------------------
# A player wins if they own all 3 positions of any one of these 8 lines.
# Positions are written as 1-9 (the numbers the players see on the board).
WINNING_LINES = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),   # 3 rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),   # 3 columns
    (1, 5, 9), (3, 5, 7),              # 2 diagonals
]


# ---------------------------------------------------------------------------
# Board functions
# ---------------------------------------------------------------------------
def create_board():
    """Return a new empty board: a list of 9 cells."""
    # The board is a list with 9 items. Index 0 is position 1, index 8 is
    # position 9. A blank space " " means the cell is empty.
    return [" "] * 9


def display_board(board):
    """Print the board. Empty cells show their position number."""
    # Build a list of 9 labels: the mark (X/O) if the cell is taken,
    # otherwise the position number, so players know what to type.
    cells = []
    for index in range(9):
        if board[index] == " ":
            cells.append(str(index + 1))   # index 0 -> shows "1", and so on
        else:
            cells.append(board[index])     # shows "X" or "O"

    # Print the 3 rows with separator lines in between
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


# ---------------------------------------------------------------------------
# Taking a move
# ---------------------------------------------------------------------------
def get_move(board, player):
    """Ask the current player for a move until a valid one is entered.

    Returns the chosen position as a number from 1 to 9.
    """
    # Keep asking until the player gives a valid position.
    # An invalid input never ends the loop, so the turn does not change.
    while True:
        text = input(f"Player {player}, enter position (1-9): ").strip()

        # Check 1: the input must be a whole number (rejects "abc", "", "1.5")
        try:
            position = int(text)
        except ValueError:
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        # Check 2: the number must be between 1 and 9 (rejects 0, 10, -3)
        if position < 1 or position > 9:
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        # Check 3: the cell must be empty (rejects an already taken position)
        if board[position - 1] != " ":
            print(f"Position {position} is already taken. Choose another position.")
            continue

        # All checks passed, so this is a valid move
        return position


def make_move(board, position, player):
    """Place the player's mark on the board."""
    # Position 1-9 is stored at list index 0-8, so subtract 1
    board[position - 1] = player


# ---------------------------------------------------------------------------
# Win and draw checks
# ---------------------------------------------------------------------------
def check_win(board, player):
    """Return the winning line (tuple) if the player has won, else None."""
    # Go through all 8 winning lines. If the player's mark is on all
    # 3 positions of a line, that player has won.
    for line in WINNING_LINES:
        a, b, c = line
        if board[a - 1] == player and board[b - 1] == player and board[c - 1] == player:
            return line      # e.g. (1, 2, 3), used to print the winning line
    return None              # no winning line found


def check_draw(board):
    """Return True if every cell is filled."""
    # If there is no empty cell left, the board is full.
    # This is only called after check_win, so a full board here means a draw.
    return " " not in board


# ---------------------------------------------------------------------------
# One full game
# ---------------------------------------------------------------------------
def play_game():
    """Play one full game of Tic-Tac-Toe."""
    board = create_board()        # fresh empty board for every new game
    current_player = "X"          # X always starts
    moves_played = 0              # counts valid moves (maximum is 9)

    display_board(board)

    while True:
        # 1. Get a valid move and place it on the board
        position = get_move(board, current_player)
        make_move(board, position, current_player)
        moves_played += 1
        display_board(board)

        # 2. Check for a win first (a win on the 9th move is still a win)
        winning_line = check_win(board, current_player)
        if winning_line:
            print(f"Player {current_player} wins!")
            print("Winning line: " + "-".join(str(p) for p in winning_line))
            return

        # 3. No winner, so check if the board is full (draw)
        if check_draw(board):
            print(f"Board is full after {moves_played} moves.")
            print("It's a draw! No moves left.")
            return

        # 4. Game continues: switch turn only after a valid move
        current_player = "O" if current_player == "X" else "X"


# ---------------------------------------------------------------------------
# Play again and main program
# ---------------------------------------------------------------------------
def ask_play_again():
    """Ask 'Play again? (y/n)' until the answer is y or n."""
    while True:
        # .lower() accepts both "y" and "Y" (and "n" and "N")
        answer = input("Play again? (y/n): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please enter y or n.")      # any other answer: ask again


def main():
    """Show the welcome message and keep playing until the players stop."""
    print("=" * 34)
    print("        TIC-TAC-TOE GAME")
    print("=" * 34)
    print("Two players: X goes first, then O.")
    print("Enter a position from 1 to 9 to play.")

    try:
        # Play games one after another until the players answer "n"
        while True:
            play_game()
            if not ask_play_again():
                break
            print()
    except EOFError:
        # Happens when no more input is available (used by the test cases)
        print("\nNo more input. Game stopped.")
        return
    except KeyboardInterrupt:
        # Happens when the user presses Ctrl + C
        print("\nGame stopped.")
        return

    print("Thanks for playing!")


# Run main() only when this file is run directly (python tic_tac_toe.py).
# When a test file imports this file, main() does not start by itself.
if __name__ == "__main__":
    main()