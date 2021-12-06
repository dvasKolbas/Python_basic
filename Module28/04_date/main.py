import datetime


class Date:
    @classmethod
    def is_date_valid(cls, string):
        try:
            date = datetime.datetime.strptime(string, "%d-%m-%Y")
            if date:
                return True
        except ValueError:
            return False

    @classmethod
    def from_string(cls, string):
        if cls.is_date_valid(string):
            date = string.split("-")
            return "День: {0}\t Месяц: {1}\t Год: {2}".format(date[0], date[1], date[2])
        else:
            return None

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))