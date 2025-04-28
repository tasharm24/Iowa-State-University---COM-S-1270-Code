#Natasha Mills      3/10/25
#Lab 7
#This program checks whether the string the user inputs is a 
#palindrome!

import reverseString

def palindromeCheckV1(input_string):
    reversed_string = reverseString.reverseStringV1(input_string)
    return input_string == reversed_string
    
def main1():
    user_input = input("Enter a string and check if it's a palindrome:")
    is_palindrome_v1 = palindromeCheckV1(user_input)
    print(is_palindrome_v1)

if __name__ == "__main__":
    main1()

def palindromeCheckV2(input_string):
    length = len(input_string)
    for i in range(length//2):
        if input_string[i] != input_string[length -i -1]:
            return False
        return True
def main2():
    user_input = input("Enter a string and check if it's a palindrome:")
    is_palindrome_v2 = palindromeCheckV1(user_input)
    print(is_palindrome_v2)

if __name__ == "__main__":
    main2()