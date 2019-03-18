if __name__ == '__main__':
    s = input()
    al=up=low=num=0
    if s.isalnum():
        print(True)
    else:
        print('False\n'*5)

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
    for x in arr:
        if x>0:
             print(True) 
        else:
             print(False)    
