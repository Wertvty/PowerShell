def is_armstrong(number):
    k = int()
    for x in str(number):
        k += int(x)**len(str(number))
    return k == number

