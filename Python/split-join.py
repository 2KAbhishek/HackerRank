def split_and_join(line):
    out = line.split(" ")
    out = "-".join(out)
    return out

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

