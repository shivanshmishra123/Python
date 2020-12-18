""""
Dekho bhai agar hume kisi school ke members ka data banana hai to hume different attriutes rkhne honge
Jaise Teacher,Student,Accountant ese teen log kisi school mei honge to teacher ki salary hogi magar 
Bacche ki nhi ese hi kuch properties baccho ki hongi magar accountant ki nhi 
ese mei hi zaroorat padti hai object Oriented progamming kii jisme hum cheeze repeat nhi krte 
aur cheezo ko systematic rkhte hai 
"""

# Class
"""
Class ek tarah ka template hai .... Jaise agar hume chutti ka letter bohut frequently banana padta
hai to mai ek letter type kr lunga jisme mai bas Date,Name,Reason in sab ko blank chhod dunga
issi ko hum Class bhi bol skte hai jisse humara time bachega and as we all know that Time is 
money and money is time 
"""

# Instance 
"""
Ek instance wo hua jo humne uss template se letter banaya ... Jaise agar Harry,Larry,marry teeno
ko ek leave letter banana hai to unhone apne avyashakta anusaar values input kii or ek letter 
prapt kiya jo doore se alag hai to Harry ka letter , Larry ka , Marry ka sab ek Instance hai 
"""

# First Class

class Student:
    pass

# harry aur larry humare do instances hue 
harry = Student()
larry = Student()

# Aur jab humne ussi instance ke variable bana diye to wo kehlata hai Instance Variable 
# Jaise ki name , cls,school

harry.name = "Shivansh Mishra"
harry.cls = "9"
harry.school = "BVBPS"

larry.name = "Dev"
larry.cls = "10"
larry.school = "DPS"

print(f"Student 1 details are as follows:\n Name = {harry.name}\n Class = {harry.cls}\n School = {harry.school}")
print(f"\nStudent 2 details are as follows:\n Name = {larry.name}\n Class = {larry.cls}\n School = {larry.school}")
