def x(a, b): 
    if a==1 and b==0:
        return 1 
    elif a==1 or a==b:
        return 1    
    else:
        return x(a-1, b)*b+x(a-1, b-1); 
print(x(4,1)+x(4,2)+x(4,3)+x(4,4))