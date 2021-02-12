#factorial of given no
num=int(input("Number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of the given no is", fact)