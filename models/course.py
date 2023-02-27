from random import randint

class course:

    def __init__(self, name, doc, code = ""):
        self.name = name
        self.doc = doc
        print("course {0} has been constructed by {1}".format(self.name,self.doc) ) if code == "" else None
        self.code = self.name[0:2].upper() + str(randint(1000,9999)) if code == "" else code

    def viewData(self) -> None:
        print('\n'.join(["course: {0}".format(self.name),"code: {0}".format(self.code),"being teached by: {0}".format(self.doc)]))