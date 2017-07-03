import os

#Generate playlistfiles from TagSystem.txt (ignore "#"-lines)
path='storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
path='storage/sdcard0/'
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PyIOFolder'
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'

os.chdir(path)
print os.listdir(os.getcwd())

f=open('TagSystem.txt','r')
for line in f:
    line =str(line.strip())
    if len(line)>0:
        if not line[0]=='#':
            #print str(line[0:10])
            #print 'TagStart: '
            #print str(line[0:10]) == 'TagStart: '
            #print len(line)>10
            #print len(line)>10 & line[0:10] == 'TagStart: '
            print '-------------'
            print ''
            print '-------------'
            if len(line)>10 & str(line[0:10])=='TagStart: ':
#            if len(line)>10:
#                if str(line[0:10])=='TagStart: ':
                    print 'a: '+line[0:10]
            elif len(line)>10:
                print 'b: '+line[0:10]
            print 'l: '+line
f.close()

 #For files all dirs:
 	#for tag in TagSystem.txt (ignore "#"-lines): #for playlistfiles: 
 		#if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
					#Add filename and relative(/or full) dir
					
					