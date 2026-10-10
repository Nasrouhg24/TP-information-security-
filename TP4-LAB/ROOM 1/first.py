encrypt = {'a': 'q','b': 'm','c': 'j','d': 'z','e': 't','f': 'g','g': 'f','h': 'k','i': 'p','j': 'w','k': 'l','l': 's','m': 'b','n': 'o','o': 'x','p': 'n','q': 'c','r': 'r','s': 'y','t': 'e','u': 'v','v': 'h','w': 'i','x': 'a','y': 'd','z': 'u'}
decrypt = {'q': 'a','m': 'b','j': 'c','z': 'd','t': 'e','g': 'f','f': 'g','k': 'h','p': 'i','w': 'j','l': 'k','s': 'l','b': 'm','o': 'n','x': 'o','n': 'p','c': 'q','r': 'r','y': 's','e': 't','v': 'u','h': 'v','i': 'w','a': 'x','d': 'y','u': 'z'}


def encrypt_fun(s):
    inp = s.lower()
    out = ""
    for i in inp : 
        if i!= ' ':
            out += encrypt[i]
        else : 
            out +=' '
    return out 

def decrypt_fun(s):
    inp = s.lower()
    out = ""
    for i in inp  : 
        if i!= ' ':
            out += decrypt[i]
        else : 
            out +=' '
    return out 


print("1 : "+ encrypt_fun("KEEP THE SECRET SAFE"))
print("2 : "+ decrypt_fun("ERVYE DXVR SXFPJ"))