from record import *
import random
import os

main_menu = True

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

    def initialize_box(self): #tuple that takes certain argument?
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

    def start_up(self):
        print("-----------------------Welcome to Mom & Pop's Jukebox!-----------------------\n")
        print("Please select one of the following options.")
        print("To play a record, type 1.")
        print("To add a record, type 2.")
        print("To delete a record, type 3.")
        print("To look up a record, type 4.")
        print("To list all the records, type 5.")
        print("To exit, type 6.")
        decision = input("Type here: ")

        if decision == "1":
            main_menu = False
            self.play_record()
        if decision == "2":
            main_menu = False
            self.add_record()
        if decision == "3":
            main_menu = False
            self.del_record()
        if decision == "4":
            main_menu = False
            self.look_up_record()
        if decision == "5":
            main_menu = False
            self.list_all_records()
        if decision == "6":
            print("Goodbye!")
            os._exit(-1)

    def play_record(self):
        os.system("clear")
        play_lines=[
            "\"Ain't it funky now?!\"",
            "\"Get on up! Get into it!! Get involved!!!\"",
            "\"Give the drummer some!!\"",
            "\"Pick up on this!!\"",
            "\"Have mercy on me!!\"",
            "\"Get up off of that thing!\nDance until you feel better!!\"",
            "\"You've got the flavor!!\""
        ]
        row_sel = input("Please select a row (Type a capital letter from A to J): ")
        col_sel = int(input("Please select a column (Type a number from 1 to 8): "))
        side_sel = input("Which side do you want to play? The A-side or B-side? (Type A or B): ")
        record_sel = self.inventory[row_sel][(col_sel - 1)]

        if side_sel == "A":
            print ("\nYou played %s by %s!\nYou proceed to dance!" % (record_sel["aside"],record_sel["artist"]))
            print (play_lines[random.randint(0,7)])
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True
        elif side_sel == "B":
            print ("\nYou played %s by %s!\nYou proceed to dance!" % (record_sel["bside"],record_sel["artist"]))
            print (play_lines[random.randint(0,7)])
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True

    def add_record(self):
        os.system("clear")
        row_num = input("Please select a row (Type a capital letter from A to J): ")
        col_num = int(input("Please select a column (Type a number from 1 to 8): "))
        possible_rows = ["A","B","C","D","E","F","G","H","I","J"]

        if (not self.inventory[row_num][col_num-1]):
            artist_inp = input("Please enter the name of the artist: ")
            aside_inp = input("Please enter the title of the song on the record's A-side: ")
            bside_inp = input("Please enter the title of the song on the record's B-side: ")
            year_inp = int(input("Please enter the year of the record's release: "))
            genre_inp = input("Please enter the genre of the record: ")

            self.inventory[row_num][col_num-1]['artist'] = artist_inp
            self.inventory[row_num][col_num-1]['aside'] = aside_inp
            self.inventory[row_num][col_num-1]['bside'] = bside_inp
            self.inventory[row_num][col_num-1]['year'] = year_inp
            self.inventory[row_num][col_num-1]['genre'] = genre_inp

            print ("%s / %s by %s has been added to slot %s%s. Thank you" % (aside_inp,bside_inp,artist_inp,row_num,col_num))
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True
        elif (row_num not in possible_rows or col_num not in range(1,9)):
            print ("I'm sorry, but this is not an actual slot in the machine.")
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True
        else:
            print ("I'm sorry, but this slot is currently taken.")
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True

    def del_record(self):
        os.system("clear")
        row_num = input("Please select a row (Type a capital letter from A to J): ")
        col_num = int(input("Please select a column (Type a number from 1 to 8): "))
        possible_rows = ["A","B","C","D","E","F","G","H","I","J"]

        if (self.inventory[row_num][col_num-1]):
            self.inventory[row_num][col_num-1].clear()
            print ("Slot %s%s is now empty. Thank you." % (row_num,col_num))
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True
        elif (row_num not in possible_rows or col_num > 8):
            print ("I'm sorry, but this is not an actual slot in the machine.")
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True
        else:
            print ("I'm sorry, but this slot is already empty.")
            input("Press any key to return to the main menu.")
            os.system("clear")
            main_menu = True

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
        input("Press any key to return to the main menu.")
        os.system("clear")
        main_menu = True

    def list_all_records(self):
        os.system("clear")
        for key1, val1 in self.inventory.items():
            for array in val1:
                column_no = str(val1.index(array) + 1)
                print("Record " + key1 + column_no + "-----------------------------")
                array_ordered = array.items()
                for key2, val2 in array_ordered:
                    print(key2.upper() + ": " + str(val2))
                print("\n")
        input("Press any key to return to the main menu.")
        os.system("clear")
        main_menu = True
