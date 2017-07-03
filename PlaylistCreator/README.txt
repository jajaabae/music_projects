Author: (Jon) Atle Hoff Jaabæk
(/Jaabaek)
email: atrakatz@gmail.com (please include "PlaylistCreator" in email title)
Licence: Any part of the code or as a whole, may not be used for comercial purposes or in comercial products without the permission of the author. All may be used, edited and shared for private use.


Dosclaimer:
!!!-WARNING! This program will try to change the file-names of the media-files(to add tags). If you have playlists or simmilar that depend on the filenames of the media files, this program may render those useless. Therefore, use a test enviournment to test this program.
-This program may be messy as I was in the proscess of learning python while writing teese scripts/this program.
-I recomend that you run the program in a "safe" enviournment (on testfiles in a test-directory) until you can be confident that this program or the combination "you and this program" is not going to ruin your files,file system or media-organisation. 


notes:
-The program makes tags directly in the file names of the media-files.
-The program should work in any python enviournment with small changes. Most of theese should be variables in top of the files. Most of the needed changes (maybe all) should just be path-variable changes or the likes.
-"qpython" installed on the android device may be the easiest way to run the program without modifying it to much.
-The directories are not "general", but may be changed to root('/storage/sdcard1') for the music-files (musicDir).
-My android music player ("walkman" by sony (?)) wants the playlist to be without directories for the music-files. This is made by setting <playlistContainsPathsForFiles=0>.
!!-Android may need to be rebooted for the "media-database" to be updated before trying to open the playlists in the media player.
-The format of the playlist is M3U. Examples are in the file "TheFormat.txt" (from Wikipedia).


Steps to "run the program (if qpython is installed):
--------------------------------------------------
01: Make tags
-musicfiles first need to be in a writable folder. F.ex. in the programs dir.

02: Remove tags (if wanted)

03: generate playlists.
-MusicFiles have to be moved back to the music folder before creating the playlist.
-edit "TagSystem.txt" if needed
-I thing it does not create duplicates in playlist "D" for song with _{DzDw}_

04: to clean empty playlists
-Not ready for use
--------------------------------------------------


Further thoughts:
- I may want to make this program "better" and easier to use.
		- {{ Generate playlist of Dz-Dzf to se the leftovers better. }}
		- {{ Add BpmXX (and other important information?) }}
		- {{ Find all tags without playlist. }}
- I plan to use this program as a base for a program to organize my pictures.
	The finished program should have the folowing functions:
		- Tag pictures while browsing them. (include browsing by tags)
		- Create a copy of all my favorite images in one separate folder with the same hierarcy as the scource. (This will make a much smaller "folder" that is easier to show to others and to take extra backups of)
		- "detect colission" and allow the user to descide here.
		- (The program may get support for other madia types as well)


