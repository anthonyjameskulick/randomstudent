import sys
import csv
import time
import numpy as np
import random
import pandas as pd
import logging
import copy
import math
import cProfile, pstats, io
from pstats import SortKey
from queue import Queue

from pandas.io.formats.format import return_docstring

np.random.seed(42)

new_rosters = ["first_hour_roster.csv", "second_hour_roster.csv", "third_hour_roster.csv", "fourth_hour_roster.csv", "fifth_hour_roster", "sixth_hour_roster.csv", "seventh_hour_roster.csv", "eighth_hour_roster.csv"]
saved_rosters = ["first_hour_save.csv", "second_hour_save.csv", "third_hour_save.csv", "fourth_hour_save.csv", "fifth_hour_save", "sixth_hour_save.csv", "seventh_hour_save.csv", "eighth_hour_save.csv"]

class random_student_problem:
    def __init__(self):
        self.hour = None
        self.roster = None
        self.load = None
        self.working_roster = None
        self.new_roster_load = None
        self.saved_roster_load = None
        self.temp = None
        self.group = None
        self.random_group = None



def open_roster(self):
    print("start open roster")
    #print(self.new_roster_load)
    #print(self.saved_roster_load)
    #print(self.hour)
    if self.new_roster_load:
        hour = new_rosters[self.hour-1]
        #print(hour)
        file = open(hour)
        self.working_roster = list(csv.reader(file))
        file.close()
        print("")
        print(self.working_roster)
        print("")
    elif self.saved_roster_load:
        hour = saved_rosters[self.hour-1]
        file = open(hour)
        self.working_roster = list(csv.reader(file))
        file.close()
        print("")
        print(self.working_roster)
        print("")
    else:
        print("Invalid option try again.")
    print("end open_roster")
    return

def save_roster(self):
#add save roster fundtionality
    print(saved_rosters[self.hour-1])
    file = open(saved_rosters[self.hour-1], 'w+', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(self.working_roster)
    print("\n\n")
    main_program(self)
    return

def random_student_draw(self):
    #print(self.working_roster)
    if len(self.working_roster) != 0 and self.temp == 1:
        #print(len(self.working_roster))
        random_entry = random.randint(0, len(self.working_roster))
        #print(random_entry)
        random_student = self.working_roster.pop(random_entry-1)
        print("")
        print(random_student)
        print("")
    elif len(self.working_roster) == 0 and self.temp == 1:
        print("")
        print("reloading roster ...")
        print("")
        open_roster(self)
        random_group_draw(self)
    else:
        main_program(self)
    print("Which option would you like?\n1 another random student\n2 select a new class\n3 save current roster")
    self.temp = int(input())
    if self.temp == 1:
        random_student_draw(self)
    elif self.temp == 2:
        main_program(self)
    elif self.temp == 3:
        save_roster(self)
    else:
        print("invalid entry")
    return


def random_group_draw(self):
    print(self.working_roster)
    print("Which option would you like?  Press:\n1 for n groups\n2 for groups of n students")
    self.group = int(input())
    if self.group == 1:
        print("How many groups do you want to make?")
        self.group = int(input())
        self.random_group = [[] for _ in range(self.group)]
        #print(self.random_group)
        for i in range(len(self.working_roster)):
            random_entry = random.randint(0, len(self.working_roster))
            #print(random_entry)
            random_student = self.working_roster.pop(random_entry - 1)
            #print(random_student)
            self.random_group[i % self.group].append(random_student)
            #print(self.random_group)
            #input()
        for i in range(len(self.random_group)):
            print(f"Group {i} is {self.random_group[i]}")
    elif self.group == 2:
        print("What size groups do you want to make?")
        group = 0
        self.group = int(input())
        self.random_group = []
        #print(self.random_group)
        #input()
        while len(self.working_roster) > 0:
            self.random_group.append([])
            #print(self.random_group)
            for i in range(self.group):
                #print(f"{i}")
                #input()
                if len(self.working_roster) != 0:
                    random_entry = random.randint(0, len(self.working_roster))
                    # print(random_entry)
                    random_student = self.working_roster.pop(random_entry - 1)
                    #print(random_student)
                    #print(self.working_roster)
                    self.random_group[group].append(random_student)
                    #print(self.random_group)
                    #print({range(len(self.random_group))})
                    #input()
                else:
                    pass

            group = group +1
            #print(group)
            #print(f"{len(self.working_roster)}")
        for j in range(len(self.random_group)):
            # print(f"{j}")
            print(f"Group {j + 1} is {self.random_group[j]}")
            # print(f"{self.working_roster}")
        print("To start over press enter")
        input()
        main_program(self)




    else:
        print("invalid entry")

def main_program(self):
    print("Welcome to Dr. Kulick's Randomizer!\nSelect a class, press:\n1 for first hour, 2 for second hour, 3 for third hour, 4 for fourth hour\n5 for fifth hour, 6 for sixth hour, 7 for seventh hour, 8 for eighth hour")
    self.hour = int(input())
    if self.hour == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
        print("Which option would you like to use?  Press:\n1 to load a new roster\n2 to load a saved roster")
        self.load = int(input())
        #print(self.hour)
        #print(self.load)
        if self.load == 1:
            self.new_roster_load = bool(True)
            #print(self.new_roster_load)
            open_roster(self)
            print("Which option would you like to use?  Press:\n1 for random student\n2 for random group")
            self.temp = int(input())
            if self.temp == 1:
                random_student_draw(self)
            elif self.temp == 2:
                random_group_draw(self)
        elif self.load == 2:
            self.saved_roster_load = bool(True)
            open_roster(self)
            print("Which option would you like to use?  Press:\n1 for random student\n2 for random group")
            self.temp = int(input())
            if self.temp == 1:
                random_student_draw(self)
            elif self.temp == 2:
                random_group_draw(self)
        else:
            print("Invalid option try again.")
    else:
        print("Invalid option try again.")

    return

a = random_student_problem()
#a.load=1
#a.hour = 1
#open_roster(a)
main_program(a)


