from record import Record

class Jukebox(object):
    def __init__(self):
        self.inventory = [
            [],[],[],[],[],[],[],[],[],[]
        ]
    def add_record(self,record,row):
        if (len(self.inventory[row]) < 5):
            self.inventory[row].append(record)
        else:
            print "I'm sorry, but this row is currently too full to insert new records."
    def del_record(self,record):
        for row in self.inventory:
            if record in row:
                row.pop(record)