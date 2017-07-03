import os

projectPath = 'PlaylistCreator/combined/17_playlistGeneratorCombined'

android = 1
if android == 1:
    basePath='storage/sdcard0/com.hipipal.qpyplus/scripts/'
    pht = basePath + projectPath
    musicDir='/storage/sdcard1/music'
else:
    basePath='C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/'
    pht = basePath + projectPath
    musicDir=pht+'/'+'music'
##print musicDir
os.chdir(pht)
print os.getcwd()
print ''

# playlistPath = basePath + ...

import genPlaylist.PlaylistGeneraterFromTags_v46 as a
import genPlaylist.DeleteEmptyPlaylists_v07 as b

a.runProg(musicDir)
if 1==1:
    b.runProg()
    
