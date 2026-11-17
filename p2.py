#default argument
def greeting(name="guest"):
    print("welcome",name)
greeting("Ashwini")
greeting()

#keyword argument
def student_info(name,age,city):
    print(name,age,city)
student_info(age = 25,name = 'Ashwini',city = "Bangslore")