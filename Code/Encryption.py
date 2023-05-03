import random
import sys
sys.path.insert(0,"C:\Users\saswa\OneDrive\Desktop\CSE\CIC\Project\Discrete Sem 1\Discrete\AffineCipher")
sys.path.insert(0,"C:\Users\saswa\OneDrive\Desktop\CSE\CIC\Project\Discrete Sem 1\Discrete\ShiftCipher")
sys.path.insert(0,"C:\Users\saswa\OneDrive\Desktop\CSE\CIC\Project\Discrete Sem 1\Discrete\SubstitutionCipher")
sys.path.insert(0,"C:\Users\saswa\OneDrive\Desktop\CSE\CIC\Project\Discrete Sem 1\Discrete\VignereCipher")
sys.path.insert(0,"C:\Users\saswa\OneDrive\Desktop\CSE\CIC\Project\Discrete Sem 1\Discrete\HillCipher")
sys.path.insert(0,"C:\Users\saswa\OneDrive\Desktop\CSE\CIC\Project\Discrete Sem 1\Discrete\PermutationCipher")

# print(sys.path)


from AffineCipher import AffineEncryption
from ShiftCipher import ShiftEncryption
from SubstitutionCipher import SubstitutionEncryption
from VignereCipher import VignereEncryption
from HillCipher import HillEncryption
from PermutationCipher import Permutationencryption





with open('text.txt','r') as file:
    message = file.read()
    
randomNumList =[]
for i in range(10000):
   randnum = random.randint(1,6)
   if randnum not in randomNumList:
        randomNumList.append(randnum)
        if len(randomNumList)==6:
            break
   
# print(randomNumList)

file = open("randomList.txt","w")
for i in range(len(randomNumList)):
    file.write(f"{str(randomNumList[i])}\n")
file.close()    

def encryption(argument):
    match argument:
        case 1:
            return AffineEncryption.encryption(message)
        case 2:
            return HillEncryption.encryption(message)
        case 3:
            return ShiftEncryption.encryption(message)
        case 4:
            return SubstitutionEncryption.encryption(message)
        case 5:
            return VignereEncryption.encryption(message) 
        case 6:
            return Permutationencryption.encryption(message) 


message = encryption(randomNumList[0])  #message ko overwrite kar diya
# print(message)
message=encryption(randomNumList[1])
# print(message)
message=encryption(randomNumList[2])
# print(message)
message=encryption(randomNumList[3])
# print(message)
message=encryption(randomNumList[4])
# print(message)
message=encryption(randomNumList[5])

with open('Encrypted.txt',"w") as file:
    file.write(message)

    
    

