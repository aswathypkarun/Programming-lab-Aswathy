#Find sum of elements in list
total = 0
c=int(input("Enter the limit:"))
print("Enter some integers:")
list1=[]
for i in range(0,c):
    list1.append(int(input()))
print("Sum of all elements in the list: ")
for i in list1:
        total = total + i
print(total)