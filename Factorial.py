def fac(num):
    if num ==0:
        return 1
    else:
        return num*fac(num-1)
    
num=int(input("Enter a number:"))
res=fac(num)
print(f"Factorial of {num} is:",res)   