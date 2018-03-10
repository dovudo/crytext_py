import sys
def __ARGS__():

    print("For decrypting usage: python crytext.py d")
    ps = input('Input your password->  ')
    for i in range(60): print("\n")
    text = input('Enter text here \n ')
    if sys.argv[0] == "d":
        print("Get decrypted text: \n " + decrypt(text, ps))
    else:
        print("Get encrypted text: \n " + encrypt(text, ps))


def encrypt(text, key='default'):

    final_str = []
    out_str = ""
    ascii_key = get_ascii(key)

    for i in range(len(text)):
        j = i
        if j >= len(ascii_key) or j >= len(text):
            j = 0
        final_str.append(chr(round(ord(text[i]) + (i * j + 13) / len(key) + (ascii_key[j]))))
    return out_str.join(final_str)


def decrypt(text, key='default'):

    final_str = []
    out_str = ""
    ascii_key = get_ascii(key)

    for i in range(len(text)):
        j = i
        if j >= len(ascii_key) or j >= len(text):
            j = 0
        final_str.append(chr(round(ord(text[i]) - ascii_key[j] - ((i * j + 13) / len(key)))))
    return out_str.join(final_str)


def get_ascii(key):

    ascii_list = []
    for i in key:
        ascii_list.append(ord(i))
    return (ascii_list)


if __name__== '__main__':
    __ARGS__()