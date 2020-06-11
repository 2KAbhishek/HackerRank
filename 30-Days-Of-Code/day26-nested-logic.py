dA, mA, yA = map(int, input().split())
dE, mE, yE = map(int, input().split())

fine = 0

if yA == yE:
    if mA == mE and dA > dE:
        fine = 15 * (dA - dE)
    elif mA > mE:
        fine = 500 * (mA - mE)
elif yA > yE:
    fine = 10000

print(fine)

