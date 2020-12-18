#Read Mode 
f = open("shivansh.txt", "r") #Open ka matlab hai humne bata diya ki uss file ka use hone waala hai aur "r" matlab mode hai
print(f.readlines()) # iss line mei f(jisme humne uss file ko store kiya hai) ko read kr liya hai aur print kr diya

# Second tareeka ye bhi hai ki f.read ko bhi pehle variable mei store kro
content = f.read()
print(content)
f.close()

# Write Mode (Iss mode ki ek problem hai ki ye previous material hata deta hai)
x = open("shivansh.txt","w")
material = x.write("Hi I am shivansh")
print(material)
x.close()

#Create Mode
a = open("shivansh2.txt","x")
material = a.write("Hi Shibboo")
print(material)
a.close()

#Append Mode
b  = open("shivansh.txt","a")
material = b.write("\n Hi Shibo")
print(material)
b.close()


  
