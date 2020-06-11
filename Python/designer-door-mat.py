height, width = map(int,(input().split()))

pattern = ""

for i in range(height//2):
        patA = ".|." * ((2*i)+1)
        pattern += (patA.center(width, "-")) + "\n"

welcome = "WELCOME".center(width,"-")

print(pattern + welcome + pattern[::-1])
