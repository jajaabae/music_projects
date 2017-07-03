import os

android = 1
if android == 1:
    basePath='storage/sdcard0/com.hipipal.qpyplus/scripts/'
else:
    basePath='C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/'
#pht='storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator/combined/12_playlistGenerator'
#pht='C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/PlaylistCreator/combined/12_playlistGenerator'
projectPath = 'PlaylistCreator/combined/16_playlistGeneratorCombined'
pht = basePath + projectPath

if android ==1:
    musicDir='/storage/sdcard1/music'
else:
    musicDir=pht+'/'+'music'
print musicDir
##PLPath=pht+'/'+'playlists'
#path=pht
##os.chdir(PLPath)
os.chdir(pht)
print os.getcwd()
print ''


import genPlaylist.PlaylistGeneraterFromTags_v46 as a
import genPlaylist.DeleteEmptyPlaylists_v07 as b

a.runProg(musicDir)
if 1==1:
    b.runProg()