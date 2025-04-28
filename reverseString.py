#Natasha Mills      3-10-25
#Lab 7
#This code takes an input string and modifies it to be backwards five different ways!

#Version 1
def reverseStringV1(input_string):
    return(input_string[::-1])

def main1():
    user_input = input("Enter the string you would like to reverse:")
    reversed_string = reverseStringV1(user_input)
    print("Your reversed string is:", reversed_string)

if __name__ == "__main__":
    main1()

#Version 2
def reverseStringV2(input_string):
    return''.join(reversed(input_string))

def main2():
    user_input = input("Enter the string you would like to reverse:")
    reversed_string_V2 = reverseStringV2(user_input)
    print("Your reversed string is:", reversed_string_V2)

if __name__ == "__main__":
    main2()

#Version 3
def reverseStringV3(input_string):
    reversed_string = ''
    for i in range(len(input_string) -1, -1, -1):
        reversed_string = reversed_string + input_string[i]
    return reversed_string

def main3():
    user_input = input("Enter the string you would like to reverse:")
    reversed_string_V3 = reverseStringV3(user_input)
    print("Your reversed string is:", reversed_string_V3)

if __name__ == "__main__":
    main3()

#Version 4
def reverseStringV4(input_string):
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string 
    return reversed_string

def main4():
    user_input = input("Enter the string you would like to reverse:")
    reversed_string_V4 = reverseStringV4(user_input)
    print("Your reversed string is:", reversed_string_V4)

if __name__ == "__main__":
    main4()

#Version 5
def reverseStringV5(input_string):
    reversed_string = ''
    index = len(input_string) -1
    while index >= 0:
        reversed_string = reversed_string + input_string[index]
        index = index - 1
    return reversed_string

def main5():
    user_input = input("Enter the string you would like to reverse:")
    reversed_string_V5 = reverseStringV5(user_input)
    print("Your reversed string is:", reversed_string_V5)

if __name__ == "__main__":
    main5()