import matplotlib.pyplot as plt

students_names=["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]

students_marks=[35,50,20,45,25,40,25,40]

marks_per=[]
for x in students_marks:
    res=(x/50)*100
    marks_per.append(res)

print(marks_per)

def students_marks_line_graph():
    plt.plot(students_names,students_marks)
    plt.title("Student Marks")
    plt.xlabel("name")
    plt.ylabel("marks")
    plt.show()

students_marks_line_graph()

def students_bar_graph():
    plt.bar(students_names,marks_per)
    plt.title("Marks percentage")
    plt.xlabel("name")
    plt.ylabel("marks")
    plt.show()

students_bar_graph()    
