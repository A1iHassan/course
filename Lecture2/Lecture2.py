#!/usr/bin/env python3

class Employees:
    def __init__(self, name, check_in_time, check_out_time, salary):
        self.name = name
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.__salary = salary
    
    def adherence(self):
        print(f"name: {self.name} - check in time: {self.check_in_time} - check out time: {self.check_out_time}")
        print("\n\n")


Ali = Employees("ali", 5, 9, 100)
Mohammad = Employees("mohammad", 4, 8, 75)
Ramy = Employees("ramy", 5, 9, 130)
Ali.adherence()
Mohammad.adherence()
Ramy.adherence()