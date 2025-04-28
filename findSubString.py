#Natasha Mills      3/10/25
#Lab 7
#This program checks for a certain index of a substring and then returns 
# the index if the substring is not found. 

#Version 1
def findSubStringV1(input_string, substring):
    return input_string.find(substring)

def main():
    user_input = input("Enter your main string: ")
    sub_string = input("Enter your substring that you want to find: ")
    
    index = findSubStringV1(user_input, sub_string)
    
    if index != -1:
        print(f"Your substring was found at index: {index}")
    else:
        print("Your substring was not found.")

if __name__ == "__main__":
    main()

#Version 2
def findSubStringV2(input_string, substring):
    index = input_string.find(substring)
    return index

def main():
    user_input = input("Enter your main string: ")
    sub_string = input("Enter your substring that you want to find: ")
    index_v2 = findSubStringV2(user_input, sub_string)
    if index_v2 != -1:
        print(f"Your substring was found at index: {index_v2}")
    else:
        print("Your substring was not found.")

if __name__ == "__main__":
    main()

#Version 3
def findSubStringV1(input_string, substring):
    return input_string.find(substring)

def findSubStringV3(input_string, substring):
    # Iterative approach to find the substring
    for i in range(len(input_string) - len(substring) + 1):
        if input_string[i:i + len(substring)] == substring:
            return i
    return -1

def main():
    user_input = input("Enter your main string: ")
    sub_string = input("Enter your substring that you want to find: ")
    index_v3 = findSubStringV3(user_input, sub_string)
    if index_v3 != -1:
        print(f"Your substring was found at index: {index_v3}")
    else:
        print("Your substring was not found.")

if __name__ == "__main__":
    main()