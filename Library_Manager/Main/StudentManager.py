from DatabaseInteractor.DAO.BookDAO import BookDAO
from DatabaseInteractor.DAO.StudentDAO import StudentDAO
from DatabaseInteractor.DAO.time_stamper import Watch
from DatabaseInteractor.DTO.DataPacker import DataPacker


class StudentManagement:
    def __init__(self):
        self.StudentDAO = StudentDAO()
        self.BookDAO = BookDAO()

    @staticmethod
    def extra_fine(x):

        c = x.split("|")
        try:
            c.remove('')
        except ValueError as e:
            pass
        t = Watch.time_stamp()
        k = 0
        for i in c:
            j = i.split("_")
            k += (t - int(j[1]))

        return DataPacker(k)

    def invoke_student_registration(self):
        student_details = self.get_student_details()
        self.StudentDAO.register_a_student(student_details)
        print("ID: ", end="")
        print(self.StudentDAO.get_recent_SID().one[0][0])
        y = input("Press enter to continue...")

    def get_student_details(self):
        name = input("Enter the student's name: ")
        roll_no = int(input("Enter the institute roll no: "))
        department = input("Enter department name ex: ECE:  ")
        gender = input("Gender: ")
        mobile = int(input("Enter mobile: "))
        regtime = Watch.time_stamp()
        return DataPacker(name, roll_no, gender, department, mobile, regtime)

    def get_student_info(self):
        SID = int(input("Enter the student ID: "))
        info = self.StudentDAO.get_student_info(SID)
        if not info.one:
            print("No student details with this ID exists.")
            y = input("Press enter to continue...")
            return None
        else:
            print("Student ID: ", info.one[0][0])
            print("Name: ", info.one[0][1])
            print("Roll no: ", info.one[0][2])
            print("Gender: ", info.one[0][3])
            print("Department: ", info.one[0][4])
            print("Mobile no: ", info.one[0][5])
            print("No of book(s) issued: ", info.one[0][7])
            print("Fine: Rs", info.one[0][9])
            print("Fine paid: Rs.", info.one[0][10])
            info.two = self.extra_fine(info.one[0][8]).one
            print("Ongoing extra Fine Rs.", info.two)

            y = input("Press enter to continue...")
            return info

    def Invoke_delete_student(self):
        info = self.get_student_info()
        if not info:
            pass
        elif info.one[0][9] - info.one[0][10] == 0 and info.two == 0:
            self.StudentDAO.delete_student(info.one[0][0])
            print("The Student got Deleted successfully.")
            y = input("Press enter to continue...")
        elif info.one[0][9] - info.one[0][10] + info.two != 0:
            print("This student is yet pay some more fine or even return a book.")
            y = input("Enter y to force delete the student ID | press enter to Cancel")
            if y == 'y' or y == 'Y':
                self.StudentDAO.delete_student(info.one[0][0])
                print("The Student got Deleted successfully.")
                y = input("Press enter to continue...")
            else:
                print("Request cancelled...")
                y = input("Press enter to continue...")
        else:
            print("Something went wrong...")
            y = input("Press enter to continue...")

    def Invoke_active_SID(self):
        n = self.StudentDAO.all_active_SID()
        m = self.StudentDAO.get_recent_SID()
        print("The number of active student Registrations are: ", m.one[0][0] - len(n.one))
        y = input("Press enter to continue...")

    def Invoke_fine_payment(self):
        info = self.get_student_info()
        payment = int(input("Enter the amount paid: Rs."))
        payment += info.one[0][10]
        info.two = payment
        self.StudentDAO.update_student_fine(info)
        print("Student Fine has been paid successfully.")
        y = input("Press enter to continue...")

    def main_panel(self):
        s = True
        while s:

            print("====> Student Management <====")
            print("Enter 1 to register a New Student into the Library.")
            print("Enter 2 to issue a Book to a Student.")
            print("Enter 3 to get student details using ID.")
            print("Enter 4 to delete a Student from the Library.")
            print("Enter 5 to see total number of active ID.")
            print("Enter 6 for Fine payment using Student ID.")
            print("Enter b to go back to previous menu.")

            x = input()
            if x == 'b' or x == 'B':
                s = False
            elif x == '1':
                self.invoke_student_registration()

            elif x == '2':
                print("Please go to Book Management menu")
                y = input("Press enter to continue...")

            elif x == '3':
                self.get_student_info()

            elif x == '4':
                self.Invoke_delete_student()

            elif x == '5':
                self.Invoke_active_SID()

            elif x == '6':
                self.Invoke_fine_payment()
