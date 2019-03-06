email = input("What is your email id?: ").strip()
user = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "your are {} and  your email address is {}".format(user,domain)
print(output)
