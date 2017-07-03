mainPath='/storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
def generate():
    subdir= '03_playlistGenerator'
    filen='PlaylistGeneraterFromTags_v45.py'
    filb=mainPath+'/'+subdir+'/'+filen
    execfile(filb) 
def delete():
    subdir = '04_DeleteEmptyPlaylists' 
    filen='DeleteEmptyPlaylists_v06.py'
    filb=mainPath+'/'+subdir+'/'+filen
    execfile( filb )


generate()
#delete() 