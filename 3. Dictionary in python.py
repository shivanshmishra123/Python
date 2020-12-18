# Dictionary is nothing but key value pairs
# Dictionary hum tab uss kr skte hai jab humare object ka direct answer ho jaise:- "Shivansh":"15" isme isne age batayi
# In the d2 we made Shubham's Column have so many entries as we have included dictionary in dictionary

# Example of a Dictionary
d2 = {"Harry":"Burger","Rohan":"Fish","SkillF":"Roti","Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}

# Calling a dictionary Item
# Deleting a Item from a dictionary
del d2["Harry"]
print(d2)

# Adding a Item in a Dictionary
d2.update({"Leena":"Toffee"})
print(d2)

# Printing only the Keys
print(d2.keys())
