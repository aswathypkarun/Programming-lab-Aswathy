#Area using lambda functions
square=lambda x :x*x
rect=lambda x,y :x*y
tri=lambda x,y :1/2*x*y
m=int(input('Enter the first number : '))
print("Area of square:",square(m))
m=int(input('Enter the first number : '))
n=int(input("Enter the second number :"))
print("Area of rectangle:",rect(m,n))
m=int(input('Enter the first number : '))
n=int(input("Enter the second number :"))
print("Area of triangle:",tri(m,n))
