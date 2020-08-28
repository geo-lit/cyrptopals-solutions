def tobit(x):

    out = [bin(i) for i in x]
    return out

def hamming(x,y):
    a = tobit(x)
    b = tobit(y)

    diff = 0

    if len(a) == len(b):
        for i,j in zip(a,b):
                        
            char1 = i[2:]
            char2 = j[2:]

            length_diff = len(char1) - len(char2)

            if length_diff < 0:
                char1 = ("0" * abs(length_diff)) + char1
            elif length_diff > 0:
                char2 = ("0" * length_diff) + char2
            
            for x,y in zip(char1,char2):
                if x != y:
                    diff += 1
    return diff
