import os
pht='storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
os.chdir(pht)
print os.getcwd()
print ''

import genPlaylist.DeleteEmptyPlaylists_v07 as a
import genPlaylist.PlaylistGeneraterFromTags_v46 as b

#a.runProg()
b.runProg()