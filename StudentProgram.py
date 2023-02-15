import StudentClass as sc


studentid = input('Enter Student ID: ')
name = input('Enter Student Name: ')
dob = input('Enter Student Date of Birth: ')
classif = input('Enter Student Classification: ')

student1 = sc.Student(studentid, name, dob, classif)

student1.calc_age()

student1.calc_register()

print(f"Student age is: {student1.get_age()}")
print(f"Studnet can register between {student1.get_register()}")
