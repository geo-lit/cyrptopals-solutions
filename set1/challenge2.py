import sys
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
    if (len(sys.argv) != 3):
        print("wrong args")
        return 0
    

    x = codecs.decode(sys.argv[1], encoding="hex")
    y = codecs.decode(sys.argv[2], encoding="hex")

    ans = xor(x,y)

    print ("".join(ans))


if __name__ == "__main__":
    main()