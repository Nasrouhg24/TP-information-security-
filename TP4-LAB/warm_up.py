from string import ascii_lowercase
alphabet = ascii_lowercase

encr = {i: k for i, k in zip(range(1, 27), alphabet)}
decrypt = {i: k for i, k in zip(alphabet,range(1, 27))}

def ceasar_encrypt(s,k):
    inp = s.lower()
    out =""
    for i in inp : 
        if i !=' ':
            out += encr[(decrypt[i]+k-1)%26+1]
        else : 
            out += ' '
    return out 

def ceasar_decrypt(s,k):
    inp = s.lower()
    out = ""
    for i in inp : 
        if i !=' ':
            out += encr[(decrypt[i]-k-1)%26+1]
            
        else : 
            out += ' '
    return out 

print("Encrypting CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ with key 4 :")
print(ceasar_encrypt("CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ",4))
print("-"*20)
print("Decrypting GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA with key 8 :")
print(ceasar_decrypt("GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA",8))
print("-"*20)
print("Bruteforcing to decrypt : ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP")
for i in range(1,27):
    print(f"key {i} : "+ ceasar_decrypt("ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP",i))