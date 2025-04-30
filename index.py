import numpy as np

data_type= [("name",'S15'),("class",int),("height",float)]

student_details= [
    ("James",5,48.5),
    ("Nail",6,52.5),
    ("Paul",5,60.5),
    ("Pit",5,48.2)

]

student= np.array(student_details,dtype=data_type)

print("Original Array")
print(student)

print("Sorted by height")
print(np.sort(student,order= "height"))
