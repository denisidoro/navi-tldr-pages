; This has been extracted from
; https://github.com/tldr-pages/tldr/blob/master/pages/common/md5sum.md

% common5sum.md

# Calculate the MD5 checksum for a file
md5sum <filename1>

# Calculate MD5 checksums for multiple files
md5sum <filename1> <filename2>

# Read a file of MD5SUMs and verify all files have matching checksums
md5sum -c <filename_md5>
