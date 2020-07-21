class Department:
    def __init__(self, dept_name, students_detail, subjects):
        self.dept_name = dept_name
        self.students_detail = students_detail
        self.subjects = subjects

    def student_details(self):
        print("Student Details in", self.dept_name, "department:")
        for student in range(len(self.students_detail)):
            print(self.students_detail[student])

    def dept_subjects(self):
        print("The department subjects offered by", self.dept_name, "department:")
        for subject in range(len(self.subjects)):
            print("      ", self.subjects[subject])

    def print_std_names(self):
        print("Student names of", self.dept_name, "department:")
        for name in self.students_detail:
            print(name[1])


def dept_name(dept_objects, department):
    for dept_object in dept_objects:
        students_list = dept_object.students_detail
        for student in students_list:
            if len(student[2]) > 3:
                list.append(student[1])
    print("student take more than 3 courses : ", set(list))


def overlap_subjects(cse, ece, mech):
    print("The overlapping subjects are", set(cse.subjects).intersection(set(ece.subjects), set(mech.subjects)))


list = []
cse = Department("cse", [[1, "mahi", ["maths", "tlw", "c++"]], [2, "sivva", ["maths", "tlw", "chemistry", "physics"]]],["maths", "tlw", "c++", "chemistry", "physics", "c"])
ece = Department("ece", [[1, "moni", ["c++", "emf", "maths"]], [2, "sas", ["ethics", "emf", "maths"]],[3, "kousi", ["maths", "c++", "ethics", "physics"]]],["physics", "emf", "maths", "c++", "kmm", "ethics"])
mech = Department("mech", [[1, "amirtha", ["electric", "maths", "c++"]], [2, "kalai", ["physics", "c++", "maths"]],[3, "karthi", ["c++", "chemistry", "maths"]]],["electric", "maths", "c++", "physics", "chemistry"])
overlap_subjects(cse, ece, mech)
ece.print_std_names()
department = input("Enter a department to print students list : ")
dept_name([cse, ece, mech], department)
