if __name__ == '__main__':
    s = input()
    if s.isalnum()==False:
        print('false\n'*5)
       
    
    else:
        print('True')
        print('True')
        print('True')
       
    for a in s :
        if a.islower()==True and a.isalpha()==True:
            p=True
            break
        else:
            p=False 
    print(p)         
    for a in s :
        if a.isupper()==True and a.isalpha()==True:
            p=True
            break
        else:
            p=False  
    print(p)                   


