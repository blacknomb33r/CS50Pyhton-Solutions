#dict for grovcery list
#str method .upper() for Keys

grocery =   {

            }


while True:
    try:
        user = input("").upper()
        if user in grocery:
            grocery[user] = grocery[user] + 1
        else:
            grocery[user] = grocery.get(user, 1)


    except EOFError:
        #sort keys
        keys = list(grocery.keys())
        keys.sort()
        s_grocery = {i: grocery[i] for i in keys}
        for v, k in s_grocery.items():
           print(k, v)
        break

