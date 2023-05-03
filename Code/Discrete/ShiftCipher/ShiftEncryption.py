def encryption(message):
    import random
    k= random.randint(0,126)
    with open('Keys/ShiftCipherKeysUsed.txt','w') as file:
        file.write(str(k)) 

    prob = []
    value_y = []
    for i in range(len(message)):
        p = ord(message[i])
        y = (p+k)%127
        
        if y < 33:
            y = y + 33
            prob.append(i)
            
        value_y.append((y))
    # print(value_y)


    
    string = ""
    for y in value_y:
        string = string +(chr(y))
      
            
            
            
    file = open('Keys/ShiftCipherProbKeys.txt','w')
    for p in prob:
        file.write(f"{str(p)}\n")        
            
            
    file = open('Keys/ShiftCipherValue_y.txt','w') 
    for y in value_y:
        file.write(f"{str(y)}\n")
    file.close()            

    return string         
                        