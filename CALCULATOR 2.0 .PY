symbol=str(input("choose the correct symbol please +,-,/,*,**,//,%=",))
a=int(input("enter the value for a=",))
b=str(input("enter the symbol=",))

c=int(input("enter the value for c=",))
if(b=="+"):
    print("add",a+c)
    if(b=="-"):
        print("sub",a-c)
        if(b=="*"):
            print("multiply",a*c)
            if(b=="/"):
                print("div",a/c)