from random import randint
from datetime import datetime

from db.executer import execute_query, execute_command


class doctor:

    def __init__(self, name, password, id = ""):
        self.name = name
        self.password = password
        self.email = self.name + "_doc@faculty.edu"
        print("Account created for doctor {0} with Email {1}".format(self.name,self.email)) if id == "" else None
        self.id = "D" + self.name[0:2].upper() + str(randint(100000000,999999999)) if id == "" else id

    def addCourse(self) -> None:
        cn = input("Enter the name of the course: ")
        c = course(cn,self.name)
        execute_command("""INSERT INTO courses(name, doc, code) VALUES (%s, %s, %s)""",(c.name, c.doc, c.code))
        execute_command("""INSERT INTO teaching(doctor_id, course_code) VALUES (%s, %s)""",(self.id, c.code))

    def viewCoursesTeaching(self) -> None:
        data = execute_query("""(SELECT course_code FROM teaching WHERE doctor_id = '%s')""" % (self.id))
        for c in data:
            cursor.execute("""SELECT name, code FROM courses WHERE code = '%s'""" % (c[0]))
            records = cursor.fetchall()
            for r in records:
                print("course {0} code {1}".format(r[0], r[1]))

    def deleteCourse(self) -> None:
        self.viewCoursesTeaching()
        code = input("Enter course code to delete: ")
        execute_command("""DELETE FROM teaching WHERE doctor_id = '%s' AND course_code = '%s'""" %(self.id, code))
        execute_command("""DELETE FROM courses WHERE code = '%s'""" %(code))
        execute_command("""DELETE FROM enrollment WHERE course_code = '%s'""" %(code))

    def post(self) -> None:
        post = input("Create a post:  ")
        execute_command("""INSERT INTO timeline VALUES ('%s', 'doctor', '%s', '%s', '%s', '%s')""" % (self.id[0:5] + str(randint(1000,10000)), self.id, self.name, post, datetime.now()))
    
    def reply(self, post_id) -> None:
        reply = input("reply: ")
        execute_command("""INSERT INTO replies VALUES ('%s', '%s', '%s', '%s')""" %(post_id, self.name, reply, datetime.now()))
    
    def viewPosts(self) -> None:
        print("posts:")
        data = execute_query("""SELECT publisher_name, publisher, post, created_at FROM timeline WHERE publisher_id = '%s'""" %(self.id))
        for r in data:
            print("---------------------------------------------------------------")
            minuits = int((datetime.now() - r[3]).total_seconds() / 60)
            print('\n'.join([r[0] + " ({0})".format(r[1]) + ":", r[2], str(minuits) + " minuits" if minuits < 60 else str(r[3])]))
            print("---------------------------------------------------------------")
    
    def viewTimeLine(self) -> None:
        print("Time Line:")
        data = execute_query("""SELECT post_id, publisher_name, publisher, post, created_at FROM timeline""")
        for r in data:
            print("---------------------------------------------------------------")
            minuits = int((datetime.now() - r[4]).total_seconds() / 60)
            print('\n'.join([r[1] + " ({0})".format(r[2]) + ":", r[3], str(minuits) + " minuits" if minuits < 60 else str(r[4])]))
            print("---------------------------------------------------------------")
            index = int(input("Enter 1 to reply, 2 to view replies or any key to view next post: "))
            if index == 1:
                self.reply(r[0])
            elif index == 2:
                records = execute_query("""SELECT replier, reply, created_at FROM replies WHERE post_id = '%s'""" %(r[0]))
                for record in records:
                    m = int((datetime.now() - record[2]).total_seconds() / 60)
                    print('\n'.join([record[0], record[1], str(m) + " minuits" if m < 60 else str(record[2])]))
                    print("---------------------------------------------------------------")
            else:
                continue
    
    def profile(self) -> None:
        print('\n'.join(["doctor: {0}".format(self.name),"Email: {0}".format(self.email),"ID: {0}".format(self.id),"Teaching:"]))
        self.viewCoursesTeaching()
    
    @staticmethod
    def menu() -> int:
        index = int(input('\n'.join(["Enter 1 to Creat a course",
                         "Enter 2 to delete a course",
                         "Enter 3 to view profile",
                         "Enter 4 to post",
                         "Enter 5 to view time line",
                         "Enter 6 to log out",": "])))
        return index