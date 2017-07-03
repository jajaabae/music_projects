import os
pht='storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator/combined/12_playlistGenerator'
#pht='C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/PlaylistCreator/combined/12_playlistGenerator'


musicDir='/storage/sdcard1/music'
#musicDir=pht+'/'+'music'

PLPath=pht+'/'+'playlists'
#path=pht
os.chdir(PLPath)
print os.getcwd()
print ''


import genPlaylist.PlaylistGeneraterFromTags_v46 as a
import genPlaylist.DeleteEmptyPlaylists_v07 as b

a.runProg(musicDir)

if 1==0:
    b.runProg()