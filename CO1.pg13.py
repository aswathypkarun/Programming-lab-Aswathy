n=int(input("Enter a limit:"))
print("Enter ",n," colour names:")
c=[]
for i in range(0,n):
    c.append(input())
print("The first and last colors are:")
for i in range(0, n):
    print(c[0],c[n-1])
    break
