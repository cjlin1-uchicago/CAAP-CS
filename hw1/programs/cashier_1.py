def cashier_1():
    change = eval(input("How many cents of change do you want?"))
    q = change//25
    d = (change%25)//10
    n = ((change%25)%10)//5
    p = ((change%25)%10)%5
    print("Quarters: ", q)
    print("Dimes: ", d)
    print("Nickels: ", n)
    print("Pennies: ", p)
    print("Total Coins: ", p+n+d+q)
cashier_1()
