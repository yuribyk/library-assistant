import pymysql
from DatabaseInteractor.DTO.DataPacker import DataPacker


class DataBaseUtilities:
    def __init__(self):
        pass

    @staticmethod
    def get_data_base_connection():
        try:
            db_connection = pymysql.connect("localhost", "root", "Peacer1490!", "LibrarySystem")
            return db_connection

        except Exception as e:
            raise e

    @staticmethod
    def close_data_base_connection(bd_connect):
        try:
            bd_connect.close()
        except Exception as e:
            raise e

    def update_data(self, query):
        db_connection = self.get_data_base_connection()
        try:
            cursor = db_connection.cursor()
            cursor.execute(query)
            db_connection.commit()
            #print("Data update was successful.")

        except Exception as e:
            raise e

        finally:
            self.close_data_base_connection(db_connection)

    def get_info(self, query):
        db_connection = self.get_data_base_connection()
        try:
            cursor = db_connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            return DataPacker(records)

        except Exception as e:
            raise e
        finally:
            self.close_data_base_connection(db_connection)