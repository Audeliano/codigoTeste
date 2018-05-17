class Parent():
    def __init__(self, last_name, eyes_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eyes_color = eyes_color
    
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eyes Color - "+self.eyes_color)

class Child(Parent):
    def __init__(self, last_name, eyes_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eyes_color)
        self.number_of_toys = number_of_toys

    #Method Overriding -> metodo de uma classe filha com mesmo nome do metodo de sua classe pai
    def show_info(self):
        print("2Last Name - "+self.last_name)
        print("2Eyes Color - "+self.eyes_color)

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
print("Billy last name is "+billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()
print("Miley last name is "+miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)