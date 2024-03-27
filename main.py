from connection import MySQLConnection
from CarData import *


def main():
    my_sqlconnection = sql_connect()
    accept_data(my_sqlconnection)
    sql_close(my_sqlconnection)


def sql_connect():
    try:
        mysql_connection = MySQLConnection('localhost', 'root', '1234kien', 'python2')

        mysql_connection.connect()

        return mysql_connection

    except Exception as e:
        print(f"Error connecting to cats database")


def accept_data(mysql_connection):
    cursor = mysql_connection.cursor
    car = CarData()
    cursor.execute(car.car_select())

    rows = cursor.fetchall()
    print("This is the list of car from the database:\n")

    if rows is None:
        print("You have no car in the database!!!")

    for row in rows:
        print(row)

    while True:
        usr_des = input("Would you like to add a new car to the table or delete a car? Add or Delete")

        match usr_des:
            case "Add":
                if car_details(car):
                    cursor.execute(car.car_insert(), (car.make, car.model, car.year, car.color))
                    print("Successfully Added Data")
                    break
            case "Delete":
                car.make = input("Enter the make of the car you want to delete")
                cursor.execute(car.car_delete(), car.make)
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

    carsdata.car_constructor(make, model, year, color)

    return True


main()
