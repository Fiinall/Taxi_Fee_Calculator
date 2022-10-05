from person import Person


class Driver(Person):

    def __init__(self,name,adress,phonenumber,emailadress,driver_id,score,driving_experience):
        super().__init__(name,adress,phonenumber,emailadress)
        self.driver_id = driver_id
        self.score = score
        self.driving_experience = driving_experience

    def __str__(self):
        print("Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name)
        return "Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name



        