import sys
sys.path.insert(0,"C:\\Users\\agarw\\OneDrive\\Desktop\\Discrete\\AffineCipher")
sys.path.insert(0,"C:\\Users\\agarw\\OneDrive\\Desktop\\Discrete\\ShiftCipher")
sys.path.insert(0,"C:\\Users\\agarw\\OneDrive\\Desktop\\Discrete\\SubstitutionCipher")
sys.path.insert(0,"C:\\Users\\agarw\\OneDrive\\Desktop\\Discrete\\VignereCipher")
sys.path.insert(0,"C:\\Users\\agarw\\OneDrive\\Desktop\\Discrete\\HillCipher")
sys.path.insert(0,"C:\\Users\\agarw\\OneDrive\\Desktop\\Discrete\\PermutationCipher")


from AffineCipher import AffineDecryption
from ShiftCipher import ShiftDecryption
from SubstitutionCipher import SubstitutionDecryption
from VignereCipher import VignereDecryption
from HillCipher import HillDecryption
from PermutationCipher import PermutationDecryption



with open('Encrypted.txt','r') as file:
    message = file.read()
randomNumList =[]
with open('randomList.txt','r') as file:
    for line in file:
        randomNumList.append(int(line))
# print(randomNumList)    
    
def decryption(argument):
    match argument:
        case 1:
            return AffineDecryption.decryption(message)
        case 2:
            return HillDecryption.decryption(message)
        case 3:
            return ShiftDecryption.decryption(message)
        case 4:
            return SubstitutionDecryption.decryption(message)
        case 5:
            return VignereDecryption.decryption(message)  
        case 6:
            return PermutationDecryption.decryption(message)
        
        
message = decryption(randomNumList[5])  #message ko overwrite kar diya
# print(message)
message = decryption(randomNumList[4])  #message ko overwrite kar diya
# print(message)
message=decryption(randomNumList[3])
# print(message)
message=decryption(randomNumList[2])
# print(message)
message=decryption(randomNumList[1])
# print(message)
message=decryption(randomNumList[0])
# print(message)

with open('Decrypted.txt',"w") as file:
    file.write(message)



