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
    def init_add(self,record,row,col):
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
        self.init_add(a_1,"A",0)
        self.init_add(a_2,"A",1)
        self.init_add(a_3,"A",2)
        self.init_add(a_4,"A",3)
        self.init_add(a_5,"A",4)
        self.init_add(a_6,"A",5)
        self.init_add(a_7,"A",6)
        self.init_add(a_8,"A",7)
        self.init_add(b_1,"B",0)
        self.init_add(b_2,"B",1)
        self.init_add(b_3,"B",2)
        self.init_add(b_4,"B",3)
        self.init_add(b_5,"B",4)
        self.init_add(b_6,"B",5)
        self.init_add(b_7,"B",6)
        self.init_add(b_8,"B",7)
        self.init_add(c_1,"C",0)
        self.init_add(c_2,"C",1)
        self.init_add(c_3,"C",2)
        self.init_add(c_4,"C",3)
        self.init_add(c_5,"C",4)
        self.init_add(c_6,"C",5)
        self.init_add(c_7,"C",6)
        self.init_add(c_8,"C",7)
        self.init_add(d_1,"D",0)
        self.init_add(d_2,"D",1)
        self.init_add(d_3,"D",2)
        self.init_add(d_4,"D",3)
        self.init_add(d_5,"D",4)
        self.init_add(d_6,"D",5)
        self.init_add(d_7,"D",6)
        self.init_add(d_8,"D",7)
        self.init_add(e_1,"E",0)
        self.init_add(e_2,"E",1)
        self.init_add(e_3,"E",2)
        self.init_add(e_4,"E",3)
        self.init_add(e_5,"E",4)
        self.init_add(e_6,"E",5)
        self.init_add(e_7,"E",6)
        self.init_add(e_8,"E",7)
        self.init_add(f_1,"F",0)
        self.init_add(f_2,"F",1)
        self.init_add(f_3,"F",2)
        self.init_add(f_4,"F",3)
        self.init_add(f_5,"F",4)
        self.init_add(f_6,"F",5)
        self.init_add(f_7,"F",6)
        self.init_add(f_8,"F",7)
        self.init_add(g_1,"G",0)
        self.init_add(g_2,"G",1)
        self.init_add(g_3,"G",2)
        self.init_add(g_4,"G",3)
        self.init_add(g_5,"G",4)
        self.init_add(g_6,"G",5)
        self.init_add(g_7,"G",6)
        self.init_add(g_8,"G",7)
        self.init_add(h_1,"H",0)
        self.init_add(h_2,"H",1)
        self.init_add(h_3,"H",2)
        self.init_add(h_4,"H",3)
        self.init_add(h_5,"H",4)
        self.init_add(h_6,"H",5)
        self.init_add(h_7,"H",6)
        self.init_add(h_8,"H",7)
        self.init_add(i_1,"I",0)
        self.init_add(i_2,"I",1)
        self.init_add(i_3,"I",2)
        self.init_add(i_4,"I",3)
        self.init_add(i_5,"I",4)
        self.init_add(i_6,"I",5)
        self.init_add(i_7,"I",6)
        self.init_add(i_8,"I",7)
        self.init_add(j_1,"J",0)
        self.init_add(j_2,"J",1)
        self.init_add(j_3,"J",2)
        self.init_add(j_4,"J",3)
        self.init_add(j_5,"J",4)
        self.init_add(j_6,"J",5)
        self.init_add(j_7,"J",6)
        self.init_add(j_8,"J",7)
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
