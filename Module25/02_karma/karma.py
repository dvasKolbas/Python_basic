import random


class MyKarma():
    __max_karma = 500
    def __init__(self, file):
        self.__current_karma = 0
        self.file = file

    def one_day(self):
        self.__current_karma += random.randint(1, 7)
        if self.check_karma():
            return True
        if random.randint(1, 10) == 1:
            self.__create_rise()
        return False

    def __create_rise(self):
        raise random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]).write_rise(self.file)

    def check_karma(self):
        if self.__current_karma >= self.__max_karma:
            return True
        return False


class KillError(Exception):
    def write_rise(self, file):
        file.write("KillError\n")

class DrunkError(Exception):
    def write_rise(self, file):
        file.write("DrunkError\n")

class CarCrashError(Exception):
    def write_rise(self, file):
        file.write("CarCrashError\n")

class GluttonyError(Exception):
    def write_rise(self, file):
        file.write("GluttonyError\n")

class DepressionError(Exception):
    def write_rise(self, file):
        file.write("DepressionError\n")

