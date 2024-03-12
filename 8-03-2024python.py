n=121

temp=n
rev=0

while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10

if temp==rev:
    print("yes")

or

n=121
temp=str(n)

rev=temp[::-1]


if temp==rev:
    print("palidrome")
else:
    print("no")
