class Human:

    def __init__(self, first,last,weight,height,ethnicity,location,born,occupation):
        self.first = first
        self.last = last
        self.weight = weight
        self.height = height
        self.ethnicity = ethnicity
        self.location = location
        self.born = born
        self.occupation = occupation

    def walk(self):
        print(f"{self.first} {self.last} is now walking!")
    def drive(self):
        print(f"{self.first} {self.last} is now driving!")
    def sleep(self):
        print(f"{self.first} {self.last} is now sleeping!")


