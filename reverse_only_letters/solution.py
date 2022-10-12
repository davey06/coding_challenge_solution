import timeit

def reverseOnlyLetters(S) -> str:
    start = timeit.default_timer()
    S, i, j = list(S), 0, len(S) - 1
    while i < j:
        if not S[i].isalpha():
            i += 1
        elif not S[j].isalpha():
            j -= 1
        else:
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
    
    end = timeit.default_timer()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")
    return "".join(S)

def reverseLetterOnly(S) -> str:
    start = timeit.default_timer()
    alphaOnly = ''

    for i in range(len(S)):
        if S[i].isalpha():
            alphaOnly += S[i]

    alphaOnly = alphaOnly[::-1]
    result = ''
    index , maxlenght = 0, len(alphaOnly)
    while index < maxlenght:
        if not S[index].isalpha():
            result += S[i]
        else:
            result += alphaOnly[i]
    
    
    end = timeit.default_timer()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")

    return result

if __name__ == "__main__":
    input = 'z<*zj'
    print(reverseOnlyLetters(input))
    print(reverseLetterOnly(input))
