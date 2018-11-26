from jukebox import Jukebox
mom_and_pops_jukebox = Jukebox()

mom_and_pops_jukebox.add_record(5,0)
print (mom_and_pops_jukebox.inventory[0])

mom_and_pops_jukebox.del_record(5)