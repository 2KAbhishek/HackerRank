def swap_case(s):
    out = ""
    for char in s:
        if char.islower():
            out += (char.upper())
        else:
            out += (char.lower())
            
    return out
    # return s.swapcase()

    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

