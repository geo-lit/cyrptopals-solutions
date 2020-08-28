import codecs

def getFreqList(allText):
    words = []
    for i in allText:
        if 4 <= len(i) <= 7:
            words.append(i.strip())
    
    return words


def xor(x, y):
    if (len(x) == len(y)):
        ans = []
        for a,b in zip(x,y):
            ans.append(chr(a ^ b))
        return ans
    else:
        return 0


def main():
    fp = open("dict.txt","r")
    wordList = getFreqList(fp.readlines())
    fp.close()
    
    max_freq = 1
    final_out = [] 

    fp =  open("ciphers.txt","rb")
    everything = fp.readlines()

    for z in everything:
        raw = codecs.decode(z.strip(), encoding='hex')
        max_freq = 1
        final_out = []
        for i in range(0,256):

            key = chr(i) * len(raw)
            out = xor(raw,key.encode())
            if out == 0:
                continue
            for i in range(0, len(out)):
                out[i] = out[i].lower()
            
            for i in wordList:
                if i in out:
                    print(out)



        


    return 1

if __name__ == "__main__":
    main()


