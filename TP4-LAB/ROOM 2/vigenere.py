from string import ascii_lowercase
from collections import Counter , defaultdict



alphabet = {letter: i for i, letter in enumerate(ascii_lowercase)}
reverse_alphabet = {value: key for key, value in alphabet.items()}
mx = [[i for i in range(26)] for _ in range(26) ]

# we know that the key is 4 len 

groups = {1 :[], 2:[],3: [],4:[]}

ciphertext = "VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZLGFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVCOPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWLGOFGGGVAQFGIEZLTUS".lower()
for i in range(len(ciphertext)): 
    groups[i%4 +1].append(ciphertext[i])

print("the groups got since the len of the key is 4 are : ")
for i in groups :
    print(f"group{i}: {groups[i]}" )

    


# searching for e in each group the most freq letter 

def analyze(s):
    counter = Counter(s)
    total = len(s)
    most_frequent = counter.most_common(1)[0]
    letter = most_frequent[0]
    frequency = most_frequent[1] / total
    return letter, frequency

keys = {}
for i in groups:
    most_frequent, frequency = analyze(groups[i])
    print(f"\nGroup {i}")
    print(f"Most frequent letter: {most_frequent}")
    print(f"Frequency: {frequency:.2%}")
    # We assume the most frequent plaintext letter is E
    cipher_index = alphabet[most_frequent]
    e_index = alphabet['e']

    shift = (cipher_index - e_index) % 26
    keys[i] = shift
    print(f"{most_frequent} corresponds to e")
    print(f"K{i} shift = {shift}")
    print(f"K{i} letter = {ascii_lowercase[shift]}")

print(keys)


key = ""

for i in range(1, 5):
    key += ascii_lowercase[keys[i]]
print("\nRecovered key:", key.upper())

recov = "" 
for i in range(len(ciphertext)):
    cipher_index = alphabet[ciphertext[i]]
    key_index = alphabet[key[i % 4]]
    plain_index = (cipher_index - key_index) % 26
    recov += reverse_alphabet[plain_index]


print("the recovered message is :")
print(recov)










