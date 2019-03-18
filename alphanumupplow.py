if __name__ == '__main__':
    s = input()
    if s.isalnum():
        print('True')
        print('True')
        print('True')
    
    else:
        print('false')
        print('false')
        print('false')
    for a in s :
        if a.islower()==True:
            p=True
            break
        else:
             p=False 
    print(p)         
    for a in s :
        if a.isupper()==True:
            p=True
            break
        else:
             p=False  
    print(p)                   
