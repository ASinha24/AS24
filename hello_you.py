name=input("what is your name?: ")
age=input("how old are you?: ")
city=input("what city you live in?: ")
love=input("what do you love doing?: ")
string="Your name is {} and you are {} year old. You live in {} and you love {}."
output=string.format(name,age,city,love)
print(output)
