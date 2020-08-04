def verify(isbn):
    l = int()
    counter = 10
    if len("".join(isbn.split('-'))) != 10:
        return False
    else:
        for k in isbn:
            try:
                if k == '-':
                    continue
                elif k == "X" and 'X' == isbn[-1]:
                    l+=10
                elif int(k) not in range(10):
                    return False
                else :
                    l+=int(k)*counter
                    counter-=1
            except ValueError:
                return False
        return l%11==0
         
