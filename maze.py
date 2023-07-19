import os
import turtle
import time
import sys
from collections import deque

# Define the classes for the Maze, Red, Blue, Green, and Yellow turtles

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

def load_maze(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]
    
def bfs_search(start_x, start_y, end_x, end_y):
    frontier = deque()
    visited = set()
    solution = {}

    def add_to_frontier(x, y, prev_x, prev_y):
        if (x, y) in path and (x, y) not in visited:
            cell = (x, y)
            solution[cell] = prev_x, prev_y  # Record the previous cell as the key for the current cell
            frontier.append(cell)
            visited.add(cell)

    frontier.append((start_x, start_y))
    solution[start_x, start_y] = start_x, start_y

    while frontier:
        x, y = frontier.popleft()

        add_to_frontier(x - 24, y, x, y)  # check the cell on the left
        add_to_frontier(x, y - 24, x, y)  # check the cell down
        add_to_frontier(x + 24, y, x, y)  # check the cell on the right
        add_to_frontier(x, y + 24, x, y)  # check the cell up

        green.goto(x, y)
        green.stamp()

    return solution



def back_route(x, y, solution):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]

def setup_maze(grid):
    global start_x, start_y, end_x, end_y

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def end_program():
    wn.exitonclick()
    sys.exit()

def main():
    global wn, maze, red, blue, green, yellow, walls, path, start_x, start_y, end_x, end_y, frontier, visited, solution

    # Create the turtle screen and set it up
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A BFS Maze Solving Program")
    wn.setup(1300,700)    # Adjust the dimensions to fit the maze (14 cells x 24 pixels)


    # Set up classes
    maze = Maze()
    red = Red()
    blue = Blue()
    green = Green()
    yellow = Yellow()

    # Set up lists
    walls = []
    path = []
    visited = set()
    frontier = deque()
    solution = {}

    # Load the maze from the text file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "maze.txt")
    grid = load_maze(file_path)

    # Set up the maze layout and get the start and end positions
    setup_maze(grid)

    # Perform BFS search to find the solution
    start_solution = bfs_search(start_x, start_y, end_x, end_y)

    # Backtrack from the end to the start to mark the path
    back_route(end_x, end_y, start_solution)

    # Display a message when the maze is solved
    turtle.color("white")
    turtle.goto(-50, -300)
    turtle.write("Maze Solved!", font=("Arial", 24, "normal"), align="center")

    # End the program when the user clicks on the window
    end_program()

if __name__ == "__main__":
    main()
