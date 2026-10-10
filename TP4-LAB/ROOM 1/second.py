from collections import Counter , defaultdict

def analyze(s):
    s = s.lower()

    counter = Counter(c for c in s if c.isalpha())
    total = sum(counter.values())

    frequencies = {
        char: count / total
        for char, count in counter.items()
    }

    groups = defaultdict(list)

    for char, freq in frequencies.items():
        groups[freq].append(char)

    return dict(sorted(groups.items(), reverse=True))

def trying_to_decrypt(s):

    s = s.lower()

    t1 = ""
    t2 = ""

    decrypt = [['E'],['T'],['R'],['S', 'O'],['A'],['H'],['N'],['D'],['I'],['G'],['L']]
    out = analyze(s)
    print(out)
    letter_rank = {}
    for rank, letters in enumerate(out.values()):
        for letter in letters:
            letter_rank[letter] = rank
    print("\nLetter ranks:")
    print(letter_rank)
    for i in s:
        if i.isalpha():
            index = letter_rank[i]
            if index < len(decrypt):
                # Two possible letters
                if len(decrypt[index]) == 2:
                    t1 += decrypt[index][0]
                    t2 += decrypt[index][1]
                else:
                    t1 += decrypt[index][0]
                    t2 += decrypt[index][0]
            else:
                t1 += '?'
                t2 += '?'

        else:
            t1 += i
            t2 += i

    print("\nt1 : " + t1)
    print("t2 : " + t2)


trying_to_decrypt("EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,MVE PE FPHTY Q FXXZ YEQRE.SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,QOZ YKXRE IXRZY.IKTO DXV RTJXHTR EKT BTYYQFT,EKT HPFTOTRT LTD KQY GXVR STEETRY.")
