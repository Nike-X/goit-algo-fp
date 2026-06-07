# This script demonstrates Pythagoras tree construction
# Note. We construct a simplified tree using lines, not squares

import turtle

# This function defines simplified Pythagoras tree construction
def pythagoras_tree(t, branch_length, order):
    # Set tree branches angle and scale
    angle = 45
    scale = 0.7
    
    # Stop recursion when order reaches 0
    if order == 0:
        return
    
    # At each recursion step, draw the main branch and two lower-order subtrees
    t.forward(branch_length)
    t.left(angle)
    pythagoras_tree(t, branch_length * scale, order - 1)
    t.right(2 * angle)
    pythagoras_tree(t, branch_length * scale, order - 1)
    t.left(angle)
    t.back(branch_length)

# This function defines Turtle objects settings
# and draws Pythagoras tree of given order
def draw_pythagoras_tree(order):
    # Set window
    window = turtle.Screen()
    window.bgcolor("white")

    # Set Turtle object and starting point for drawing
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    # Draw Pythagoras tree
    pythagoras_tree(t, 150, order)
    # Keep the Turtle window open
    window.mainloop()

# Main function to process user input
def main():
    # Print greeting
    print("Welcome! This program draws a simplified Pythagoras tree.")
    print("Drawing a tree with order > 7 may take a long time!")

    # Wait for user input
    while True:
        user_input = input("Enter a Pythagoras tree order (integer): ")

        # Try to convert user input into integer (tree order)
        try:
            order = int(user_input)

            # Ignore negative order value
            if order < 0:
                print("Order should be greater than or equal to 0.")
                continue
            
            # Draw Pythagoras tree of given order and exit
            draw_pythagoras_tree(order)
            return

        except ValueError:
            print(f"Is not an integer: {user_input}")

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()