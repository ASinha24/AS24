number=int(input("enter a number").strip())
def isArmstrong(number):
    temp=number
    sum1=0
    while number !=0:
        r=int(number%10)
        sum1=int(sum1+r*r*r)
        number=int(number/10)
    return (sum1==temp)

if isArmstrong(number):
    print("Armstrong number")
else:
    print("not an Armstrong number")
    
