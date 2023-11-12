def remvoveSpecialChars(str):
    strOut = ""
    for char in str:
        if char.isnumeric() or char.isalpha():
            strOut += char
    return strOut

def getNumberOfUniqueChars(str):
    uniqueCharList = []
    for char in str:
        if char.lower() not in uniqueCharList:
            uniqueCharList.append(char.lower())
    return len(uniqueCharList)
        
def isPalindrome(str):
    str = remvoveSpecialChars(str)
    NoUniqueChars = getNumberOfUniqueChars(str)
    for i in range(0, len(str) // 2):
        if str[i].lower() != str[-i-1].lower():
            return ("NO", -1)
    return ("YES", NoUniqueChars)
    
with open('./palindrome_checker/input.txt', 'r') as f:
    line = f.readline()
    while line:
        result = isPalindrome(line)
        print(f"{result[0]}, {result[1]}")
        line = f.readline()