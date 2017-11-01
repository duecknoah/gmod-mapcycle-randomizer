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
import sys

def shuffle(map_list):
    """Shuffles a list while ignoring comments (//)"""
    # Allowed indexes is the line numbers that are not commented out
    allowed_indexes = []
    # go through and put the indexes of the lines in the list
    # that do not start with //
    for i, item in enumerate(map_list):
        current_line = item
        if current_line.find('//') == -1:
            allowed_indexes.append(i)
    # randomize!
    for i, item in enumerate(allowed_indexes):
        # Choose random index within the allowed indexes
        current_line_index = item
        other_line_index = allowed_indexes[int(random.randrange(0, len(allowed_indexes) - 1))]
        # Swap the the other line with the current line
        hold = map_list[current_line_index]
        map_list[current_line_index] = map_list[other_line_index]
        map_list[other_line_index] = hold
    return map_list

if __name__ == '__main__':
    map_cycle_opened_successfully = False
    map_cycle_default_path = "garrysmod/cfg/mapcycle.txt"
    lines = []

    #Intro
    print("*** GMOD mapcycle randomizer (https://github.com/duecknoah/gmod-mapcycle-randomizer) ***")

    # If no arguments entered, make user manually enter mapcycle path.
    # If 2 arguments entered, use arg[1] as mapcycle path
    # Else throw an error as too many arguments were passed
    if len(sys.argv) < 2:
        map_cycle_path = input("File name (with file path and extension)"
                               " of mapcycle: (default: {}) ".format(map_cycle_default_path))
    elif len(sys.argv) == 2:
        map_cycle_path = sys.argv[1]
    else:
        raise ValueError('Too many arguments entered, usage: python3 gmod_mapcycle_rand.py path/to/mapcycle')


    if map_cycle_path == "":
        map_cycle_path = map_cycle_default_path
        print("Using default path", map_cycle_default_path)
    try:
        # Attempt to Read file and Split lines into separate strings in a list
        with open(map_cycle_path, "r+") as map_cycle_file:
            lines = map_cycle_file.readlines()
        map_cycle_file.close()
        map_cycle_opened_successfully = True

        # If there is no newline at end of file, add one
        last_line_index = len(lines) - 1
        last_line = lines[last_line_index]
        last_char = last_line[len(last_line) - 1]
        if last_char != '\n':
            lines[last_line_index] += '\n'

    except FileNotFoundError:
        print("***** mapcycle file not found, unable to randomize file. *****")
        exit(2)
    except IOError:
        print("***** IO error, unable to randomize file. *****")
        exit(3)

    # Reorder list randomly, do not affect commented lines
    print("randomizing ... ", end="")
    lines = shuffle(lines)
    all_data = ""
    for i in lines:
        all_data += i

    # re-write randomized mapcycle file to the mapCyclePath
    map_cycle_file = None
    try:
        map_cycle_file = open(map_cycle_path, "wb")
        map_cycle_file.write(bytes(all_data, 'UTF-8'))
        print("mapcycle randomized successfully.")
    except FileNotFoundError:
        print("File not found, aborting ...")
    except IOError:
        print("IOError with mapcycle.txt file, aborting ...")
    finally:
        map_cycle_file.close()
