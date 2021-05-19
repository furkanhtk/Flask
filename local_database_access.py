from database import Database
import sqlite3
from parameter import Parameter


def get_parameters(db):
    datas=[]
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = "SELECT ID, FREQUENCY, PWR FROM PARAMETER ORDER BY ID"
    for row in cur.execute(query):
        datas.append(row)
    return datas

def add_parameter(db,freq,pwr):
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = "INSERT INTO PARAMETER (FREQUENCY, PWR) VALUES (?, ?)"
    cur.execute(query,(freq, pwr))
    con.commit()


def update_parameter(db,parameter_key, frequency,power):
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = "UPDATE PARAMETER SET FREQUENCY = ?, PWR = ? WHERE (ID = ?)"
    cur.execute(query, (frequency, power, parameter_key))
    con.commit()


def delete_parameter(db,parameter_key):
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = "DELETE FROM PARAMETER WHERE (ID = ?)"
    cur.execute(query, (parameter_key,))
    con.commit()


if __name__ == "__main__":
    db = r"C:\Users\Furkan\Desktop\Flask\parameters.sqlite"
    x=get_parameters(db)
    print(x)
    #add_parameter(db,"100 Ghz",-50)
    x=get_parameters(db)
    print(x)
    #delete_parameter(db,4)
    x=get_parameters(db)
    print(x)
    #update_parameter(db,13,"1 Ghz",-20)
    x=get_parameters(db)
    print(x)


