def main():
    time = convert(input("What time is it? "))
    if 7.0 <= time <= 8.00:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("Dinner time")
    else:
        pass


def convert(time):
    #12h support
    if time.endswith("a.m."):
        time = time.replace("a.m.", "")
        h, m = time.split(":")
        m = int(m)/60
        time = float(h) + float(m)
    elif time.endswith("p.m."):
        time = time.replace("p.m.", "")
        h, m = time.split(":")
        m = int(m)/60
        time = float(h) + float(m)
        time = time + 12
    else:
        h, m = time.split(":")
        m = int(m)/60
        time = float(h) + float(m)
    return time

if __name__ == "__main__":
    main()