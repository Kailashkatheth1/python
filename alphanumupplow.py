if __name__ == '__main__':
    s = input()
    al=up=low=num=0

    for a in s:
        if a.isalpha():
            al+=1
        if a.isupper():
            up+=1
        if a.islower():
            low+=1
        if a.isdigit():
            num+=1
    arr=[al,num,low,up]    
    if(num>0 or al>0) :
        print(True) 
    else:
        print(False) 
    for x in arr:
        if x>0:
             print(True) 
        else:
             print(False)    
