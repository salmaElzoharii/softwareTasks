n = int(input())
amounts = [200, 100, 50, 20, 10, 5]

for i in range(len(amounts)):
    if n % amounts[i] == 0:
        print(n // amounts[i], "x", amounts[i], end="")
        break
    elif n % amounts[i] < n:
        print(n // amounts[i], "x", amounts[i], "L.E.+ ", end="")
        n = n % amounts[i]

if(n<5):
    print(n,"x 1", end="")
print(" L.E.")






