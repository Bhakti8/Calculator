def Calculator():
    a=int(input("Give first operand : "))
    b=int(input("Give second operand : "))
    op=input("what operstion would u like to perform  +  -  /  *   : ")
    
    if op not in '+*/-':
        print("Invalid operation")
    if op=='/':
        print("result is c : "+str(a/b))
    if op=='*':
        print("result is c : "+str(a*b))
    if op=='+':
        print("result is c : "+str(a+b))
    if op=='-':
        print("result is c : "+str(a-b))
    calc=input("Do u wanna continue?? y/n") 
    if calc=='y':
        print(Calculator())
    else:
        print("Thankyou!!")
Calculator()    
