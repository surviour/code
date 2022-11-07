def extract_string(a):
    print(a)
    print(type(a))
    c=a.split(" ")
    print(c)
    print(type(c))
    b=c[0]
    print(type(b))
a=input("Enter a string : ")
extract_string(a)