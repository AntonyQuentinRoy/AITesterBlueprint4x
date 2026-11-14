class Family:
    def __init__(self):
        self.private.wife = "dia"
        self.protected.son = "shi"
        self.protected.daughter = "sta"
   
    def mom(self):
        print("Wife:", self.private.wife)
        print("Son:", self.protected.son)
        print("Daughter:", self.protected.daughter)

class Child(Family):
    def __init__(self):
        super().__init__()
        print("Son:", self.protected.son)
        print("Daughter:", self.protected.daughter)
        # print("Wife:", self.private.wife)  # This will raise an AttributeError