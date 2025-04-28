
import turtle

def tridecagon(t):
    """Draws a tridecagon (13-sided polygon) using the given turtle instance."""
    sides = 13
    angle = 360 / sides
    length = 20  # Adjust size as needed
    
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    tridecagonTurtle(t)
    
    screen.mainloop()