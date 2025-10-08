while True:
    def Zero_Division_Error(num1, num2):
        if num2 == 0:
            print("Second entered cannot be zero")
        else: 
            dv = num1/num2
            print(dv)
            return dv
    


    n1 = int (input("Enter your first number:"))
    n2 = int (input("Enter your second number:"))
    Zero_Division_Error(num1= n1, num2=n2)
    if n2 !=0:
        break
