s = input("What int would you like to test?")

def transformString(s):
    result = []
    i = 2
    while i < len(s):
        if i + 2 < len(s) and s[i] == s[i + 1] == s[i + 2]:
            result.append("X")
            i += 3
        elif i + 2 < len(s) and s[i] == s[i + 1]:
            result.append(s[i] ** 3)
            i += 2
        else:
            result.append(s[i])
            i += 1
    return "".join(result)
transformString(s)
