print('Add the numbers from 0 to X. What value of X do you like?')
X = int(input()) + 1

total = 0
for num in range(X):
    total = total + num
print(total)
