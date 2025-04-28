#transformingToysCost.py
def transformingToysCost():
    robot = 0
    pack = 0
    toyType = input('What would you like to buy? \n'
    'we offer [r]obots and 5-[p]acks of robots!: ')
    if toyType == "r":
        robot = int(input('How many would you like to buy?: '))
    elif toyType == "p":
        pack = int(input('How many would you like to buy?: '))
    robotPrice = 14.99 * robot
    packPrice = 69.99 * pack
    toyCost = robotPrice + packPrice
    Tax = 0.08 * toyCost
    shippingCost = (robot * 2) + (pack * 7)
    previousTotal = toyCost + shippingCost
    discount = 0.05 * previousTotal
    totalCost = previousTotal - discount + Tax
    print(f'Your total is ${totalCost:.2f}')
#transformingToysCost()

def nextSpecialMultiple(number, mult):
    if number <= 0 or mult <= 0:
        return -1
    
    nextMultiple = (number // mult + 1) * mult
    return nextMultiple
#print(nextSpecialMultiple(22,5))

def levelAssessment(points):
    if points < 0:
        return "ERROR"
    if points < 25:
        level = "Novice"
    elif points >= 25 and points < 50:
        level = "Beginner"
    elif points >= 50 and points < 75:
        level = "Intermediate"
    elif points >= 75 and points < 100:
        level = "Expert"
    elif points >= 100:
        level = "Master"
        return level
print(levelAssessment(65))

def replaceCharWithCAT(text, char):
    if len(char) != 1:
        return "ERROR" 
    return text.replace(char, "CAT!")
print(replaceCharWithCAT("APPLE CAT!", "A"))  # Output: "CAT!PPLE CCAT!T!"
