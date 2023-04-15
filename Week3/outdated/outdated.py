months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#input user -> check if input is valid format
#valid format: 9/8/1636, September 8, 1636
while True:
    date = input("Date: ")

    try:
        m, d, y = date.split("/")
        m = m.strip()
        d = d.strip()
        y = y.strip()
        if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
            break

    except:
        try:
            alt_m, alt_d, y = date.split(" ")
            for month in range(len(months)):
                if alt_m == months[month]:
                    m = month + 1
            if alt_d.find(",") == -1:
                continue
            d = alt_d.replace(",", "")

            if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                break
        except:
            print()
            pass

print(f"{y}-{int(m):02}-{int(d):02}")
