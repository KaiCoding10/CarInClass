from connection import MySQLConnection
from CarData import *


def main():
    my_sqlconnection = sql_connect()
    accept_data(my_sqlconnection)
    sql_close(my_sqlconnection)


def sql_connect():
    try:
        mysql_connection = MySQLConnection('127.0.0.1', 'root', 'root', 'carsinclass')

        mysql_connection.connect()

        return mysql_connection

    except Exception as e:
        print(f"Error connecting to cats database")


def accept_data(mysql_connection):
    cursor = mysql_connection.cursor
    db = CarData()
    cursor.execute(db.cars_select())

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    while True:
        usr_des = input("Would you like to add a new car to the table or delete a car? Add or Delete")

        match usr_des:
            case "Add":
                cursor.execute(db.car_insert(), (db.make, db.model, db.year, db.color))
                print("Successfully Added Data")
                break
            case "Delete":
                car_make = input("Enter the make of the car you want to delete")
                cursor.execute(db.car_delete(), db.make)
                print("Successfully Deleted Data")
                break
            case _:
                print("Error, enter data again")

        mysql_connection.connection.commit()


def sql_close(mysql_connection):
    mysql_connection.close()


def car_details(carsdata):
    make = input("Enter car make")
    model = input("Enter car model")
    year = input("Enter car year")
    color = input("Enter car color")

    carsdata.car_construct(make, model, year, color)

    return True


main()
