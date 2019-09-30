from DatabaseInteractor.DatabaseUtilities import DataBaseUtilities
from DatabaseInteractor.QueryConstants import queries


class StudentDAO:
    def __init__(self):
        self.db_object = DataBaseUtilities()

    def register_a_student(self, n):
        query = queries.insert_into_student % (n.one, n.two, n.three, n.four, n.five, n.six)
        self.db_object.update_data(query)
        query2 = queries.get_recent_SID
        print("Student was registered successfully.")
        return self.db_object.get_info(query2)

    def get_recent_SID(self):
        query = queries.get_recent_SID
        return self.db_object.get_info(query)

    def get_student_info(self, SID):
        query = queries.get_details_SID % SID
        return self.db_object.get_info(query)

    def delete_student(self, SID):
        query = queries.delete_student % SID
        self.db_object.update_data(query)

    def all_active_SID(self):
        query = queries.active_SID
        return self.db_object.get_info(query)

    def update_student_fine(self, info):
        query = queries.update_fine_student % (info.two, info.one[0][0])
        self.db_object.update_data(query)
