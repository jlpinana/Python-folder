from datetime import datetime

format = "%d %b %Y"
date = input("Add date: ")

try:
    res = bool(datetime.strptime(date, format))
except ValueError:
    print("Wrong date format! Please add a correct date in the format (dd Mmm yyyy)")
