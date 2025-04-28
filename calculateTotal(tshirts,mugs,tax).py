def calculateTotal(tshirts, mugs, tax):
    tshirtCost = tshirts * 15
    mugsCost = mugs * 5
    shippingCost = 20
    items = tshirts + mugs
    if items <= 50:
        serviceCharge = 30
    else:
        serviceCharge = 0
    freeMugs = tshirts // 3
    freeMugs = -5
    tax = tshirtCost + mugsCost + serviceCharge + freeMugs
    totalCost = serviceCharge + tshirtCost + mugsCost + tax + freeMugs
    print("Your total cost is going to be,", totalCost)

def main():
    tshirts = int(input("How many tshirts?"))
    mugs = int(input("How many mugs?"))
    calculateTotal(tshirts, mugs, tax)
    
if __name__ == "__main__":
    main()