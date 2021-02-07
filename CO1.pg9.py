w=input("Enter a word:")
n=len(w)
for i in range(0,n):
    if i==0:
        print(w[n-1],end="")
    elif i==n-1:
        print(w[0],end="")
    else:
        print(w[i],end="")
