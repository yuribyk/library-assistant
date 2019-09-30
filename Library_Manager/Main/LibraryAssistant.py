from Main.BookManager import BookManagement
from Main.StudentManager import StudentManagement


class LibraryAssistant:

    def __init__(self):
        self.StudentManager = StudentManagement()
        self.BookManager = BookManagement()

    def invoke_student_management(self):
        self.StudentManager.main_panel()

    def invoke_book_management(self):
        self.BookManager.main_panel()

    def invoke_make_table(self):
        self.BookManager.create_default_tables()


if __name__ == "__main__":
    Library_Assistant = LibraryAssistant()
    s = True

    while s:

        print("====> Welcome to Library Management System  <====")

        print("Enter 1 for Book Management [ issue books, return books etc. ]")
        print("Enter 2 for Student Management [ student info, fine paymnet etc. ]")
        print()
        print("Enter n to create library default tables.")
        print("Enter x to exit.")
        print("Input: ")

        x = input()
        if x == 'x' or x == 'X':
            s = False
            print("Have a nice day... Bye")

        elif x == '1':
            Library_Assistant.invoke_book_management()
        elif x == '2':
            Library_Assistant.invoke_student_management()
        elif x == 'n':
            Library_Assistant.invoke_make_table()