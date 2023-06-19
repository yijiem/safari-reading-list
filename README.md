# safari-reading-list
Upload my safari reading list to GitHub so that I can read on non-apple devices.

## Update step
1. Copy `~/Library/Safari/Bookmarks.plist` using Finder. It might not work if trying to do so in a terminal (even with `sudo`). Since this folder seems to have special access control with extended attributes.
2. Run `$ plutil -convert xml1 -o Bookmarks.plist.xml Bookmarks.plist` to convert the plist file into xml.
3. Run `$ python3 parser.py`.
