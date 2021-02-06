c=int(input("Enter the limit:"))
print("\nEnter some numnbers:")
lst=[]
for i in range (0,c):
 lst.append(int(input()))
squared_numbers = [number ** 2 for number in lst]
print("Square of numbers:",squared_numbers)