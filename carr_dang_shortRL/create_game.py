
# --------create_game.py-----------------
# Authors: Caleb Carr & Bibi Dang
# Date   : 14 Sept 2020
# Desc.  : create and compile custom game

import argparse
import string
import random
import textworld
from textworld import GameMaker
from textworld.logic import Proposition

from textworld import g_rng


def make_example_game(args):
    g_rng.set_seed(20201008)

    M = GameMaker()

    # Define rooms
    roomS = M.new_room(name="start", desc="\n")
    roomI = M.new_room(name="if", desc="\n")
    roomV = M.new_room(name="variable", desc="\n")
    roomF = M.new_room(name="for", desc="\n")

    # Define connections
    connectSI = M.connect(roomS.east, roomI.west)
    connectSV = M.connect(roomS.south, roomV.north)
    connectFS = M.connect(roomF.east, roomS.west)

    # Set player
    M.set_player(roomS)

    #Create objects
    i_rand=random.choice(string.ascii_letters)
    f_rand=random.choice(string.ascii_letters)
    v_rand=random.choice(string.ascii_letters)

    objectI = M.new(type='o', name=i_rand, desc="if")
    objectF = M.new(type='o', name=f_rand, desc="for")
    objectV = M.new(type='o', name=v_rand, desc="variable")

    #Add objects to rooms
    roomI.add(objectI)
    roomF.add(objectF)
    roomV.add(objectV)

    #Print object names for testing (will not be in game)
    print(objectI.name)
    print(objectF.name)
    print(objectV.name)

    #Create quests with assigned rewards
    q1 = M.record_quest() #Create quest for including completed if statement
    q1.reward = 1 #Reward for completing if statement (sparse=1, dense=5, balanced=1)
    q2 = M.record_quest() #Create quest for including complete for loop
    q2.reward = 1 #Reward for completing for loop (same distribution as if)
    q3 = M.record_quest() #Create quest for including print statement
    q3.reward = 1 #Reward for completing print statement (sparse=0, dense=1, balanced=1)
    q4 = M.record_quest() #Create quest for including new variable assignment
    q4.reward = 1 #Reward for completing variable assignment (same distribution as print)

    #Create game and associated files
    game_file = M.compile("./carr_dang_shortRL/compiled_game/games.ulx")

    return game_file


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default="./game.ulx",
        help="Name of the generated game. Default: exmaple.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    game_file = make_example_game(args)
