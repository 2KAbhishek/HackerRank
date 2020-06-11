def print_rangoli(size):
    # import string
    # alpha = string.lowercase
    alpha = "abcdefghijklmnopqrstuvwxyz"[:size]

    for i in range (size - 1, -size, -1):
        x = abs(i)
        pat = alpha[size:x:-1]+alpha[x:size]
        print("--"*x + "-".join(pat) + "--"*x)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)