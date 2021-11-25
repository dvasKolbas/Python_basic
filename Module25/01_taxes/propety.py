class Propety():
    def __init__(self, worth, percent_tax):
        self.__worth = worth
        self.__percent_tax = percent_tax
        self.__tax = self.__worth/self.__percent_tax

    def get_tax(self):
        return self.__tax

class Appartment(Propety):
    __percent_tax = 1000
    def __init__(self, worth):
        self.worth = worth
        super().__init__(self.worth, self.__percent_tax)

class Car(Propety):
    __percent_tax = 200
    def __init__(self, worth):
        self.worth = worth
        super().__init__(self.worth, self.__percent_tax)

class CountryHouse(Propety):
    __percent_tax = 500
    def __init__(self, worth):
        self.worth = worth
        super().__init__(self.worth, self.__percent_tax)


