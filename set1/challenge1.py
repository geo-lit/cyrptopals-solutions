import codecs
hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

ans = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n".encode()

raw = codecs.decode(hex_str, encoding='hex')

if(ans == codecs.encode(raw, encoding='base64')):
    print(raw)