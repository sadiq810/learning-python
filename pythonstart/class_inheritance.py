class Anyone:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display(self):
        print(self.firstname, self.lastname)


# anyone = Anyone('Ali', 'Jan')
# anyone.display()

class Player(Anyone):
    pass  # this keyword is used when there is no other properties or methods in the class to avoid error.


obj = Player("Jamal", "Khan")
obj.display()