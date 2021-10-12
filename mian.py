# def find_hcf(x,y):
#     while(y):
#         x , y = y, x % y

#     return x 
while ('y','yes','yep','Y','YES','YEP'):
    ab = input("enter first number:  ")
    ba = input("enter second number:  ")
    if('.' in ab):
        print("First Number should not be float..")
    elif('.' in  ba):
        print("Float not allowed")
    else:

    # while ('y','yes','yep','Y','YES','YEP'):
    
        a = int(ab)
        b = int(ba)

        restart = ('y')


        def find_hcf(x,y):
            while(y):
                x , y = y, x % y

            return x 

        hcf = find_hcf(a,b)
        lcm = (a * b) // hcf
            
        print(f"The Hcf Of {a} and {b} is {hcf}")
        print(f"The Lcm of {a} and {b} is {lcm}")

        restart = input("would you like to calculate again??")
        if restart in ('n', 'no', 'NO', 'N'):
            print("thank you")
            exit()
        elif restart in ('y','yes','yep','Y','YES','YEP'):
            print("restarting..")
            



