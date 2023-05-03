
import numpy
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
    message1=message
    
    with open('Keys/HillCiphermessage.txt','w') as file:
        file.write(message1) 
        
    if len(message1)%2 ==1:
        message = message1 +"x"
    else:
        message = message1   
    
        
            

    with open('Keys/HillCipherlength.txt','w') as file:
        file.write(str(len(message))   ) 

    Key_matrix = numpy.matrix([[random.randint(1,127),random.randint(1,127)],[random.randint(1,127),random.randint(1,127)]])
    file = open('Keys/HillCipherKeyMatrix.txt','w')
    for i in range(0,2):
        for j in range(0,2):
            file.write(f"{str(Key_matrix[i,j])}\n")        
    file.close()


    cipher_matrices =[]
    i =0
    while i<=(len(message)-2):
        message_matrix = numpy.array([[ord(message[i]),ord(message[i+1])]])
        # print(f"Message Matrix:{message_matrix}")
        i=i+2
        cipher_matrix = (message_matrix*Key_matrix)%127
        # print(f"Cipher matrix:{cipher_matrix}")
    
        cipher_matrices.append(cipher_matrix)   
    # print(cipher_matrices)
    # print(len(cipher_matrices))


    CipherKeys =[]
    for i in range(len(cipher_matrices)):
        for j in range(0,1):
            for k in range(0,2):
                CipherKeys.append(int(cipher_matrices[i][j,k]))
    # print(CipherKeys)
    # print(len(CipherKeys))

    string =""
    probKeys=[]
    for i in range(len(CipherKeys)):
        if CipherKeys[i]<33:
            CipherKeys[i]=CipherKeys[i]+33
            probKeys.append(i)
            string = string +(chr(CipherKeys[i]))
        else:
            string = string +(chr(CipherKeys[i]))
            
    file = open('Keys/HillCipherProbKeys.txt','w')
    for p in probKeys:
        file.write(f"{str(p)}\n")         
                
        
    return string


        


                    
                    


    