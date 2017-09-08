'''
gmod_mapcycle_rand.py

This program randomizes the mapcycle for any gmod server.
Put this file in the root of your server directory and run it using:
    python3.5 gmod_mapcycle_rand.py
If that doesn't work, see the README.md for details in installing
The mapcycle of gmod (mapcycle.txt) comes part of just about every gmod server by default.
It is stored in /garrysmod/cfg/mapcycle.txt
'''
import random

# Shuffles a list while ignoring comments (//)
def shuffle(list):
    # Allowed indexes is the line numbers that are not commented out
    allowedIndexes = []
    # go through and put the indexes of the lines in the list
    # that do not start with //
    for i in range(len(list)):
        currentLine = list[i]
        if (currentLine.find('//') == -1):
            allowedIndexes.append(i)
    # randomize!
    for i in range(len(allowedIndexes)):
        # Choose random index within the allowed indexes
        currentLineIndex = allowedIndexes[i]
        otherLineIndex = allowedIndexes[int(random.randrange(0, len(allowedIndexes) - 1))]
        # Swap the the other line with the current line
        hold = list[currentLineIndex]
        list[currentLineIndex] = list[otherLineIndex]
        list[otherLineIndex] = hold
    return list


mapCycleOpenedSuccessfully = False
mapcycleDefaultPath = "garrysmod/cfg/mapcycle.txt"
lines = []

#Intro
print("*** GMOD mapcycle randomizer by Noah Dueck (https://github.com/duecknoah) ***")

# Get user to decide how to open map
while (not mapCycleOpenedSuccessfully):
    mapcyclePath = input("File name (with file path and extension) of mapcycle: (default: {}) ".format(mapcycleDefaultPath))

    if mapcyclePath == "":
        mapcyclePath = mapcycleDefaultPath
        print("Using default path", mapcycleDefaultPath)
    try:
        # Attempt to Read file and Split lines into separate strings in a list
        with open(mapcyclePath, "r+") as mapcycleFile:
            lines = mapcycleFile.readlines()
        mapcycleFile.close()
        mapCycleOpenedSuccessfully = True
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("IO error, try again")

# Reorder list randomly, do not affect commented lines
print("randomizing ... ", end="")
lines = shuffle(lines)
allData = ""
for i in lines:
    allData += i

# re-write randomized mapcycle file to the mapCyclePath
try:
    mapcycleFile = open(mapcyclePath, "wb")
    mapcycleFile.write(bytes(allData, 'UTF-8'))
    print("mapcycle randomized successfully.")
except FileNotFoundError:
    print("File not found, aborting ...")
except IOError:
    print("IOError with mapcycle.txt file, aborting ...")
finally:
    mapcycleFile.close()