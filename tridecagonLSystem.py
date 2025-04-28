import turtle
import random

def tridecagon(t):
    sides = 13
    angle = 360 / sides
    length = 20  
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    tridecagon(t)
    screen.mainloop()

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'PFPBH-B++FPBF-B'   # Rule 1
    elif ch == 'T':
        newstr = 'F+PHBF+B+H' #Rule 2
    elif ch == 'P':
        newstr == 'HPHB-F-B-P' #Rule 3
    else:
        newstr = ch    # no rules apply so keep the character
    return newstr

def isInScreen(w, t): #checks whether turtle is in screen
    if random.random() > 0.1:
        return True
    else:
        return False

def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'H':
            def tridecagonTurtle(s, x, y, t):
                t.penup()
                t.goto(random.randint(), random.randint())
                t.pendown()
                angle = 360 / 13
                for _ in range(13): 
                    t.right(angle)  
                    t.forward(s) 

            def main():
                s = 3
                x = 0
                y = 0
                t = turtle.Turtle()
                tridecagonTurtle(s, x, y, t)
                turtle.done()

                if __name__ == "__main__":
                    main()
        elif cmd == 'P':
            turtle.Turtle().shape('turtle')
            while isInScreen(turtle.Screen(), turtle.Turtle()):
                def randomPlace(s,t):
                    coin = random.randrange(0, 2)
                    if coin == 0:              # heads
                        x = random.randint(-300,300)
                        y = random.randint(-300,300)
                        turtle.Turtle().goto(x,y)
                    else:                      # tails
                        turtle.Turtle().goto(x,y)
                    turtle.Turtle().forward(50)

def main():
    inst = createLSystem(4, "FTP")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(100)
    drawLsystem(t, inst, 75, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
