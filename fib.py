def fib(n):
    
    a = int(input("enter the value a:"))
    b = int(input("enter the value of b:"))

    print(a)
    print(b)
    
    for i in range(2,n) & n<100 :
            
            c = a + b
            a = b
            b = c
            print(c)
        
        

