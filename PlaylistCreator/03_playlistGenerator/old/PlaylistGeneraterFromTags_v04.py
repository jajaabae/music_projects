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
    if len(line)>0:
        print len(line)
        print len(str(line))
        print line[0]
        print line
f.close()

 #For files all dirs:
 	#for tag in TagSystem.txt (ignore "#"-lines): #for playlistfiles: 
 		#if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
					#Add filename and relative(/or full) dir
					
					