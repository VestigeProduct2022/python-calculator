print("Simple calculator in python")
a=int(input("enter the value"))
operator=input("ener the operator")
b=int(input("enter the value"))
if operator=='+':
    print(a+b)
    
elif operator=='-':
    print(a-b)
    
elif operator=='*':
    print(a*b)
    
elif operator=='/':
    print(a/b)
    
else:
    print("invalid")