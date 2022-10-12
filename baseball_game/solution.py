def calPoints(ops) -> int:
    
    records = []
    
    for op in ops:
        
        if op.lstrip('-').isdigit():
            records.append(int(op))
            
        elif op == 'C':
            del records[-1]
            
        elif op == 'D':
            records.append(int(2*records[-1]))
            
        elif op == '+':
            records.append(int(records[-1]+records[-2]))

    result = sum(records)   
    return result
  
if __name__ == "__main__": 
    # line = '5 -2 + D'   
    line = input("Enter Score ex(5,2,+,D): ")

    ops = line.strip().split()
    
    print(calPoints(ops))