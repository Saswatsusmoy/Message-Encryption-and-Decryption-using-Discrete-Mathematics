
import random
def a_inverse(a):
        c=1
        if a==1:
            return 1
        else:
            for i in range(127*127):
                c=c+127
                f=c%a
                if f==0:
                    ans=c/a
                    ans=int(ans)
                    break
        return ans
    
    
    
    
def encryption(message):

    k = random.randint(0,126)
    # print(k)
    a = random.randint(2,126)
    # print(a)


    with open('Keys/AffineCipherkey1.txt','w') as file:
        file.write(str(k))
        
    with open('Keys/AffineCipherkey2.txt','w') as file:
        file.write(str(a))    
    prob=[]
    value_y=[]
    for i in range(len(message)):
        p = ord(message[i])
        y= (a*p+k)%127
        if y<33:
            y=y+33
            prob.append(i)
        value_y.append(y)
            
        # print(y)
        
        # print(chr(y),end='')

    print("\n")


            
    string="" 
    for y in value_y:
        string = string + chr(y)
    # print(string)       
            
            
    file = open('Keys/AffineCipherProbKeys.txt','w')
    for p in prob:
        file.write(f"{str(p)}\n")        
            
            
    file = open('Keys/AffineCipherValue_y.txt','w') 
    for y in value_y:
        file.write(f"{str(y)}\n")
    file.close()   
    
    
    return string

    
    








