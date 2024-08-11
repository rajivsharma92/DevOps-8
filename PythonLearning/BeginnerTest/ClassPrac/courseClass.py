class Course:
    
    def __init__(self, course_name):
        
        self.course_name = course_name

        self.students = []

    def add_student(self, name):
        if name not in self.students:
            self.students.append(name)
            # print(f"Student named {name}, added to the course")

        else:
            print(f"Student is already enrolled for the course")

    def remove_student (self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"Student named {name} is removed from the course")

    def list_students(self):
        if self.students:
            print(f"Students in the Course:{self.course_name}")
            for name in self.students:
                print(f"- {name}")
        else:
            print("No Student enrolled for this course.")

class OnlineCourse(Course):

    def __init__(self, course_name, platform):
        super().__init__(course_name)
        self.platform = platform

    def list_students(self):
        if self.students:
            print(f"Students enrolled in [{self.course_name}] on [{self.platform}]:")
            for name in self.students:
                print(f"- {name}")
        else:
            print("No students enrolled for this course.")

onlineCourse1 = OnlineCourse('DevOps', 'Online')

onlineCourse1.add_student("Rajiv")
onlineCourse1.add_student('Sundeep')

onlineCourse1.list_students()

onlineCourse1.remove_student('Sundeep')

onlineCourse1.list_students()
