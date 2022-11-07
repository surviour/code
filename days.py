def hours(a):
    hours=str(round(int(a)/24,2))
    print(hours)
    h=hours.split(".")
    hours=h[0]
    print(h)
    h3=round(0.01*float(h[1]),2)
    print(h3)
    h3=h3*24
    h=str(h3).split('.')
    h.append(hours)
    print(h)
hours("119")