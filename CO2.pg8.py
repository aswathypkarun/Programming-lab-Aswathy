#Return length of longest word
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter word " + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with longest length is:",temp)
print("Length of ",temp," is",len(i))
