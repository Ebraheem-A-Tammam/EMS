from models import *


if __name__ == "__main__":

    
    while True:
        inp = console.run()
        if inp == 1:
            console.signUp()
        inp = console.login()
        obj = console.doctorLogin() if inp == 1 else console.studentLogin()
        while True:
            if inp == 1:
                n = doctor.menu()
                if n == 1:
                    obj.addCourse()
                elif n == 2:
                    obj.deleteCourse()
                elif n == 3:
                    obj.profile()
                elif n == 4:
                    obj.post()
                elif n == 5:
                    obj.viewTimeLine()
                elif n == 6:
                    break
            elif inp == 2:
                n = student.menu()
                if n == 1:
                    obj.enroll()
                elif n == 2:
                    obj.unenroll()
                elif n == 3:
                    obj.profile()
                elif n == 4:
                    obj.post()
                elif n == 5:
                    obj.viewTimeLine()
                elif n == 6:
                    break
        esc = int(input("Do you want to close the program? (Enter 1 to close or any key to continue): "))
        if esc == 1:
            break