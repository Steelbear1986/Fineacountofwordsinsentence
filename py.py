def encode(string):
    print(" ".join(sorted(set(string.split), key=words.index)))
    return ''


string = input()

print(encode(string))
