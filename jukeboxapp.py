from jukebox import Jukebox
from record import *
import os
mom_and_pops_jukebox = Jukebox()

mom_and_pops_jukebox.initialize_box()

print mom_and_pops_jukebox.inventory['A'][5]
print mom_and_pops_jukebox.inventory['A'][5]['genre']

for k, v in mom_and_pops_jukebox.inventory.items():
    for array in v:
        for k, v in array.items():
            if k=="year":
                if v in range(1990,2000):
                    print ("%s by %s: The B-Side on this record is %s." % (array['aside'],array['artist'],array['bside']))
