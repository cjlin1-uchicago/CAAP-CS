def fibonacci():
    a_m = 1
    a_n = 1
    term = eval(input("Which term would you like to know?"))
    if term == 1:
        print(1)
    if term == 2:
        print(1)
    else:
        for x in range(0,term-2):
            a_n, a_m = a_n+a_m, a_n
        print(a_n)
fibonacci()
