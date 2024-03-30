from queue import PriorityQueue

def is_goal_state(state):
    """Check if no two queens attack each other."""
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            # Check if queens are in the same row or on the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                return False
    return True

def get_successors(state):
    """Generate all possible successor states by moving each queen to a new row in its column."""
    successors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if j != state[i]:
                # Generate a new state by moving queen i to row j
                new_state = list(state)
                new_state[i] = j
                successors.append(tuple(new_state))
    return successors

def heuristic(state):
    """Calculate the heuristic value based on pairs of queens attacking each other."""
    h = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                h += 1
    return h

def print_board(state):
    """Print the board state."""
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def a_star_search(initial_state, verbose=False):
    """Perform the A* search algorithm with optional verbose output."""
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), initial_state))
    visited = set()

    while not frontier.empty():
        _, current_state = frontier.get()

        if verbose:
            print_board(current_state)

        if is_goal_state(current_state):
            return current_state

        visited.add(current_state)

        for successor in get_successors(current_state):
            if successor not in visited:
                frontier.put((heuristic(successor), successor))

    return None  # No solution found

# Example usage
initial_state = (0, 2, 4, 1, 3, 5, 7, 6)  # A more complex starting state
print("Starting from initial state:")
print_board(initial_state)
print("Searching for a solution...\n")
solution = a_star_search(initial_state, verbose=True)
if solution:
    print("Final solution found:")
    print_board(solution)
else:
    print("No solution found.")




import tkinter as tk
import time
from queue import PriorityQueue

# Constants for GUI
CELL_SIZE = 50
DELAY = 0.5  # Delay between each state display (in seconds)

def draw_board(canvas, state):
    """Draw the board state on the canvas."""
    canvas.delete("all")
    n = len(state)
    for row in range(n):
        for col in range(n):
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(col * CELL_SIZE, row * CELL_SIZE,
                                    (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE,
                                    fill=color, outline="")
            if state[col] == row:
                canvas.create_text((col + 0.5) * CELL_SIZE, (row + 0.5) * CELL_SIZE,
                                   text="Q", font=("Arial", 20))

def animate_search(canvas, initial_state):
    """Animate the A* search algorithm."""
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), initial_state))
    visited = set()

    while not frontier.empty():
        _, current_state = frontier.get()

        draw_board(canvas, current_state)
        root.update()  # Update the GUI

        time.sleep(DELAY)

        if is_goal_state(current_state):
            return current_state

        visited.add(current_state)

        for successor in get_successors(current_state):
            if successor not in visited:
                frontier.put((heuristic(successor), successor))

    return None  # No solution found

# Initialize GUI
root = tk.Tk()
root.title("N-Queens Solver")

canvas = tk.Canvas(root, width=CELL_SIZE * 8, height=CELL_SIZE * 8)
canvas.pack()

# Example usage
initial_state = (0, 2, 4, 1, 3, 5, 7, 6)  # A more complex starting state
print("Starting from initial state:")
print_board(initial_state)
print("Searching for a solution...\n")
solution = animate_search(canvas, initial_state)
if solution:
    print("Final solution found:")
    print_board(solution)
else:
    print("No solution found.")

root.mainloop()