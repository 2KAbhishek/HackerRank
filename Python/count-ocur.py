def count_substring(string, sub_string):
    count, pos = 0, 0
    
    while pos < len(string):
        nextPos = string.find(sub_string, pos)
        if nextPos >= 0:
            pos = nextPos + 1
            count += 1
        else:
            break

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

