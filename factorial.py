#factorial Example

choice='y'
def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1); 
while choice == 'Y' or choice == 'y' :
    number=int(input("enter a number, you wish to get the factorial").strip())
    print("The factorial of a number is: ")
    print (factorial(number))
    choice=input("do you want to continue(Y/N): ")
      
    
