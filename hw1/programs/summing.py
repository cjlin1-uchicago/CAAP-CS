def summing():
    sum = 0
    total = eval(input("How many numbers will you input? "))
    for x in range(0, total):
        f = eval(input("Enter number: "))
        sum = f + sum
    print(sum)
summing()
