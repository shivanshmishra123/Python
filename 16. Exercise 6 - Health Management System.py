# Iss prooject mei humare pass teen clients hai --- Harry,Shivansh and Rohan
# In teeno clients ki health ki zimmedari humare upar hai --- we are acting as a fitness trainer
# Hume in total milakar 6 file banani hai(2 each(1 for food and 2 for Exercise))
# in files mei humko read ya write krna hai ki unhone kab kya khaya hai 


def getdate():
    import datetime
    return datetime.datetime.now

user = ["Harry","Shivansh","Rohan"]
actions = ["Food_taken","Exercise_done"]
l_r = ["Log","Retrieve"]

  
client = int(input("Press 1 for Harry, 2 for Shivansh and 3 for Rohan\n"))
if client == 1:
    client = user[0]
elif client == 2:
    client = user[1]
elif client == 3:
    client = user[2]


action = int(input("Press 1 for Food and 2 for Exercise\n"))
if action == 1:
    action = actions[0]
elif action == 2:
    action = actions[1]


filename = str(client)+"_"+str(action)+".txt"

lorr = int(input("Press 1 for Log and 2 for Retrive\n"))
if lorr == 1:
    lorr = l_r[0]
    foodtaken = input("What "+ action + "by "+client)
    f = open(filename , "w")
    print(f.write(foodtaken))
    f.close()

elif lorr == 2:
    lorr = l_r[1]
    x = open(filename,"r")
    print("The "+action + " by "+client + " are:")
    print(x.readlines())


    
    