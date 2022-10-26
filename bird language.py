def translate(text: str) -> str:
    i = 0
    fin = ''
    sam = 'euioay'
    spol = 'qwrtplkjhgfdszxcvbnm'
    while i < len(text):
        if text[i] in sam:
            fin += text[i]
            i += 3
        elif text[i] in spol:
            fin += text[i]
            i += 2
        else:
            fin += text[i]
            i += 1
    return fin


print("Example:")
print(translate("hieeelalaooo"))
