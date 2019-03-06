def simpleInterest(p,r,t):
    return int((p*r*t)/100)
def compoundInterest(p,r,t):
    return int(p*(pow((1+r/100),t)))

principal=int(input("enter principal amount: ").strip())
time=int(input("enter time: ").strip())
rate=int(input("enter rate: ").strip())
print("SI", simpleInterest(principal,time,rate))
print("CI", compoundInterest(principal,time,rate))
