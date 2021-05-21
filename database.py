import sqlite3 as dbapi2

from parameter import Parameter


class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def add_parameter(self, parameter):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO PARAMETER (FREQUENCY, PWR) VALUES (?, ?)"
            cursor.execute(query, (parameter.frequency, parameter.power))
            connection.commit()
            parameter_key = cursor.lastrowid
        return parameter_key

    def update_parameter(self, parameter_key, parameter):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE PARAMETER SET FREQUENCY = ?, PWR = ? WHERE (ID = ?)"
            cursor.execute(query, (parameter.frequency, parameter.power, parameter_key))
            connection.commit()

    def delete_parameter(self, parameter_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM PARAMETER WHERE (ID = ?)"
            cursor.execute(query, (parameter_key,))
            connection.commit()

    def get_parameter(self, parameter_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT FREQUENCY, PWR FROM PARAMETER WHERE (ID = ?)"
            cursor.execute(query, (parameter_key,))
            frequency, power = cursor.fetchone()
        parameter_ = Parameter(frequency, power)
        return parameter_

    def get_parameters(self):
        parameters = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, FREQUENCY, PWR FROM PARAMETER ORDER BY ID"
            cursor.execute(query)
            for parameter_key, frequency, power in cursor:
                parameters.append((parameter_key, Parameter(frequency, power)))
        return parameters