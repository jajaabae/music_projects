import os

os.chdir('/storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator/playlists')
delete=1

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
            if len(a)==2:
                if (a[0]=='#EXTM3U') & (a[1]==''):
                    print file
                    print 'L1: '+a[0]
                    print 'L2: '+a[1]
                    #print a[1]==''
                    print 'len='+str(len(a))
                    print ''
                    if delete==1:
                        print 'deleting'
                        os.remove(file)
                        print 'deleted'
deleteEmptyPlaylists()