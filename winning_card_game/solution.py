import timeit

def getWinningCards(cards) -> int:
    start = timeit.default_timer()
    res = -1
    winningCards = []
    for sets in cards:
        duplicates = []
        for value in sets:
            count = sets.count(value)
            if count == 1:
                winningCards.append(value)

    if len(winningCards) > 0:
        res = max(winningCards) 

    end = timeit.default_timer()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")
    return res



if __name__ == "__main__":
    listTest =  [
                [[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]],
                [[5,5], [2,2]],
                [[1,1,2,3,3,4,5,6,6], [1,2,2,3,4,4], [1,2,3,5,5,7]],
            ]
    
    for q in listTest:
        print(getWinningCards(q))