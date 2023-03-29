import os 
import random
import time
clear = lambda: os.system("cls")

"""
#
#
#          _____                    _____           _______                   _____                    _____                    _____                    _____                    _____                                  
#         /\    \                  /\    \         /::\    \                 /\    \                  /\    \                  /\    \                  /\    \                  /\    \                 ______          
#        /::\    \                /::\____\       /::::\    \               /::\    \                /::\    \                /::\    \                /::\    \                /::\____\               |::|   |         
#       /::::\    \              /:::/    /      /::::::\    \             /::::\    \              /::::\    \              /::::\    \              /::::\    \              /:::/    /               |::|   |         
#      /::::::\    \            /:::/    /      /::::::::\    \           /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /:::/    /                |::|   |         
#     /:::/\:::\    \          /:::/    /      /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /                 |::|   |         
#    /:::/  \:::\    \        /:::/    /      /:::/    \:::\    \       /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/    /                  |::|   |         
#   /:::/    \:::\    \      /:::/    /      /:::/    / \:::\    \      \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/    /                   |::|   |         
#  /:::/    / \:::\    \    /:::/    /      /:::/____/   \:::\____\   ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    /      _____         |::|   |         
# /:::/    /   \:::\    \  /:::/    /      |:::|    |     |:::|    | /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/____/      /\    \  ______|::|___|___ ____ 
#/:::/____/     \:::\____\/:::/____/       |:::|____|     |:::|    |/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::\____\|:::|    /      /::\____\|:::::::::::::::::|    |
#\:::\    \      \::/    /\:::\    \        \:::\    \   /:::/    / \:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /|:::|____\     /:::/    /|:::::::::::::::::|____|
# \:::\    \      \/____/  \:::\    \        \:::\    \ /:::/    /   \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \:::\    \   /:::/    /  ~~~~~~|::|~~~|~~~      
#  \:::\    \               \:::\    \        \:::\    /:::/    /     \:::\   \:::\    \       \:::\   \:::\    \       \:::\   \:::\    \               \::::::/    /    \:::\    \ /:::/    /         |::|   |         
#   \:::\    \               \:::\    \        \:::\__/:::/    /       \:::\   \:::\____\       \:::\   \:::\____\       \:::\   \:::\____\               \::::/    /      \:::\    /:::/    /          |::|   |         
#    \:::\    \               \:::\    \        \::::::::/    /         \:::\  /:::/    /        \:::\   \::/    /        \:::\   \::/    /               /:::/    /        \:::\__/:::/    /           |::|   |         
#     \:::\    \               \:::\    \        \::::::/    /           \:::\/:::/    /          \:::\   \/____/          \:::\   \/____/               /:::/    /          \::::::::/    /            |::|   |         
#      \:::\    \               \:::\    \        \::::/    /             \::::::/    /            \:::\    \               \:::\    \                  /:::/    /            \::::::/    /             |::|   |         
#       \:::\____\               \:::\____\        \::/____/               \::::/    /              \:::\____\               \:::\____\                /:::/    /              \::::/    /              |::|   |         
#        \::/    /                \::/    /         ~~                      \::/    /                \::/    /                \::/    /                \::/    /                \::/____/               |::|___|         
#         \/____/                  \/____/                                   \/____/                  \/____/                  \/____/                  \/____/                  ~~                      ~~              
#                                                                                                                                                                                                                
#
#
"""

class squad:
    def __init__(self, activesquad, squad1, squad2, cooldown, round):
        self.activesquad = activesquad
        self.squad1 = squad1
        self.squad2 = squad2
        self.cooldown = cooldown
        self.round = round
    def squadchange(self):
        if self.activesquad == 1:
            self.activesquad = 2
        else:
            self.activesquad = 1


one = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |     __       | |\n| |    /  |      | |\n| |    `| |      | |\n| |     | |      | |\n| |    _| |_     | |\n| |   |_____|    | |\n| |              | |\n| '--------------' |\n '----------------' "
two = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |    _____     | |\n| |   / ___ `.   | |\n| |  |_/___) |   | |\n| |   .'____.'   | |\n| |  / /____     | |\n| |  |_______|   | |\n| |              | |\n| '--------------' |\n '----------------' "
tree = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |    ______    | |\n| |   / ____ `.  | |\n| |   `'  __) |  | | \n| |   _  |__ '.  | |\n| |  | \____) |  | |\n| |   \______.'  | |\n| |              | |\n| '--------------' |\n '----------------' "
four = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |   _    _     | |\n| |  | |  | |    | |\n| |  | |__| |_   | |\n| |  |____   _|  | |\n| |      _| |_   | |\n| |     |_____|  | |\n| |              | |\n| '--------------' |\n '----------------' "
five = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |   _______    | |\n| |  |  _____|   | |\n| |  | |____     | |\n| |  '_.____''.  | |\n| |  | \____) |  | |\n| |   \______.'  | |\n| |              | |\n| '--------------' |\n '----------------' "
six = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |    ______    | |\n| |  .' ____ \   | |\n| |  | |____\_|  | |\n| |  | '____`'.  | |\n| |  | (____) |  | |\n| |  '.______.'  | |\n| |              | |\n| '--------------' |\n '----------------' "
x = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |  ____  ____  | |\n| | |_  _||_  _| | |\n| |   \ \  / /   | |\n| |    > `' <    | |\n| |  _/ /'`\ \_  | |\n| | |____||____| | |\n| |              | |\n| '--------------' |\n '----------------' "
y = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |  ____  ____  | |\n| | |_  _||_  _| | |\n| |   \ \  / /   | |\n| |    \ \/ /    | |\n| |    _|  |_    | |\n| |   |______|   | |\n| |              | |\n| '--------------' |\n '----------------' "
z = "\033[1;37;40m" + " .----------------. \n| .--------------. |\n| |   ________   | |\n| |  |  __   _|  | |\n| |  |_/  / /    | |\n| |     .'.' _   | |\n| |   _/ /__/ |  | |\n| |  |________|  | |\n| |              | |\n| '--------------' |\n '----------------' "

firework1 = "\033[0;31;40m    *\n    .\n    .\n    ."


firework2 = "\033[0;32;40m   *''*\n  *_\/_*\n  * /\ *\n   *''* "

firework3 = "\033[0;33;40m   *''* \n* *_\/_* *\n* * /\ * *\n   *''* "

firework4 = "\033[0;34;40m   *''* \n* .    . *\n* .    . *\n   *''* "

firework5 = "\033[0;35;40m   .  . \n. .    . .\n. .    . .\n   .  . "

firework6 = "\033[0;36;40m   .  .\n.        .\n.        .\n   .  ."


firework7 = "\033[1;37;40m  YES!! :)"

global activesquad 

activesquad = squad(1, 0, 0, False, 1)
aktstext = "\033[1;37;40m" + "Active Team: " + str(activesquad.activesquad)


teamtext1 = "\033[0;31;40m" + "Team 1:  " + str(activesquad.squad1) + " Points"
teamtext2 = "\033[0;34;40m" + "Team 2:  " + str(activesquad.squad2) + " Points"
roundstext = "\033[1;37;40m" + "Current Round: " + str(activesquad.round)

def firework():
    print(firework1)
    time.sleep(0.1)
    clear()
    print(firework2)
    print(firework1)
    time.sleep(0.2)
    clear()
    print(firework3)
    print(firework2)
    print(firework1)
    time.sleep(0.2)
    clear()
    print(firework4)
    print(firework3)
    print(firework2)
    print(firework1)
    time.sleep(0.3)
    clear()
    print(firework5)
    print(firework4)
    print(firework3)
    print(firework2)
    print(firework1)
    time.sleep(0.3)
    clear()
    print(firework7)
    print(firework6)
    print(firework5)
    print(firework4)
    print(firework3)
    print(firework2)
    print(firework1)
    time.sleep(1)
    refresh()


def Header():
    teamtext1 = "\033[0;31;40m" + "Team 1:  " + str(activesquad.squad1) + " Points"
    teamtext2 = "\033[0;34;40m" + "Team 2:  " + str(activesquad.squad2) + " Points"
    aktstext = "\033[1;37;40m" + "Current Team: " + str(activesquad.activesquad)
    roundstext = "\033[1;37;40m" + "Current Round: " + str(activesquad.round)
    print("\033[1;37;40m" + " __          __               __     _ \n \ \        / /              / _|   | |\n  \ \  /\  / /   _  ___ _ __| |_ ___| |\n   \ \/  \/ / | | |/ _ \ '__|  _/ _ \ |\n    \  /\  /| |_| |  __/ |  | ||  __/ |\n     \/  \/  \__,_|\___|_|  |_| \___|_|")
    print("\033[1;37;40m" + "Enter to Roll")
    print(" \n " + teamtext1 + "\n\n " + teamtext2 + " \n\n " + aktstext + "\n \n " + roundstext + "\n")

def refresh():
    clear()
    Header()

def anima():
    clear()
    print(x)
    time.sleep(0.2)
    clear()
    print(y)
    time.sleep(0.2)
    clear()
    print(z)
    time.sleep(0.2)


def Roll(value, one = one, two = two, tree = tree, four = four, five = five, six = six, x=x,y=y,z=z):
    # reroll
    if activesquad.cooldown == False:
        activesquad.cooldown = True
        if activesquad.activesquad == 1:
            activesquad.squad1 += value
        else:
            activesquad.squad2 += value
            activesquad.round += 1

        anima()
        anima()
        anima()
        activesquad.squadchange()
        refresh()
        if value == 1:
            print(one)
        elif value == 2:
            print(two)
        elif value == 3:
            print(tree)
        elif value == 4:
            print(four)
        elif value == 5:
            print(five)
        elif value == 6:
            firework()
            print(six) 

        activesquad.cooldown = False
        inp = input()
        Roll(random.randint(1,6))



Header()
clear()
Header()
inp = input()
Roll(random.randint(1,6))
