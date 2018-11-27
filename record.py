rec_att = ["artist","aside","bside","year","genre"]

class Record(object):
    def __init__(self,rec_att):
        self.artist = rec_att[0]
        self.aside = rec_att[1]
        self.bside = rec_att[2]
        self.year = rec_att[3]
        self.genre = rec_att[4]
       
"""
Records to be added:

a_1 = Record("MC5","Kick Out The Jams","Motor City Is Burning",1969,"Rock")
a_2 = Record("808 State","Pacific-707","Pacific-B",1989,"Techno")
a_3 = Record("De La Soul","Breakadawn","En Focus",1993,"Rap")
a_4 = Record("Iron Maiden","2 Minutes To Midnight","Rainbows Gold",1984,"Metal")
a_5 = Record("Doug E. Fresh And The Get Fresh Crew","The Show","La Di Da Di",1985,"Rap")
b_1 = Record("Anthrax","I Am The Law","Bud E. Luvbomb And Satan's Lounge Band",1987,"Metal")
b_2 = Record("Wu-Tang Clan","C.R.E.A.M. (Cash Rules Everything Around Me)","Da Mystery Of Chessboxin’",1993,"Rap")
b_3 = Record("Prince","1999","How Come U Don’t Call Me Anymore?",1982,"Funk")
b_4 = Record("Black Sabbath","Sweet Leaf","After Forever",1971,"Metal")
b_5 = Record("The Stooges","Search And Destroy","Penetration",1973,"Rock")
c_1 = Record("XTC","Earn Enough For Us","Sacrificial Bonfire",1986,"Rock")
c_2 = Record("Dick Dale", "Misirlou Twist","Peppermint Man",1963,"Rock")
c_3 = Record("Megadeth","Wake Up Dead","Black Friday",1986,"Metal")
c_4 = Record("Run-D.M.C.","My Adidas","Peter Piper",1986,"Rap")
c_5 = Record("Aretha Franklin","Chain Of Fools","Prove It",1967,"Soul")
d_1 = Record("The Police","Message In A Bottle","Landlord",1979,"Rock")
d_2 = Record("Faith No More","From Out Of Nowhere","Cowboy Song",1989,"Metal")
d_3 = Record("James Brown","Get Up Offa That Thing","Release The Pressure",1976,"Funk")
d_4 = Record("Killing Joke","Wardance","Pssyche",1980,"Rock")
d_5 = Record("LFO","LFO (The Leeds Warehouse Mix)","Track 4",1990,"Techno")
e_1 = Record("Johnny Cash","Folsom Prison Blues","The Folk Singer",1968,"Country")
e_2 = Record("Nina Simone","Four Women","What More Can I Say",1966,"Jazz")
e_3 = Record("Michael Jackson","P.Y.T. (Pretty Young Thing)","Working Day And Night",1982,"Pop")
e_4 = Record("Mobb Deep","Shook Ones, Part II", "Shook Ones, Part I", 1995,"Rap")
e_5 = Record("Frank Zappa","Cosmik Debris","Uncle Remus",1974,"Rock")
f_1 = Record("LL Cool J","Go Cut Creator Go","Kanday",1987,"Rap")
f_2 = Record("Madonna","Vogue","Keep It Together",1990,"Pop")
f_3 = Record("Pete Rock & C.L. Smooth", "They Reminisce Over You (T.R.O.Y.)","Straighten It Out", 1992, "Rap")
f_4 = Record("The Beach Boys","Good Vibrations","Wouldn’t It Be Nice",1967,"Pop")
f_5 = Record("Public Enemy", "Bring The Noise","Sophisticated",1987,"Rap")
g_1 = Record("Simon & Garfunkel","Mrs. Robinson","Scarborough Fair (Canticle)",1968,"Folk")
g_2 = Record("Creedence Clearwater Revival","Run Through The Jungle","Up Around The Bend",1970,"Rock")
g_3 = Record("Ice Cube","Steady Mobbin’","Us",1991,"Rap")
g_4 = Record("Laura Branigan","Self Control","Silent Partners",1984,"Pop")
g_5 = Record("St. Vincent","Digital Witness","Rio",2014,"Rock")
h_1 = Record("Jerry Reed","Amos Moses","The Preacher And The Bear",1970,"Country")
h_2 = Record("Raekwon","Ice Cream","Incarcerated Scarfaces",1995,"Rap")
h_3 = Record("Patsy Cline","Crazy","Who Can I Count On",1961,"Country")
h_4 = Record("France Gall","La Cloche","Jazz à Gogo",1964,"Pop")
h_5 = Record("João Gilberto & Stan Getz","The Girl From Ipanema","Vivo Sonhando",1964,"Bossa Nova")
i_1 = Record("Gang Starr","Take It Personal","DWYCK",1992,"Rap")
i_2 = Record("Jon Lucien","Lady Love","Satan",1973,"Soul")
i_3 = Record("The Beatles","Strawberry Fields Forever","Penny Lane",1967,"Rock")
i_4 = Record("Blondie","Heart of Glass","Hanging On The Telephone",1978,"Rock")
i_5 = Record("Depeche Mode","Personal Jesus","Dangerous",1989,"Pop")
j_1 = Record("Nirvana","Heart-Shaped Box","Marigold",1993,"Rock")
j_2 = Record("Stevie Wonder","Higher Ground","Too High",1973,"Funk")
j_3 = Record("Tears For Fears","Everybody Wants To The Rule The World","Pharaohs",1985,"Pop")
j_4 = Record("The Fall","Cruiser’s Creek","L.A.",1985,"Rock")
j_5 = Record("Sly & The Family Stone","Thank You (Falettinme Be Mice Elf Agin)","Everybody Is A Star",1969,"Funk")
"""
