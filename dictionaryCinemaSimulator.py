films={
    "Harry Potter":{"Age":3, "seat":5},
    "Despicable me":{"Age":18, "seat":5},
    "Thor":{"Age":15, "seat":5},
    "Avengers":{"Age":12, "seat":5},
    "50 shades of gray":{"Age":19, "seat":5}
    }
while True:
    choice=input("what film would you like to watch? :  ").strip().title()
    if choice in films:
        cust_Age=int(input("How old are you?:").strip())
        if cust_Age >= films[choice]["Age"]:
            num_seats=films[choice]["seat"]
            if num_seats >0:
                print("enjoy the film.....")
                films[choice]["seat"]=films[choice]["seat"]-1
            else:
                print("we are sold out!...")
        else:
            print("you are too young to see that film..")
    else:
        print("We don't have that film......");
                        
   
   
       
       
             
             
       
           
    
                      

    
