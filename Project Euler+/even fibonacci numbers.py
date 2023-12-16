import sys

def even_fibonacci(n):
    a = [0]
    for i in range(1,n+1):
        a = a.append(i)
        print(a)
        i += 1
    
    return a

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
print(even_fibonacci(n))