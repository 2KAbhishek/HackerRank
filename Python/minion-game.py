def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)def minion_game(string):
    vowel =['A','E','I','O','U']
    stuScr, kevScr = 0, 0
    for i in range(len(string)):
        if string[i] in vowel:
            kevScr+= len(string)-i
        else:
            stuScr+=len(string)-i
            
    if stuScr>kevScr:
        print("Stuart" + " " + "%d" % stuScr)
    elif kevScr>stuScr:
        print("Kevin" + " " + "%d" % kevScr)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)