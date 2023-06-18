# safari-reading-list
Sync my safari reading list to GitHub.

## Update step
1. Copy `~/Library/Safari/Bookmarks.plist` using Finder. It might not work if trying to do so in a terminal even with `sudo`, since this folder seems to be special with special extended attributes.
2. Run `$ plutil -convert xml1 -o Bookmarks.plist.xml Bookmarks.plist` to convert the plist file into xml.
3. Run `$ python3 parser.py`.
