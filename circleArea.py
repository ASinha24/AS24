def areaOfCircle(radius):
    radius=int(input("enter radius").strip())
    PI=3.14
    return PI*radius*radius

def primenumber(start,end):
    for val in range(start, end+1):
        if val >1:
            for n in range(2, val):
                if val % n == 0:
                    exit
                else:
                    print(val)
        else:
            print("1 is not prime number")

primenumber(2,20)

#print("area of circle", areaOfCircle(radius))


