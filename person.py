class Person:
    def __init__(self,name,adress,phonenumber,emailadress):
       self.name = name
       self.adress = adress
       self.phone_number = phonenumber
       self.e_mail_adress = emailadress

    def __str__(self):
        print("Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name)
        return "Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name

    