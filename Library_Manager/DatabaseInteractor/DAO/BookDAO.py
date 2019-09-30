import pymysql

from DatabaseInteractor.DatabaseUtilities import DataBaseUtilities
from DatabaseInteractor.QueryConstants import queries


class BookDAO:
    def __init__(self):
        self.db_object = DataBaseUtilities()

    def register_a_book(self,book_details):
        query = queries.insert_into_library % (book_details.one, book_details.two, book_details.three, book_details.four, book_details.five)
        self.db_object.update_data(query)
        query2 = queries.get_recent_BID
        return self.db_object.get_info(query2)

    def get_recent_BID(self):
        query = queries.get_recent_BID
        return self.db_object.get_info(query)

    def get_book_info(self, BID):
        query = queries.get_details_BID % BID
        return self.db_object.get_info(query)

    def issue_a_book(self, data):
        query = queries.issue_from_library % (data.one, data.two, data.four, data.three)
        self.db_object.update_data(query)
        query2 = queries.update_issued_book % (data.one, data.three, data.seven, data.two)
        self.db_object.update_data(query2)
        query3 = queries.update_issued_student % (data.six, str(data.two) + "_" + str(data.three) + "|" + data.five, data.one)
        self.db_object.update_data(query3)

    def return_a_book(self, book_info, s_info):
        query = queries.update_issued_book % ('NULL', 'NULL','NULL', book_info.one[0][0])
        self.db_object.update_data(query)
        query2 = queries.update_issued_student2 % (s_info.one, s_info.two, book_info.two, book_info.one[0][6])
        self.db_object.update_data(query2)
        query3 = queries.issue_from_library % (book_info.one[0][6], book_info.one[0][0], book_info.three, book_info.four)
        self.db_object.update_data(query3)


    def out_book_tally(self):
        query = queries.get_recent_out_book_tally
        return self.db_object.get_info(query)

    def delete_a_book(self, BID):
        query = queries.delete_book % BID
        self.db_object.update_data(query)

    def get_delete_BID(self):
        query = queries.active_BID_d
        return self.db_object.get_info(query)

    def get_reference_BID(self):
        query = queries.active_BID_r
        return self.db_object.get_info(query)

    def create_default_tables(self):
        created = False

        try:
            query = queries.create_default_tables_1
            self.db_object.update_data(query)
            created = True
        except pymysql.err.InternalError:
            print("These tables are already created, please proceed for data entry...")
            y = input("Press enter to continue...")
        if created:
            query = queries.create_default_tables_2
            self.db_object.update_data(query)
            query = queries.create_default_tables_3
            self.db_object.update_data(query)
            print("The default tables have been created successfully.")
            y = input("Press enter to continue...")

    def check_database_online(self):
        pass

    def create_default_DB(self):
        created = False

        query = queries.create_default_bd
        self.db_object.update_data(query)
        created = True
