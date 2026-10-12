#Answer 1
n=-5
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

#Answer 2
sides=(3,3,5)
a,b,c=sides
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")

