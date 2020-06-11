if __name__ == '__main__':
    marksheet = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores += [score]
        marksheet += [[name, score]]
    
    second_max = sorted(list(set(scores)))[1]

    for name, score in sorted(marksheet):
        if score == second_max:
            print(name)
