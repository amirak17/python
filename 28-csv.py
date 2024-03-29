

# name, home
# Harry, "Number Four, Privet Drive"
# Ron, The Burrow 
# Draco, Malfoy Manor 


import csv 

students = [] 

with open("students.csv") as file: 
    reader = csv.reader (file) 
    for name, home in reader: 
        students.append({"name": name, "home": home}) 

for student in sorted (students, key=lambda student: student ["name"]):
    print(f" {student ['name']} is from {student ['home']}")



# ///
    
import csv 

students = [] 

with open("students.csv") as file:
    reader = csv. DictReader(file)
    for row in reader : students.append({"name": row["name"], "home": row["home"]}) 
    
    
for student in sorted (students, key=lambda student : student ["name"]): 
    print (f" {student ['name']} is from {student ['home']}")

# ///
    
import csv 

name = input("What's your name? ") 
home = input("Where's your home? ") 

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({ "name": name, "home": home })
