def remvoveSpecialChars(str):
    strOut = ""
    for char in str:
        if char.isnumeric() or char.isalpha():
            strOut += char
    return strOut

def getNumberOfUniqueChars(str):
    uniqueCharList = []
    for char in str:
        if char not in uniqueCharList:
            uniqueCharList.append(char.lower())
    return len(uniqueCharList)
        
def isPalindrome(str):
    str = remvoveSpecialChars(str)
    str = str.lower()
    noUniqueChars = getNumberOfUniqueChars(str)
    for i in range(0, len(str) // 2):
        if str[i] != str[-i-1]:
            return ("NO", -1)
    return ("YES", noUniqueChars)
    
with open('./input.txt', 'r') as f:
    line = f.readline()
    while line:
        isPalindrome, uniqueChars  = isPalindrome(line)
        print(f"{isPalindrome}, {uniqueChars}")
        line = f.readline()