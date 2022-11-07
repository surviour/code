# arithmatic formatter

def printF(x, y, z, r, cds):  # Printing format(complete)(int,int,str)
    a = x
    b = y
    c = z
    d = r
    # print(len(str(a)))
    # print(len(str(b)))
    i = 0
    print(len(a))
    while (i != 1):
        for l in range(len(a)):
            if (len(str(b[l])) > len(str(a[l]))):
                # print("hi")
                print(" "*(len(str(b[l]))+1)+str(a[l]), end="    ")
            elif (len(str(a[l])) > len(str(b[āl]))):
                # print("hi")
                print("  "*(len(str(b[l]))-len(str(a[l]))+2) +
                      str(a[l]), end="    ")
            else:
                # print("hi")
                print("  "+str(a[l]), end="    ")

        print("\n")
        for j in range(len(b)):
            if (len(str(b[j])) > len(str(a[j]))):
                print(f"{c[j]} "+str(b[j]), end="    ")
            elif (len(str(a[j])) > len(str(b[j]))):
                print(f"{c[j]} "+" "*(len(str(a[j])) -
                      len(str(b[j])))+str(b[j]), end="    ")
            else:
                print(f"{c[j]} "+str(b[j]), end="    ")
        print("\n")
        for k in range(len(a)):
            if (len(str(b[k])) > len(str(a[k]))):
                print("-"*(len(str(b[k]))+2), end="    ")
            elif (len(str(a[k])) > len(str(b[k]))):
                print("-"*(len(str(a[k]))+2), end="    ")
            else:
                print("-"*(len(str(a[k]))+2), end="    ")

        print("\n")
        if (cds==True):
            for h in range(len(a)):
                if (len(str(b[h])) > len(str(a[h]))):
                    print(" "*(len(str(d[h]))-len(str(b[h]))) +
                          str(d[h]), end="    ")
                elif (len(str(a[h])) > len(str(b[h]))):
                    print(" "*(len(str(d[h]))-len(str(a[h]))+2) +
                          str(d[h]), end="    ")
                else:
                    print(" "+" "*(len(str(d[h]))-(len(str(b[h]))+1)) +
                          str(d[h]), end="    ")
        i += 1
        # if (len(str(b[i])) > len(str(a[i]))):
        #     print(" "*3+str(a[i]))
        #     print(f"{c[i]} "+str(b[i]))
        #     print("-"*(len(str(b[i]))+2))
        #     print(" "*(len(str(d[i]))-len(str(b[i]))+2)+str(d[i]), end="    ")
        # elif (len(str(a[i])) > len(str(b[i]))):
        #     print("  "+str(a[i]))
        #     print(f"{c[i]} "+" "*(len(str(a[i]))-len(str(b[i])))+str(b[i]))
        #     print("-"*(len(str(a[i]))+2))
        #     print(" "*(len(str(d[i]))-len(str(a[i]))+2)+str(d[i]))
        # else:
        #     print("  "+str(a[i]))
        #     print(f"{c[i]} "+str(b[i]))
        #     print("-"*(len(str(a[i]))+2))
        #     print(" "*(len(str(d[i]))-len(str(b[i]))+2)+str(d[i]))


def arg(l1, be):
    st1 = l1[0]
    print(st1)
    i = 1
    for j in range(1, len(l1)):
        temp = l1[j]
        st1 = st1+" "+temp
    print(st1)
    print(type(st1))
    temp = []
    temp = st1.split()
    print(temp)
    a = []*100
    b = []*100
    c = []*100
    index = 0
    j = 0
    while (j < 4):
        a.append(temp[index])
        print(temp[index])
        c.append(temp[index+1])
        print(temp[index+1])
        b.append(temp[index+2])
        print(temp[index+2])
        if (index >= len(temp)):
            break
        else:
            index += 3
            j += 1
    print(a)
    print(b)
    print(c)
    d = []*100
    i = 0
    if (be == True):
        while (i < 4):
            if (c[i] == '+'):
                ele = int(a[i])+int(b[i])
                d.append(ele)
            else:
                ele = int(a[i])-int(b[i])
                d.append(ele)
            i += 1
    print(d)
    printF(a, b, c, d, be)
    # for index in range(0, len(temp), 3):  # for result of one element of list
    #     a.append(temp[index])
    #     print(a)
    #     c.append(temp[index+1])
    #     b.append(temp[index+2])
    #     printF(a, b, c)


l1 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print("Do you want to see the answers:\n1.) Yes\n2.) No")
cds = int(input("Your choice: "))
if (cds == 1):
    b = True
else:
    b = False
arg(l1, b)
# arithmatic formatter
# def printF(x, y, z, r):  # Printing format(complete)(int,int,str)
#     a = x
#     b = y
#     c = z
#     d = r
#     # print(len(str(a)))
#     # print(len(str(b)))
#     i=0
#     while(i!=len(a)):
# if (len(str(b[i])) > len(str(a[i]))):
#     print(" "*3+str(a[i]))
#     print(f"{c[i]} "+str(b[i]))
#     print("-"*(len(str(b[i]))+2))
#     print(" "*(len(str(d[i]))-len(str(b[i]))+2)+str(d[i]), end="    ")
# elif (len(str(a[i])) > len(str(b[i]))):
#     print("  "+str(a[i]))
#     print(f"{c[i]} "+" "*(len(str(a[i]))-len(str(b[i])))+str(b[i]))
#     print("-"*(len(str(a[i]))+2))
#     print(" "*(len(str(d[i]))-len(str(a[i]))+2)+str(d[i]))
# else:
#     print("  "+str(a[i]))
#     print(f"{c[i]} "+str(b[i]))
#     print("-"*(len(str(a[i]))+2))
#     print(" "*(len(str(d[i]))-len(str(b[i]))+2)+str(d[i]))
# i+=1
