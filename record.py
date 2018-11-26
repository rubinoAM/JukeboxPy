rec_att = ["artist","aside","bside","year","genre"]

class Record(object):
    def __init__(self,rec_att):
        self.artist = rec_att[0]
        self.aside = rec_att[1]
        self.bside = rec_att[2]
        self.year = rec_att[3]
        self.genre = rec_att[4]