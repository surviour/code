def mins(mins):
    mins=int(mins)
    if (mins >= 60):
        s = mins/60
        s = str(round(s, 2))
        m = s.split(".")
        print(m)
        hours = m[0]
        mins = m[1]
        m.append(hours)
        m.append(mins)
        return m
    else:
        m.append(0)
        m.append(mins)
        return m


m=mins("70")
print(m)

