sub1=int(input("Enter a Math marks :"))
sub2=int(input("Enter a English marks :"))
sub3=int(input("Enter a hindi marks :"))

sum=sub1+sub2+sub3
marks=sum/3
print("Total maks is = ",marks)

if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
else:
    print("F")