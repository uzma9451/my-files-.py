a=int(input("enter the number="))
b=str(input("enter the symbol="))
c=int(input ("enter the number="))
if (b=="+"):
    print("add",a+c)
elif(b=="-"):
    print("sub",a-c)
elif(b=="*"):
    print("multiplication",a*c)
elif(b=="/"):
    print("div",a/c)
elif(b=="%"):
    print("modulus",a%c)
elif(b=="**"):
    print("exponentiation",a**c)
elif(b=="//"):
    print("floor div",a//c)
else:
    print("please enter the valid symbol")