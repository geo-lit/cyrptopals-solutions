import codecs

def xor(x, y):
    if (len(x) == len(y)):
        ans = []
        for a,b in zip(x,y):
            ans.append(chr(a ^ b))
        return ans
    else:
        return 0

def main():
    fp = open("iceicebaby.txt", "r")
    plain = "".join(fp.readlines()).encode()
    
    i = 0
    key = ""
    base = "ICE"
    while i < len(plain):
        key += base[i%3]
        i += 1

    key = key.encode()

    ans = xor(plain, key)

    out = codecs.encode("".join(ans).encode(), encoding="hex")
    print(out)
    
if __name__ == "__main__":
    main()