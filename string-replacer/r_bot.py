###########################################################################
###                                                                     ###
###                                                                     ###
###                         REPLACE BOT                                 ###
###     (replaces specified keys with values at in specified files)     ###
###             (and creates backup of the original file)               ###
###                                                                     ###
###########################################################################

###         

###         Loads names of targeted files from "r_target_files.txt"
###         Loads keys to be replaced from "r_keys.txt"
###         Loads values to replace them with from "r_values.txt"
###         Also creates a backup of the file prior to replacement; ie 'BACKUP foobar.txt'
###         key, value, file_list, and backups all work in the same directory.

VERBOSITY=False                         ##  Mostly for debugging. Shows a bunch more detail if set to True

target_files = "r_target_files.txt"     ##  This file contains names of all the fils that need processing.
key_file = "r_keys.txt"                 ##  Where the keys are stored
value_file = "r_values.txt"             ##  WHere values are stored


### Loads and returns contents of a file
### INPUT:  _filename_ (string) representing location/name of the file
###         _verbose_ (boolean) goes into 'verbose' mode if set to True
### OUTPUT: _contents_ [list] of file contents
###         FALSE if indicated file does not exist
def load_contents_of_file(filename, strip_newline, verbose):
    import os.path
    if not os.path.isfile(filename):                                    # If the file doesn't exist, notify console and automatically return False.
        print "UNABLE TO OPEN FILE " + filename
        print "FULL FILE PATH: " + os.getcwd() + "\\" + filename
        return False
    if verbose: print "--------------------- <"+ filename+"> LOADING CONTENTS..."
    contents = []
    f = open(filename, 'r')
    line = f.readline()
    counter = 0
    while len(line) > 0:
        counter+=1
        if verbose: print "LINE "+str(counter)+": "+line.strip('\n')
        if strip_newline: line = line.strip("\n")
        contents.append(line)
        line = f.readline()
    if verbose: print "--------------------- <"+ filename+"> LOADING CONTENTS... COMPLETED"
    if verbose: print '\n'
    f.close()
    return contents

### Checks if a file exists, returns a boolean accordingly.
### INPUT: a string representing full directory and name of file.
def is_file(filename):
    import os.path
    if(os.path.isfile(filename)):
        return True
    else:
        print "UNABLE TO OPEN FILE " + filename
        print "Full file path: " + os.getcwd() + "\\" + filename
    return False

### Loads _filename_ file into memory, looks for instances of _keys_ and replaces them with appropriate _values_
### INPUT:  _filename_  : (string) of the name of the file
###         _keys_      : [list] of keys to look for within the file
###         _values_    : [list] of values to replace the keys with
###         _verbose_   : boolean of whether or not to spell everything out.
def replace_values(filename, keys, values, verbose):
    if(is_file):
        replacement_performed = False
        contents = load_contents_of_file(filename,False,verbose)
        for line in range(0,len(contents)):
            for k in range(0,len(keys)):
                if(contents[line].find(keys[k]) >= 0):
                   contents[line] = contents[line].replace(keys[k],values[k])
                   replacement_performed = True
                   print "Replacement on line", (line+1), "of", filename, ":"
                   print "#"+keys[k]+"# with #"+values[k]+"#"
    if not replacement_performed: print "No keys were located in", filename
    return contents
            
### Writes passed contents to a file
### INPUT:  _filename_  : (string) of the name of the file
###         _contents_    : [list] of things to write into the file
###         _verbose_   : boolean of whether or not to spell everything out.
def write_to_file(filename,contents,verbose):
    verb = "OVER-WRITING"
    if(not is_file(filename)):
        if verbose: print filename+" does not exist yet. WIll be created..."
        verb = "WRITING"
    if verbose: print "\n"
    if verbose: print "--------------------- <"+ filename+"> "+verb+"..."
    
    f = open(filename, 'w')
    for line in contents:
        f.write(line)
    if verbose: print "....................."
    if verbose: print "--------------------- <"+filename+"> "+verb+"... COMPLETED"
    print "\n"
    f.close()

### Returns name of the file by exploding the splitting the _directory_ and returning whatever's after the last '/'
### INPUT:  _directory_ string of location of file; ie          'contents/test.txt'
### OUTPUT:             string depicting name of the file; ie   'test.txt'
def get_filename(directory):
    folders = directory.split("/")
    return folders[len(folders)-1]

############################################################################################################################



print "############################################################################################"
print "--- LOADING FILES + KEYS + VALUES..."
print "\n"
files = load_contents_of_file(target_files,True,VERBOSITY)
keys = load_contents_of_file(key_file,True,VERBOSITY)
values = load_contents_of_file(value_file,True,VERBOSITY)
for k in range(0,len(keys)):
    print "-- WILL REPLACE '"+keys[k]+"' WITH '"+values[k]+"'"
print "\n"
print "--- LOADING FILES + KEYS + VALUES... COMPLETED"
print "############################################################################################"
print "\n"

backup_counter = 0

for f in files:
    backup_counter+=1
    print "--- PROCESSING <"+f+">..."
    contents = load_contents_of_file(f,False,VERBOSITY)                 #   First load contents of the file and create a BACKUP of it
    write_to_file("BACKUP"+str(backup_counter)+" "+get_filename(f),contents,VERBOSITY)
    contents = replace_values(f,keys,values,VERBOSITY)                  #   Then process its contents and over-write the original
    write_to_file(f,contents,False)
    print "--- PROCESSING <"+f+">... COMPLETED"
