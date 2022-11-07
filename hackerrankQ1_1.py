def work(str1):
    temp = []
    str1 = str1.swapcase()
    temp = str1.split()
    str1 = " ".join(temp[::-1])
    return str1


msg = input("Enter a String: ")
print(msg)
print(work(msg))
