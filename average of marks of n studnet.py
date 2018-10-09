if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    c=0
    s=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l=student_marks[query_name]
    for i in l:
        c+=1
        s+=i    
    a=s/c    
    print("%.2f" % a)
    
