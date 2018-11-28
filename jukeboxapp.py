#Runs most optimally in Python 3.7
from jukebox import Jukebox, main_menu
from record import *
import os
mom_and_pops_jukebox = Jukebox()
mom_and_pops_jukebox.initialize_box()

if (main_menu):
    mom_and_pops_jukebox.start_up()
