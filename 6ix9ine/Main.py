import random

#  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$     /$$ /$$      /$$  /$$$$$$  /$$     /$$
# |__  $$__/| $$__  $$ /$$__  $$|  $$   /$$/| $$  /$ | $$ /$$__  $$|  $$   /$$/
#    | $$   | $$  \ $$|__/  \ $$ \  $$ /$$/ | $$ /$$$| $$| $$  \ $$ \  $$ /$$/
#    | $$   | $$$$$$$/   /$$$$$/  \  $$$$/  | $$/$$ $$ $$| $$$$$$$$  \  $$$$/
#    | $$   | $$__  $$  |___  $$   \  $$/   | $$$$_  $$$$| $$__  $$   \  $$/
#    | $$   | $$  \ $$ /$$  \ $$    | $$    | $$$/ \  $$$| $$  | $$    | $$
#    | $$   | $$  | $$|  $$$$$$/    | $$    | $$/   \  $$| $$  | $$    | $$
#    |__/   |__/  |__/ \______/     |__/    |__/     \__/|__/  |__/    |__/
#
# This is a program to create bespoke songs using the style of Tekashi 6ix9ine
# In the form of:
#               -- intro
#               -- verse 1
#               -- chorus
#               -- verse 2 (feature)
#               -- chorus
#               -- outro
#
#   /$$$$$$   /$$$$$$  /$$   /$$ /$$      /$$      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$
# /$$__  $$ /$$__  $$| $$  | $$| $$$    /$$$     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
# | $$  \__/| $$  \__/| $$  | $$| $$$$  /$$$$    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
# |  $$$$$$ | $$      | $$  | $$| $$ $$/$$ $$    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
#  \____  $$| $$      | $$  | $$| $$  $$$| $$    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
#  /$$  \ $$| $$    $$| $$  | $$| $$\  $ | $$    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$
# |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \/  | $$    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
#  \______/  \______/  \______/ |__/     |__/     \______/ |__/  |__/|__/  \__/ \______/


def print_ascii_art():
    # Function to add sick ascii art in the console
    treyway = ("""\
     /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$     /$$ /$$      /$$  /$$$$$$  /$$     /$$
    |__  $$__/| $$__  $$ /$$__  $$|  $$   /$$/| $$  /$ | $$ /$$__  $$|  $$   /$$/
       | $$   | $$  \ $$|__/  \ $$ \  $$ /$$/ | $$ /$$$| $$| $$  \ $$ \  $$ /$$/
       | $$   | $$$$$$$/   /$$$$$/  \  $$$$/  | $$/$$ $$ $$| $$$$$$$$  \  $$$$/
       | $$   | $$__  $$  |___  $$   \  $$/   | $$$$_  $$$$| $$__  $$   \  $$/
       | $$   | $$  \ $$ /$$  \ $$    | $$    | $$$/ \  $$$| $$  | $$    | $$
       | $$   | $$  | $$|  $$$$$$/    | $$    | $$/   \  $$| $$  | $$    | $$
       |__/   |__/  |__/ \______/     |__/    |__/     \__/|__/  |__/    |__/
                        """)
    scumgang = ("""\
      /$$$$$$   /$$$$$$  /$$   /$$ /$$      /$$      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$
     /$$__  $$ /$$__  $$| $$  | $$| $$$    /$$$     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
     | $$  \__/| $$  \__/| $$  | $$| $$$$  /$$$$    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
     |  $$$$$$ | $$      | $$  | $$| $$ $$/$$ $$    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
      \____  $$| $$      | $$  | $$| $$  $$$| $$    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
      /$$  \ $$| $$    $$| $$  | $$| $$\  $ | $$    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$
     |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \/  | $$    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
      \______/  \______/  \______/ |__/     |__/     \______/ |__/  |__/|__/  \__/ \______/
                        """)
    gangshit = ("""\
      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$       /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$$
     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$     /$$__  $$| $$  | $$|_  $$_/|__  $$__/
    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/    | $$  \__/| $$  | $$  | $$     | $$   
    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$    |  $$$$$$ | $$$$$$$$  | $$     | $$   
    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$     \____  $$| $$__  $$  | $$     | $$   
    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$     /$$  \ $$| $$  | $$  | $$     | $$   
    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/    |  $$$$$$/| $$  | $$ /$$$$$$   | $$   
     \______/ |__/  |__/|__/  \__/ \______/      \______/ |__/  |__/|______/   |__/   
                """)
    splishsplash = ("""\
      /$$$$$$  /$$$$$$$  /$$       /$$$$$$  /$$$$$$  /$$   /$$      /$$$$$$  /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$
     /$$__  $$| $$__  $$| $$      |_  $$_/ /$$__  $$| $$  | $$     /$$__  $$| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  | $$
    | $$  \__/| $$  \ $$| $$        | $$  | $$  \__/| $$  | $$    | $$  \__/| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$  | $$
    |  $$$$$$ | $$$$$$$/| $$        | $$  |  $$$$$$ | $$$$$$$$    |  $$$$$$ | $$$$$$$/| $$      | $$$$$$$$|  $$$$$$ | $$$$$$$$
     \____  $$| $$____/ | $$        | $$   \____  $$| $$__  $$     \____  $$| $$____/ | $$      | $$__  $$ \____  $$| $$__  $$
     /$$  \ $$| $$      | $$        | $$   /$$  \ $$| $$  | $$     /$$  \ $$| $$      | $$      | $$  | $$ /$$  \ $$| $$  | $$
    |  $$$$$$/| $$      | $$$$$$$$ /$$$$$$|  $$$$$$/| $$  | $$    |  $$$$$$/| $$      | $$$$$$$$| $$  | $$|  $$$$$$/| $$  | $$
     \______/ |__/      |________/|______/ \______/ |__/  |__/     \______/ |__/      |________/|__/  |__/ \______/ |__/  |__/
                """)
    schmurder = ("""\
      /$$$$$$   /$$$$$$  /$$   /$$ /$$      /$$ /$$   /$$ /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
     /$$__  $$ /$$__  $$| $$  | $$| $$$    /$$$| $$  | $$| $$__  $$| $$__  $$| $$_____/| $$__  $$
    | $$  \__/| $$  \__/| $$  | $$| $$$$  /$$$$| $$  | $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
    |  $$$$$$ | $$      | $$$$$$$$| $$ $$/$$ $$| $$  | $$| $$$$$$$/| $$  | $$| $$$$$   | $$$$$$$/
     \____  $$| $$      | $$__  $$| $$  $$$| $$| $$  | $$| $$__  $$| $$  | $$| $$__/   | $$__  $$
     /$$  \ $$| $$    $$| $$  | $$| $$\  $ | $$| $$  | $$| $$  \ $$| $$  | $$| $$      | $$  \ $$
    |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \/  | $$|  $$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
     \______/  \______/ |__/  |__/|__/     |__/ \______/ |__/  |__/|_______/ |________/|__/  |__/
                """)
    ascii_options = (treyway, scumgang, gangshit, splishsplash, schmurder)
    print(random.choice(ascii_options))


def create_finished_song():
    # Function to put together all the elements for your finished 6ix9ine Masterpiece
    create_song_name()


def create_song_name():
    # Function to make the song title
    # 4 letter words, all caps, consonants characters 1 and 3, vowels 2 and 4, vowels same on both
    # Populating lists of consonants and vowels
    consonants = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    vowels = ("A", "E", "I", "O", "U")

    # Create the song name
    repeated_vowel = random.choice(vowels)
    songname = random.choice(consonants) + repeated_vowel + random.choice(consonants) + repeated_vowel
    print("Your song title is: \"" + songname + "\"")


print_ascii_art()
create_finished_song()
