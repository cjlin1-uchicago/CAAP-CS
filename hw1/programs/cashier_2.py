def cashier_2():
    change = eval(input("How many cents of change do you want?"))
    quarters = eval(input("How many quarters do you have?"))
    dimes = eval(input("How many dimes do you have?"))
    nickels = eval(input("How many nickels do you have?"))
    pennies = eval(input("How many pennies do you have?"))

    q = change//25
    if q <= quarters:
        change = change - 25*q
    else:
        q = quarters
        change = change - 25*q

    d = change//10
    if d <= dimes:
        change = change - 10*d
    else:
        d = dimes
        change = change - 10*d

    n = change//5
    if n <= nickels:
        change = change - 5*n
    else:
        n = nickels
        change = change - 5*n

    p = change
    if p <= pennies:
        p = p
        print("Quarters: ", q)
        print("Dimes: ", d)
        print("Nickels: ", n)
        print("Pennies: ", p)
        print("Total Coins: ", p+n+d+q)
    else:
        p = pennies
        print("Oops! Not enough coins!")
cashier_2()
