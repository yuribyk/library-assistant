from DatabaseInteractor.DAO.BookDAO import BookDAO
from DatabaseInteractor.DAO.StudentDAO import StudentDAO
from DatabaseInteractor.DAO.time_stamper import Watch
from DatabaseInteractor.DTO.DataPacker import DataPacker


class BookManagement:
    def __init__(self):
        self.BookDAO = BookDAO()
        self.StudentDAO = StudentDAO()
        self.Watch = Watch()

    def invoke_book_registration(self):
        book_details = self.get_book_details()
        BID = self.BookDAO.register_a_book(book_details)
        if not BID:
            print("The registration was unsuccessful, please try again...")
            y = input("Press enter to continue...")
        else:
            print("Book was registered successfully.")
            print("Book ID: ", BID.one[0][0])
            y = input("Press enter to continue...")

    @staticmethod
    def get_book_details():
        title = input("Enter the title of the book: ")
        department = input("Enter department name ex: ECE:  ")
        author = input("Enter the author name: ")
        type_of_book = input("Enter book type v/r: ")
        regtime = Watch.time_stamp()
        return DataPacker(title, author, type_of_book, department, regtime)

    def invoke_issue_book(self):
        validated_data = self.validate_SID_BID()
        if not validated_data:
            pass
        else:
            n = self.BookDAO.out_book_tally()
            if not n.one:
                validated_data.four = 1
                validated_data.seven = 1
            else:
                validated_data.four = n.one[0][3] + 1
                validated_data.seven = n.one[0][2] + 1

            self.BookDAO.issue_a_book(validated_data)
            print("This has been successfully Issued to the Student.")
            y = input("Press enter to continue...")

    @staticmethod
    def collect_SID_BID():
        SID = int(input("Enter the student ID: "))
        BID = int(input("Enter the book ID: "))
        return DataPacker(SID, BID)

    def validate_SID_BID(self):
        group = self.collect_SID_BID()
        y = self.StudentDAO.get_student_info(group.one)
        if not y.one:
            print("Student with this ID does not exists.")
            y = input("Press enter to continue...")
            return None
        elif y.one[0][6] == 0:
            print("This Student ID is in Delete status.")
            y = input("Press enter to continue...")
            return None
        else:
            z = self.BookDAO.get_book_info(group.two)
            if not z.one:
                print("Book with this ID does not exists.")
                y = input("Press enter to continue...")
                return None
            else:
                if y.one[0][7] >= 7:
                    print("This student has already issued 7 books.")
                    y = input("Press enter to continue...")
                    return None
                elif type(z.one[0][6]) is int:
                    print("This book is already issued.")
                    y = input("Press enter to continue...")

                    return None
                elif z.one[0][3] == 'r':
                    print("This book is only for reference. Please select another book.")
                    y = input("Press enter to continue...")

                    return None
                elif z.one[0][3] == 'd':
                    print("This book has been deleted. Please choose another book.")
                    y = input("Press enter to continue...")

                    return None
                else:
                    group.three = Watch.time_stamp()
                    group.six = y.one[0][7] + 1
                    group.five = y.one[0][8]
                    return group

    @staticmethod
    def string_changer(a, b):
        c = a.one[0][8].split("|")
        b = str(b)
        try:
            c.remove('')
        except ValueError as e:
            pass
        k = -1

        for i in c:
            j = i.split("_")
            k += 1
            if j[0] == b:
                break
        try:
            c.pop(k)
        except IndexError as e:
            pass

        d = "|".join(c)
        return DataPacker(a.one[0][7] - 1, d)

    def invoke_return_book(self):
        BID = int(input("Enter the book ID: "))
        book_info = self.BookDAO.get_book_info(BID)
        if not book_info.one:
            print("This book ID does not exist.")

            y = input("Press enter to continue...")

        elif not book_info.one[0][6]:
            print("This book is not issued! and already inside the library. ")

            y = input("Press enter to continue...")

        else:
            book_info.four = self.Watch.time_stamp()
            time_lapsed = book_info.four - book_info.one[0][8]
            # charges = Rs.2 per minute

            stud_details = self.StudentDAO.get_student_info(book_info.one[0][6])
            book_info.two = (time_lapsed // 60) * 2 + stud_details.one[0][9]
            print("The book fine is Rs.", book_info.two)
            SID_updates = self.string_changer(stud_details, book_info.one[0][0])
            book_info.three = self.BookDAO.out_book_tally().one[0][3] - 1
            self.BookDAO.return_a_book(book_info, SID_updates)
            print("The book has been successfully Returned the Library.")

            y = input("Press enter to continue...")

    def Invoke_book_details(self):
        BID = input("Enter the book ID: ")
        details = self.BookDAO.get_book_info(BID)

        if not details.one:
            print("No Book with this ID exists.")

            y = input("Press enter to continue...")
            return 0
        else:
            print("Book ID: ", details.one[0][0])
            print("Title: ", details.one[0][1])
            print("Author: ", details.one[0][2])
            print("Type: ", details.one[0][3])
            print("Department: ", details.one[0][4])
            print("Book status: ", end="")
            if not details.one[0][6] and details.one[0][3] == 'v':
                print("Avialable for Issue")

                y = input("Press enter to continue...")
                return 1
            elif details.one[0][3] == 'd':
                print("This book has been Deleted.")

                y = input("Press enter to continue...")
                return 2
            else:
                print("Issued to student ID: ", details.one[0][6])

                y = input("Press enter to continue...")
                return 3

    def Invoke_delete_book(self):
        BID = self.Invoke_book_details()
        if BID == 0:
            pass
        elif BID == 1:
            confirm = input("Enter y to confirm delete | Enter n to cancel: ")
            if confirm == 'y' or confirm == 'Y':
                self.BookDAO.delete_a_book(BID)
                print("The book got Deleted successfully.")
                y = input("Press enter to continue...")
            else:
                print("Request got cancelled.")
                y = input("Press enter to continue...")
        elif BID == 2:
            pass

        elif BID == 3:
            print("This book is presently issued to a student.")
            confirm = input("Enter y to confirm delete | Enter n to cancel: ")
            if confirm == 'y' or confirm == 'Y':
                self.BookDAO.delete_a_book(BID)
                y = input("Press enter to continue...")
            else:
                print("Request got cancelled.")
                y = input("Press enter to continue...")
        else:
            print("Request got cancelled.")
            y = input("Press enter to continue...")

    def invoke_active_books(self):
        max = self.BookDAO.get_recent_BID()
        d = self.BookDAO.get_delete_BID()
        r = self.BookDAO.get_reference_BID()
        print("The total number of books in Library = ", max.one[0][0] - len(d.one))
        print("The total number of vendable books = ", max.one[0][0] - len(d.one) - len(r.one))
        print("The total number of reference books = ", len(r.one))
        print("The total number of deleted books = ", len(d.one))

        y = input("Press enter to continue...")

    def create_default_tables(self):
        self.BookDAO.create_default_tables()

    def main_panel(self):

        s = True
        while s:

            print("====> Book Management <====")
            print("Enter 1 to register a New Book into the Library.")
            print("Enter 2 to issue a Book.")
            print("Enter 3 to return a Book.")
            print("Enter 4 to delete a Book from the Library.")
            print("Enter 5 to get book details using book ID.")
            print("Enter 6 to get recent BID.")
            print("Enter 7 to get total active books.")
            print("Enter b to go back to previous menu.")

            x = input()
            if x == 'b' or x == 'B':
                s = False
            elif x == '1':
                self.invoke_book_registration()

            elif x == '2':
                self.invoke_issue_book()

            elif x == '3':
                self.invoke_return_book()

            elif x == '4':
                self.Invoke_delete_book()

            elif x == '5':
                self.Invoke_book_details()

            elif x == '6':
                bid = self.BookDAO.get_recent_BID()
                print("The recently registered book's ID is: ", end="")
                if not bid.one:
                    print("No book registrations yet.")

                else:
                    print(bid.one[0][0])

                y = input("Press enter to continue...")

            elif x == '7':
                self.invoke_active_books()



