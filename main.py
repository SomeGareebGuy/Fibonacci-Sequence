# Fibonacci sequence up to Nth term
a = [0, 1]
n = int(input("Insert the number of terms you want to see in Fibonacci sequence : \n"))
u = 0
while u < n-2:
    b = a[len(a)-1] + a[len(a)-2]
    a.insert(len(a), b)
    u += 1
print("The Fibonacci Sequence is : ", a)
input()
