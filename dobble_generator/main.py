def getTotalNumberOfCards(s):
    return s*s - s + 1

def nobodyInCard(buddies, card):
    for buddy in buddies:
        if buddy in card:
            return False
    return True

def generateDeck(s):
    k = getTotalNumberOfCards(s)
    cards = [[] for i in range(k)]
    for i in range(1, k+1):
        buddies = [i]
        count = 0
        for card in cards:
            if nobodyInCard(buddies, card) and len(card) < s:
                buddies.extend(card)
                card.append(i)
                count += 1
            if count == s:
                break
    print(s) 
    for i in range(len(cards)):
        print(str(i + 1) + " - " + str(cards[i]))
with open('./input.txt', 'r') as f:
    input = f.readline()
    while input:
        try:
            generateDeck(int(input))
        except:
            print(input)
            print("invalid")
        input = f.readline()
