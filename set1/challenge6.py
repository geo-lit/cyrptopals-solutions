import hammingDistance
import codecs

def getFreqList(allText):
    freqList = {}
    count = 0
    for i in allText:
        for j in i.lower():
            if str(j).isalpha():
                if j in freqList.keys():
                    freqList[j] += 1
                else:
                    freqList[j] = 1
                count += 1

    for i in freqList:
        freqList[i] = freqList[i]/count
    
    return freqList

def xor(x, y):
    if (len(x) == len(y)):
        ans = []
        for a,b in zip(x,y):
            ans.append(chr(a ^ b))
        return ans
    else:
        return 0

def getKeyByte(raw, freqList):
    max_freq = 1
    allStrings = {}

    for i in range(0, 256):
        key = chr(i) * len(raw)
        out = xor(raw,key.encode())
        if out == 0:
                continue
        for i in range(0, len(out)):
            out[i] = out[i].lower()
        
        freq = {}
        total = 0
        for j in out:
            if 97 <= ord(j) <= 122:
                if j in freq.keys():
                    freq[j] += 1
                else:
                    freq[j] = 1
                total += 1
        
        if len(freq.keys()) == 0:
            continue
        
        avg_freq = 0

        for x in freq:
            avg_freq += (freq[x]/total) - (freqList[x])
        avg_freq = abs(avg_freq / len(freq))
        
        allStrings[avg_freq] = key

    return allStrings[sorted(allStrings)[0]]

        

def getKey(transposed):
    fp = open("beemovie.txt","r")
    freqList = getFreqList(fp.readlines())
    fp.close()
    key = b''
    for i in transposed:
        key += getKeyByte(i, freqList).encode()
    return key



def main():
    fp = open("plainFor6.txt", "r")
    base64 = fp.readline()
    raw = codecs.decode(base64.encode(), encoding="base64")
    
    # for each keysize generate 5 windows and calculate
    # hamming distance between all of them
    avg_distances = {}
    for i in range(2, 41):
        windows = []
        for j in range(0, 12):
            windows.append(raw[j*i:j*i+i])
        first_window = 0
        distances = []
        while first_window < len(windows) - 1:
            second_window = first_window + 1
            while second_window < len(windows):
                distances.append(hammingDistance.hamming(windows[first_window], windows[second_window]))    
                second_window += 1
            first_window += 1
        
        # calculate normalized average distance
        avg_distance = 0
        for j in distances:
            avg_distance += j
        avg_distance = avg_distance / (len(distances) * i)
        avg_distances[i] = avg_distance
    
    # sort dictionary by value
    sorted_distances = sorted(avg_distances.items(), key=lambda x: x[1])
    keysize = sorted_distances[0][0]

    # break data into keysize chunks
    allblocks = []
    i = 0
    while i < len(raw)-keysize:
        allblocks.append(raw[i:i+29])
        i += 29

    # transpose all blocks - take all first bytes, second bytes ...
    transposed = [b''] * len(allblocks[0])
    i = 0
    while i < len(allblocks):
        j = 0
        while j < len(allblocks[i]):
            transposed[j] += chr(allblocks[i][j]).encode()
            j += 1
        i += 1

    base = "terminator x: bring the noise"
    key = ""
    i = 0
    while i < len(raw):
        key += base[i%29]
        i += 1
    key = key.encode()
    print("".join(xor(raw,key)))



if __name__ == "__main__":
    main()