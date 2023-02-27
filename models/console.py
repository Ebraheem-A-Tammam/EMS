from random import randint
from datetime import datetime

from db.executer import execute_query, execute_command
from .doctor import doctor
from .student import student

class console:
    
    @staticmethod
    def run() -> int:
        index = int(input("Enter 1 for sign up or 2 for log in: "))
        return index
    
    @staticmethod
    def signUp() -> None:
        name = input("Enter your name: ")
        password = input("Creat a password: ")
        index = int(input("Enter 1 for doctor or 2 for student: "))
        obj = doctor(name, password) if index == 1 else student(name, password)
        if index == 1:
            execute_command("""INSERT INTO doctors(name, email, password, id) VALUES('%s', '%s', '%s', '%s')""" % (obj.name, obj.email, obj.password, obj.id))
        elif index == 2:
            execute_command("""INSERT INTO students(name, email, password, id) VALUES('%s', '%s', '%s', '%s')""" % (obj.name, obj.email, obj.password, obj.id))
    
    @staticmethod
    def login() -> int:
        index = int(input("Enter 1 to login as a doctor or 2 to login as a student: "))
        return index
    
    @staticmethod
    def doctorLogin() -> doctor:
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        data = execute_query("""SELECT name, password, id FROM doctors WHERE email = '%s'""" %(email))
        if data:
            if data[0][1] == password:
                return doctor(data[0][0],password,data[0][2])
        else:
            print("Email or password is incorrect")
            return doctorLogin()

    @staticmethod
    def studentLogin() -> student:
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        data = execute_query("""SELECT name, password, id FROM students WHERE email = '%s'""" %(email))

        if data:
            if data[0][1] == password:
                return student(data[0][0],password,data[0][2])
        else:
            print("Email or password is incorrect")
            return studentLogin()