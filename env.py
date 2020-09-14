# --------env.py-----------------
# Authors: Caleb Carr & Bibi Dang
# Date   : 14 Sept 2020
# Desc.  : testing ground for room placement and action relationships

import textworld
from textworld import GameMaker
from textworld import g_rng
g_rng.set_seed(20200914)

M = GameMaker()

# "rooms"
start = M.new_room('Start')
if_room = M.new_room('if')
var_room = M.new_room('variables')
for_room = M.new_room('for')
print_room = M.new_room('print')
else_room = M.new_room('else')

# room connections
start_to_var = M.connect(start.south, var_room.north)
start_to_if = M.connect(start.east, if_room.west)
start_to_for = M.connect(start.west, for_room.east)
start_to_print = M.connect(start.north, print_room.south)
if_to_else = M.connect(if_room.east, else_room.west)
if_to_var = M.connect(if_room.south, var_room.east)
else_to_var = M.connect(else_room.east, var_room.south)

# place the machine in the start room
M.set_player(start)

# visualize
M.render()
