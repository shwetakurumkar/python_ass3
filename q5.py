class InvalidDateException(Exception):
    """Custom exception for invalid dates."""
    def _init_(self, message="Invalid Date!"):
        self.message = message
        super()._init_(self.message)

class Date:
    def _init_(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def accept(self):
        try:
            self.day = int(input("Enter day: "))
            self.month = int(input("Enter month: "))
            self.year = int(input("Enter year: "))
            self.validate_date()
        except InvalidDateException as e:
            print(e)

    def validate_date(self):
        if self.month < 1 or self.month > 12:
            raise InvalidDateException("Invalid month! Must be between 1 and 12.")
        if self.day < 1 or self.day > self.days_in_month(self.month, self.year):
            raise InvalidDateException("Invalid day for the given month.")
        if self.year < 1:
            raise InvalidDateException("Invalid year! Must be a positive value.")

    def days_in_month(self, month, year):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self.is_leap_year(year):
            return 29
        return days_in_month[month]

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def display(self):
        print(f"Date: {self.day:02d}/{self.month:02d}/{self.year}")

date = Date()
date.accept()
date.display()