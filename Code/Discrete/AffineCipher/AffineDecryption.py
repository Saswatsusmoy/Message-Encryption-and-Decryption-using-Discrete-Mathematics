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

def decryption(Encrypted_message):

    # with open('ShiftCipher/DecryptedText.txt','r') as file:
    #     Encrypted_message = file.read()
    with open('Keys/AffineCipherkey1.txt','r') as file:
        Key1Used = file.read()
    with open('Keys/AffineCipherkey2.txt','r') as file:
        Key2Used = file.read()

    k = int(Key1Used)
    a = int(Key2Used)    
        
    


    problist= []
    with open('Keys/AffineCipherProbKeys.txt','r') as file:
        for line in file:
            problist.append(int(line))
            
    value_y = []        
    with open('Keys/AffineCipherValue_y.txt','r') as file:
        for line in file:
            value_y.append(int(line))       
            
    # print(problist)
    # print(Key)
    # print(value_y)
    DecryptedText = []
    for i in range(len(Encrypted_message)):
        if i in problist:
            value_j=value_y[i]-33
            a_inv= a_inverse(a)
            x= a_inv*(value_j-k)%127
            # print(chr(x),end='')
            DecryptedText.append(chr(x))
        else:
            a_inv= a_inverse(a)
            x= a_inv*(value_y[i]-k)%127
            # print(chr(x),end='')
            DecryptedText.append(chr(x))
            
            
    string ="" 
    for d in DecryptedText:
        string = string +(d)         
    return string         