import os

os.chdir('/storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator/playlists')


def deleteEmptyPlaylists():
    
    direc = os.getcwd()
    files = os.listdir(direc)
    print files
    print '###########'
    for file in files:
        if os.path.isfile(file):
            t=open(file,'r')
            a=t.read()
            a=a.split('\n')
            #print a
            #print len(a)
            t.close()
            if len(a)==1:
                if a[0]=='#EXTM3U':
                    print file
                    #print length of file
                    #os.delete(file)
deleteEmptyPlaylists()