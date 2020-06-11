import re

n = int(input())
PATTERN = re.compile(r"@gmail\.com$")
gmailUsers = []

for _ in range(n):
    name, email = input().split()

    if PATTERN.search(email):
        gmailUsers.append(name)

for name in sorted(gmailUsers):
    print(name)

