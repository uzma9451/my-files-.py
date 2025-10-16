symbol=str(input("choose the correct symbol please +,-,/,*,**,//,%=",))#we take input from user in symbols
a=int(input("enter the value for a=",))       #we take int casting here because we need nmuber here for performing program)
b=str(input("enter the symbol=",))

c=int(input("enter the value for c"))
if(b=="+"):
    print("add",a+c)
    if(b=="-"):
        print("sub",a-c)
        if(b=="*"):
            print("multiply",a*c)
            if(b=="/"):
                print("div",a/c)
                 if(b=="%"):
                     print("modulus",a%b)
                      if(b=="**"):
                         print("exponentiation",a**b)
                          if(b=="//"):
                              print("floor div",a//b)
