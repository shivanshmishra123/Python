import random #Is line ki madat se humne random fuction ko le aaya

# Bringing a Random integer between two no.
random_no = random.randint(0,100)
print(random_no)

#Bringing a Random decimal no.  
rand = random.random() * 100 # "*100" ka matlab hai hume 100 ke andar koi no chahiye
print(rand)

# Bringing a choice from fixed no. or Things
list = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(list)
print(choice)
  
