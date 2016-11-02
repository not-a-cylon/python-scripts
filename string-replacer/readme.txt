Updated 3 minutes ago
A quick python script that searches within specified files and replaces specified keys with... wait for it... specified values!
This one was written to help migrate a website from one server to another by replacing absolute path references.

Currently only compatible with Python 2.7, as that's what I had configured at the time...

Also might not scale well, since a file's entire contents will be loaded into memory while replacing the strings... The largest file I've used it on is only 4KB, and for my purposes, the filesize isn't likely to grow much more.


To run, specify the filenames, keys, and values in proper .txt files.
The script and associated r_*.txt files must be placed with the same parent directory of the files being scanned.
The first line in r_keys.txt will be matched and replaced with the first line in the r_values.txt, second line with second line, etc...
Avoid blank lines when specifying keys and vals. Script will throw a fuss.
