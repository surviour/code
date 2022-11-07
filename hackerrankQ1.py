def work(str1):
    temp1 = str1
    temp = []
    for i, letters in enumerate(temp1):
        if (letters == " "):
            temp.append(str1)
            str1 = ""
        elif (letters.isupper()):
            if (i == 0):
                str1 = letters.lower()
            else:
                letters = letters.lower()
                str1 = str1+letters
        else:
            if (i == 0):
                str1 = letters.upper()
            else:
                letters = letters.upper()
                str1 = str1+letters
    temp.append(str1)
    str1 = ""
    print(temp)
    str1 = " ".join(temp[::-1])
    return str1


msg = "HeLLo WorlD"
print(msg)
print(work(msg))
