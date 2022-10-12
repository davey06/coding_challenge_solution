def isValid(s: str) -> bool:
    bracket_couples = ['()',
                       '[]',
                       '{}',
                      ]
    
    while s:
        initial_lenght = len(s)
        
        for bracket_couple in bracket_couples:
            s = s.replace(bracket_couple, '')
            
        final_lenght = len(s)
        
        if initial_lenght == final_lenght:
            result = False
            return result
        
    result = True
    return result 

if __name__ == "__main__":
    line = '(){}()[({})]'
    
    if isValid(line):
        print("valid")
    else:
        print("invalid")