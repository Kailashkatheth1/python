import random
while 1:
    print(".....r=rock....p=paper......s=scissor")
    x1=input("player plays:")
    x=random.randint(0,2)
    ip=['r','p','s']
    x2=ip[x]
    print("computer plays:"+x2) 
    if (x1=='r' and x2=='s') or (x1=='p' and x2=='r') or (x1=='s' and x2=='p'):
             print("you won :)")
    elif (x2=='r' and x1=='s') or (x2=='p' and x1=='r') or (x2=='s' and x1=='p'):
             print("computer  wins :(")
    elif (x1==x2):
             print("************tie**************")
    else :
        print("enter r,p,s only please")
        

             

             
