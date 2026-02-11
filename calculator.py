a=float(input("enter a first number : "))
operator=input(" enter a operation (+,-,*,/) :")
b=float(input("enter a second number : "))
if(operator=="+"):
    print("sum:",a+b)
elif(operator=="-"): 
     print("sub:",a-b)
elif(operator=="*"): 
    print("mul:",a*b)
elif(operator=="/"):
    print("div:",a/b)           
else:
    print("invalid")



