def changeCoin(coins):
    coins.sort()
    currentChange = 0
    
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        
        currentChange += coin
    return currentChange + 1
    
print(changeCoin([1,1,2,3,5,7,22]))