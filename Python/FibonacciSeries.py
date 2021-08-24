# Generating Fibonacci Series by Python

a = [1, 1]
n = 2

while n<10 : # length = 10
    a.append(a[n-2] + a[n-1])
    n += 1

print(a)