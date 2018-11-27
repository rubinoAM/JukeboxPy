from record import *
import os

class Jukebox(object):
    def __init__(self):
        self.inventory = {
            "A":[{},{},{},{},{},{},{},{}],
            "B":[{},{},{},{},{},{},{},{}],
            "C":[{},{},{},{},{},{},{},{}],
            "D":[{},{},{},{},{},{},{},{}],
            "E":[{},{},{},{},{},{},{},{}],
            "F":[{},{},{},{},{},{},{},{}],
            "G":[{},{},{},{},{},{},{},{}],
            "H":[{},{},{},{},{},{},{},{}],
            "I":[{},{},{},{},{},{},{},{}],
            "J":[{},{},{},{},{},{},{},{}]
        }
    def add_record(self,record,row,col):
        row_num = row
        col_num = col

        if (not self.inventory[row_num][col_num]):
            self.inventory[row_num][col_num]['artist'] = record.artist
            self.inventory[row_num][col_num]['aside'] = record.aside
            self.inventory[row_num][col_num]['bside'] = record.bside
            self.inventory[row_num][col_num]['year'] = record.year
            self.inventory[row_num][col_num]['genre'] = record.genre
        else:
            print ("I'm sorry, but this slot is currently taken.")
    def initialize_box(self):
        self.add_record(a_1,"A",0)
        self.add_record(a_2,"A",1)
        self.add_record(a_3,"A",2)
        self.add_record(a_4,"A",3)
        self.add_record(a_5,"A",4)
        self.add_record(a_6,"A",5)
        self.add_record(a_7,"A",6)
        self.add_record(a_8,"A",7)
        self.add_record(b_1,"B",0)
        self.add_record(b_2,"B",1)
        self.add_record(b_3,"B",2)
        self.add_record(b_4,"B",3)
        self.add_record(b_5,"B",4)
        self.add_record(b_6,"B",5)
        self.add_record(b_7,"B",6)
        self.add_record(b_8,"B",7)
        self.add_record(c_1,"C",0)
        self.add_record(c_2,"C",1)
        self.add_record(c_3,"C",2)
        self.add_record(c_4,"C",3)
        self.add_record(c_5,"C",4)
        self.add_record(c_6,"C",5)
        self.add_record(c_7,"C",6)
        self.add_record(c_8,"C",7)
        self.add_record(d_1,"D",0)
        self.add_record(d_2,"D",1)
        self.add_record(d_3,"D",2)
        self.add_record(d_4,"D",3)
        self.add_record(d_5,"D",4)
        self.add_record(d_6,"D",5)
        self.add_record(d_7,"D",6)
        self.add_record(d_8,"D",7)
        self.add_record(e_1,"E",0)
        self.add_record(e_2,"E",1)
        self.add_record(e_3,"E",2)
        self.add_record(e_4,"E",3)
        self.add_record(e_5,"E",4)
        self.add_record(e_6,"E",5)
        self.add_record(e_7,"E",6)
        self.add_record(e_8,"E",7)
        self.add_record(f_1,"F",0)
        self.add_record(f_2,"F",1)
        self.add_record(f_3,"F",2)
        self.add_record(f_4,"F",3)
        self.add_record(f_5,"F",4)
        self.add_record(f_6,"F",5)
        self.add_record(f_7,"F",6)
        self.add_record(f_8,"F",7)
        self.add_record(g_1,"G",0)
        self.add_record(g_2,"G",1)
        self.add_record(g_3,"G",2)
        self.add_record(g_4,"G",3)
        self.add_record(g_5,"G",4)
        self.add_record(g_6,"G",5)
        self.add_record(g_7,"G",6)
        self.add_record(g_8,"G",7)
        self.add_record(h_1,"H",0)
        self.add_record(h_2,"H",1)
        self.add_record(h_3,"H",2)
        self.add_record(h_4,"H",3)
        self.add_record(h_5,"H",4)
        self.add_record(h_6,"H",5)
        self.add_record(h_7,"H",6)
        self.add_record(h_8,"H",7)
        self.add_record(i_1,"I",0)
        self.add_record(i_2,"I",1)
        self.add_record(i_3,"I",2)
        self.add_record(i_4,"I",3)
        self.add_record(i_5,"I",4)
        self.add_record(i_6,"I",5)
        self.add_record(i_7,"I",6)
        self.add_record(i_8,"I",7)
        self.add_record(j_1,"J",0)
        self.add_record(j_2,"J",1)
        self.add_record(j_3,"J",2)
        self.add_record(j_4,"J",3)
        self.add_record(j_5,"J",4)
        self.add_record(j_6,"J",5)
        self.add_record(j_7,"J",6)
        self.add_record(j_8,"J",7)
    def del_record(self,record):
        for row in self.inventory:
            if record in row:
                row.pop(record)
    
    def look_up_record(self):
        os.system("clear")
        print("What criteria would you like to use in your search?")
        print("Please select from the following:")
        query = input("1.Artist\n2.Year\n3.Genre\nEnter: ")
        check_count = 0

        if query == "1":
            print("Please enter the first letter you wish to search by:")
            search_key = input("Enter: ")
            os.system("clear")
            print("Search Results:\n")
            for key1, val1 in self.inventory.items():
                for array in val1:
                    column_no = str(val1.index(array) + 1)
                    array_ordered = array.items()
                    for key2, val2 in array_ordered:
                        if key2 == "artist":
                            if search_key == val2[0]:
                                print("Record " + key1 + column_no + "-----------------------------")
                                for key3, val3 in array_ordered:
                                    print(key3.upper() + ": " + str(val3))
                                    check_count += 1
                                print("\n")
            if check_count == 0:
                print ("No records were found using that string.")
        elif query == "2":
            print("Please enter the year you wish to search by:")
            search_key = input("Enter: ")
            os.system("clear")
            print("Search Results:\n")
            for key1, val1 in self.inventory.items():
                for array in val1:
                    column_no = str(val1.index(array) + 1)
                    array_ordered = array.items()
                    for key2, val2 in array_ordered:
                        if key2 == "year":
                            if search_key == str(val2):
                                print("Record " + key1 + column_no + "-----------------------------")
                                for key3, val3 in array_ordered:
                                    print(key3.upper() + ": " + str(val3))
                                    check_count += 1
                                print("\n")
            if check_count == 0:
                print ("No records were found from that year.")
        elif query == "3":
            print("Please enter the string you wish to search by:")
            search_key = input("Enter: ")
            os.system("clear")
            print("Search Results:\n")
            for key1, val1 in self.inventory.items():
                for array in val1:
                    column_no = str(val1.index(array) + 1)
                    array_ordered = array.items()
                    for key2, val2 in array_ordered:
                        if key2 == "genre":
                            if search_key in val2:
                                print("Record " + key1 + column_no + "-----------------------------")
                                for key3, val3 in array_ordered:
                                    print(key3.upper() + ": " + str(val3))
                                    check_count += 1
                                print("\n")
            if check_count == 0:
                print ("No records were found using that string.")
        check_count = 0



    def list_all_records(self):
        for key1, val1 in self.inventory.items():
            for array in val1:
                column_no = str(val1.index(array) + 1)
                print("Record " + key1 + column_no + "-----------------------------")
                array_ordered = array.items()
                array_ordered.sort()
                for key2, val2 in array_ordered:
                    print(key2.upper() + ": " + str(val2))
