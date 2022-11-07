def time_cal(time, duration):
    placeholders = time.split()
    due = duration.split(":")
    m = []
    t = []
    pl = []
    a = placeholders[0]
    t = a.split(":")
    b = placeholders[1]
    pl.append(b.upper())
    print(t)
    print(due)
    print(pl)
    mins = int(t[1])+int(due[1])
    print(mins)
    if (mins >= 60):
        s = mins/60
        s = str(round(s, 2))
        m = s.split(".")
        print(m)
        hours = int(t[0])+int(due[0])+int(m[0])
        mins=int(m[1])
    else:
        hours = int(t[0])+int(due[0])
    if (hours > 12):
        hours = hours-12
        if (pl[0] == "AM"):
            pl[0] = "PM"
        else:
            pl[0] = "AM"
    print(f"Return: {hours}:{mins} {pl[0]}")


a = input("Enter default time: ")
b = input("Enter time duration: ")
time_cal(a, b)
