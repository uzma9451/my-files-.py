a=int(input("enter the number=")) #we take int casting here because we need integers 
b=str(input("enter the symbol=")) # we take str casting here because we need symbols
c=int(input ("enter the number="))# we again take int casting for numbers
if (b=="+"):  # we take condetion in if function for addition
    print("add",a+c) 
elif(b=="-"):  # we again take  condetion in if function for subtraction
    print("sub",a-c)
elif(b=="*"):
    print("multiplication",a*c) #we again take condetion in if function for multiplication
elif(b=="/"):   # we are taking condetion for division)
    print("div",a/c)
elif(b=="%"): # we 
    print("modulus",a%c)
elif(b=="**"):
    print("exponentiation",a**c)
elif(b=="//"):
    print("floor div",a//c)
else:

    print("please enter the valid symbol")
