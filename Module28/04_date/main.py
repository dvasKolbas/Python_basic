import datetime


class Date:
    date = None
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return "День: {0}\t Месяц: {1}\t Год: {2}".format(self.date[0], self.date[1], self.date[2])

    @classmethod
    def is_date_valid(self, string):
        try:
            date = datetime.datetime.strptime(string, "%d-%m-%Y")
            if date:
                return True
        except ValueError:
            return False

    @classmethod
    def from_string(self, string):
        if self.is_date_valid(string):
            date = string.split("-")
            self.date = Date(date)
            return self.date
        else:
            return self.date

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))