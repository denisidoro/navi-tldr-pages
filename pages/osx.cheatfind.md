; This has been extracted from
; https://github.com/tldr-pages/tldr/blob/master/pages/osx/mdfind.md

% osxfind.md

# Find a file by its name
mdfind -name <file>

# Find a file by its content
mdfind <query>

# Find a file containing a string, in a given directory
mdfind -onlyin <directory> <query>
