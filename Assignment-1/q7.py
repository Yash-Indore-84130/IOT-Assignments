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


for n in range(10):
    x=factfun(n)
    print(x)