import os

#Generate playlistfiles from TagSystem.txt (ignore "#"-lines)
path='storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
path='storage/sdcard0/'
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PyIOFolder'

os.chdir(path)
print os.listdir(os.getcwd())

#f=open('TagSystem.txt')
#f.close()

 #For files all dirs:
 	#for tag in TagSystem.txt (ignore "#"-lines): #for playlistfiles: 
 		#if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
					#Add filename and relative(/or full) dir
					
					