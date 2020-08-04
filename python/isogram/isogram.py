def is_isogram(string):
    dic = {}
    for k in string:
        if k.isalpha():
            if k.lower() not in dic:
                dic[k.lower()] = 1
            else:
                return False
    return True