
def factfun(n):
        fact=1
        i=1
        if n<0:
              print("Negative number")
        if n==0:
              return 1
        while(i<=n):
            fact=fact*i
            i=i+1
        return fact

n=int(input("Enter a number : "))
x=factfun(n)
print(x)