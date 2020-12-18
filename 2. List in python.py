# Iss video mein hum seekhenge ki kaise LIST banate hai / Arrays banate hai
#Note ;- Jub bhi tumhare program mei bohut saare variables ho jaaye to sabko array mei daal dena chahiye

# Example of List
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi","Lollypop", 56]

# How to call a LIST
print(grocery[5])

#  Adding a object at the end of the List
grocery.append("Shivansh")
print(grocery)

# Adding a object at a specified place
# Syntax : - listname.inset(index no where to insert , what to insert)
grocery.insert(2, 67)
print(grocery)

# Removing a object from a List
grocery.remove("Harpic")


