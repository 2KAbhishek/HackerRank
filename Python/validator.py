if __name__ == '__main__':
    s = input()

    alphaNum = False
    alpha = False
    num = False
    lower = False
    upper = False

    for item in s:
        if item.isalnum() is True:
            alphaNum = True
        if item.isalpha() is True:
            alpha = True
        if item.isdigit() is True:
            num = True
        if item.islower() is True:
            lower = True
        if item.isupper() is True:
            upper = True
    
    print (alphaNum)
    print (alpha)
    print (num)
    print (lower)
    print (upper)

